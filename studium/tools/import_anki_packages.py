#!/usr/bin/env python3
"""Add missing subject decks from a local APKG directory to the study library."""

import argparse
from collections import Counter, defaultdict
import ctypes
import ctypes.util
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sqlite3
import tempfile
from zoneinfo import ZoneInfo
import zipfile

from import_anki import export_group, sha, slug


class Zstd:
    def __init__(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("zstd"))
        self.lib.ZSTD_decompressBound.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
        self.lib.ZSTD_decompressBound.restype = ctypes.c_ulonglong
        self.lib.ZSTD_decompress.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t]
        self.lib.ZSTD_decompress.restype = ctypes.c_size_t
        self.lib.ZSTD_isError.argtypes = [ctypes.c_size_t]
        self.lib.ZSTD_isError.restype = ctypes.c_uint

    def decode(self, data):
        if not data.startswith(b"\x28\xb5\x2f\xfd"):
            return data
        bound = self.lib.ZSTD_decompressBound(data, len(data))
        if not 0 <= bound < 500_000_000:
            raise ValueError(f"Unexpected decompressed size: {bound}")
        buffer = ctypes.create_string_buffer(bound)
        size = self.lib.ZSTD_decompress(buffer, bound, data, len(data))
        if self.lib.ZSTD_isError(size):
            raise ValueError("Invalid Zstandard stream")
        return buffer.raw[:size]


def protobuf(data):
    def varint(position):
        value = shift = 0
        while position < len(data):
            byte = data[position]
            position += 1
            value |= (byte & 127) << shift
            if not byte & 128:
                return value, position
            shift += 7
            if shift > 70:
                break
        raise ValueError("Invalid protobuf varint")

    position = 0
    while position < len(data):
        key, position = varint(position)
        wire = key & 7
        if wire == 0:
            value, position = varint(position)
        elif wire == 2:
            length, position = varint(position)
            value = data[position:position + length]
            if len(value) != length:
                raise ValueError("Truncated protobuf field")
            position += length
        else:
            raise ValueError(f"Unexpected protobuf wire type {wire}")
        yield key >> 3, value


def unpack_package(path, work, decoder):
    directory = work / path.stem.lower()
    directory.mkdir()
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:
            raise ValueError(f"Invalid ZIP checksum: {path}")
        member = next((name for name in ("collection.anki21b", "collection.anki21", "collection.anki2")
                       if name in z.namelist()), None)
        if member is None:
            raise ValueError(f"No database in {path}")
        database = directory / "collection.anki2"
        database.write_bytes(decoder.decode(z.read(member)))
        con = sqlite3.connect(database)
        con.row_factory = sqlite3.Row
        con.create_collation("unicase", lambda a, b: (a.casefold() > b.casefold()) - (a.casefold() < b.casefold()))
        con.execute("PRAGMA query_only=ON")
        if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError(f"Database integrity failed: {path}")
        decks = {r["id"]: dict(r) for r in con.execute("SELECT * FROM decks")}
        for deck in decks.values():
            deck["name"] = deck["name"].replace(chr(31), "::")
        notes = {r["id"]: dict(r) for r in con.execute("SELECT * FROM notes")}
        cards = [dict(r) for r in con.execute("SELECT * FROM cards ORDER BY id")]
        active = {decks[c["odid"] or c["did"]]["name"].split("::")[0] for c in cards}
        if len(active) != 1:
            raise ValueError(f"Package is not one subject: {path}: {active}")
        name = active.pop()
        sid = name.lower()
        if not re.fullmatch(r"[a-z]+-[a-z0-9]+", sid):
            raise ValueError(f"Unexpected subject code: {name}")
        media_dir = directory / "collection.media"
        media_dir.mkdir()
        media_data = decoder.decode(z.read("media"))
        if media_data.lstrip().startswith(b"{"):
            mapping = [(number, filename, None, None) for number, filename in json.loads(media_data).items()]
        else:
            entries = [value for number, value in protobuf(media_data) if number == 1]
            mapping = []
            for number, entry in enumerate(entries):
                values = dict(protobuf(entry))
                mapping.append((str(number), values[1].decode("utf-8"), values.get(2), values.get(3)))
        for member_name, filename, size, expected_sha1 in mapping:
            if Path(filename).name != filename or "\\" in filename:
                raise ValueError(f"Unsafe media filename: {filename}")
            data = decoder.decode(z.read(member_name))
            if size is not None and len(data) != size:
                raise ValueError(f"Media size mismatch: {filename}")
            if expected_sha1 is not None and hashlib.sha1(data).digest() != expected_sha1:
                raise ValueError(f"Media SHA-1 mismatch: {filename}")
            (media_dir / filename).write_bytes(data)
    return dict(subject=sid, name=name, con=con, decks=decks, notes=notes, cards=cards,
                media_dir=media_dir, database_hash=sha(database.read_bytes()),
                media_count=len(mapping))


def groups_for(package):
    groups = {}
    by_note = defaultdict(list)
    for card in package["cards"]:
        by_note[card["nid"]].append(card)
    for nid, note in sorted(package["notes"].items()):
        cards = by_note[nid]
        if not cards:
            raise ValueError(f"Unassigned note in {package['name']}: {nid}")
        tags = note["tags"].split()
        candidates = []
        for kind, prefix in (("p", "Přednáška"), ("ps", "Proseminář"), ("c", "Cvičení")):
            for tag in tags:
                match = re.fullmatch(re.escape(package["subject"]) + f"::{kind}(\\d+)", tag, re.I)
                if match:
                    candidates.append((int(match.group(1)), prefix))
            if candidates:
                break
        if candidates:
            number, prefix = sorted(candidates)[0]
            title = f"{prefix} {number:02}"
        else:
            title = "Základní sada otázek"
        tid = slug(title)
        group = groups.setdefault(tid, dict(subject=package["subject"], name=package["name"],
                                            topic_id=tid, title=title, decks=set(), notes={}, cards=[]))
        group["notes"][nid] = note
        group["cards"].extend(cards)
        group["decks"].update(c["odid"] or c["did"] for c in cards)
    return groups


def verify(store, report, expected, baseline):
    seen_cards = Counter()
    seen_notes = Counter()
    media = set()
    queries = []
    for item in report["materials"]:
        sid, tid, source_id = item["subject_id"], item["topic_id"], item["source_id"]
        state = store.load(sid)
        assert not state["checkpoints"]
        assert state["topics"][tid]["status"] == "unseen"
        source = state["sources"][source_id]
        store.verify_source(sid, source)
        assert source["indexed"] and source["topic_ids"] == [tid]
        transcript = (store.directory(sid) / source["transcript_file"]).read_text().splitlines()
        passages = store.passages(sid, source_id, 0, len(source["passages"]))["passages"]
        locators = {p["locator"] for p in passages}
        for passage in passages:
            prefix, number = passage["locator"].split(":")
            assert prefix == "transcript-line" and transcript[int(number) - 1] == passage["text"]
        with zipfile.ZipFile(store.directory(sid) / source["file"]) as z:
            assert z.testzip() is None
            manifest = json.loads(z.read("manifest.json"))
            for note in json.loads(z.read("original-notes.json")):
                original = expected[sid]["notes"][note["id"]]
                assert original["flds"] == note["original_flds"]
                assert original["tags"] == note["tags"]
                assert original["guid"] == note["guid"]
                assert original["mid"] == note["note_type_id"]
                assert note["original_flds"].split(chr(31)) == [f["html"] for f in note["fields"]]
                seen_notes[sid, note["id"]] += 1
            for card in json.loads(z.read("cards.json")):
                assert expected[sid]["cards"][card["id"]] == card
                seen_cards[sid, card["id"]] += 1
            for attachment in manifest["media"]:
                data = z.read(attachment["member"])
                assert sha(data) == attachment["sha256"]
                media.add(attachment["sha256"])
            for card in manifest["card_index"]:
                assert card["locator"] in locators
        heading = next(i for i, p in enumerate(passages) if p["text"].startswith("## Poznámka Anki "))
        field = next(i for i in range(heading + 1, len(passages)) if passages[i]["text"].startswith("### "))
        query = passages[field + 1]["text"]
        result = store.search(sid, query, tid, 0, 10)
        assert any(hit["source_id"] == source_id for hit in result["matches"])
        assert not result["unindexed_sources"]
        queries.append(dict(subject_id=sid, topic_id=tid, source_id=source_id,
                            query=query[:180], locator=result["matches"][0]["locator"]))
    expected_notes = {(sid, nid) for sid, values in expected.items() for nid in values["notes"]}
    expected_cards = {(sid, cid) for sid, values in expected.items() for cid in values["cards"]}
    assert set(seen_notes) == expected_notes and all(count == 1 for count in seen_notes.values())
    assert set(seen_cards) == expected_cards and all(count == 1 for count in seen_cards.values())
    changed_states = []
    for path, expected_hash in baseline.items():
        if sha(Path(path).read_bytes()) != expected_hash:
            if Path(path).name != "state.json":
                raise ValueError(f"Existing material changed: {path}")
            changed_states.append(path)
    for package in report["inventory"]:
        assert sha(Path(package["path"]).read_bytes()) == package["sha256"]
    for item in report["subjects"]:
        store.resume(item["subject_id"], "2026-10-17")
    return dict(status="passed", subjects=len(report["subjects"]), materials=len(report["materials"]),
                notes_verified=len(seen_notes), cards_verified=len(seen_cards),
                unique_media_contents=len(media), hashes_and_citations_verified=True,
                topic_searches_verified=len(queries), source_packages_unchanged=True,
                existing_library_materials_unchanged=True,
                concurrent_existing_state_changes=changed_states,
                missing_media=sum(len(item["missing_media"]) for item in report["materials"]),
                new_checkpoints=0, search_samples=queries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", required=True, type=Path)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--store-script", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("study_store", args.store_script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    store = module.StudyStore(args.root)
    existing = {s["subject_id"] for s in store.subjects()}
    baseline = {str(p): sha(p.read_bytes()) for p in (args.root / "subjects").rglob("*")
                if p.is_file() and p.name != ".lock"}
    version = datetime.now(ZoneInfo("Europe/Prague")).isoformat(timespec="seconds")
    report = dict(format="anki-package-study-import-v1", export_version=version,
                  directory=str(args.directory),
                  assignment="Current request 'udělej to samé' repeats one subject per missing deck; BI-PST remains separate by course code.",
                  inventory=[], skipped_existing=[], subjects=[], materials=[])
    decoder = Zstd()
    expected = {}
    exports = []
    with tempfile.TemporaryDirectory(prefix="anki-package-study-") as temporary:
        work = Path(temporary)
        for path in sorted(args.directory.rglob("*.apkg")):
            package = unpack_package(path, work, decoder)
            sid = package["subject"]
            inventory = dict(subject_id=sid, name=package["name"], path=str(path),
                             sha256=sha(path.read_bytes()), database_sha256=package["database_hash"],
                             notes=len(package["notes"]), cards=len(package["cards"]),
                             media=package["media_count"])
            report["inventory"].append(inventory)
            if sid in existing:
                store.sources(sid)
                report["skipped_existing"].append(inventory)
                package["con"].close()
                continue
            if sid in expected:
                raise ValueError(f"Two new packages have the same subject: {sid}")
            groups = groups_for(package)
            flags = Counter(c["flags"] & 7 for c in package["cards"])
            summary = dict(subject_id=sid, name=package["name"], cards=len(package["cards"]),
                           notes=len(package["notes"]), topics=len(groups),
                           author_flags=dict(flags), author_suspended=sum(c["queue"] == -1 for c in package["cards"]))
            report["subjects"].append(summary)
            expected[sid] = dict(notes=package["notes"], cards={c["id"]: c for c in package["cards"]})
            if args.apply:
                notice = ("Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. "
                          "Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, "
                          "zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.")
                for tid, group in sorted(groups.items()):
                    result = export_group(package["con"], group, package["decks"], package["media_dir"],
                                          work / "exports", version, package["database_hash"],
                                          origin_label=f"FIT ČVUT Anki, {path}; APKG SHA-256 {inventory['sha256']}",
                                          source_notice=notice)
                    result["package_path"] = str(path)
                    result["package_sha256"] = inventory["sha256"]
                    exports.append((group, result))
            package["con"].close()
        report["new_cards"] = sum(item["cards"] for item in report["subjects"])
        report["new_topics"] = sum(item["topics"] for item in report["subjects"])
        if not args.apply:
            print(json.dumps({k: v for k, v in report.items() if k != "materials"}, ensure_ascii=False, indent=2))
            return
        # All archives and text exports are validated before any study state changes.
        for subject in report["subjects"]:
            store.init(subject["subject_id"], subject["name"],
                       [f"Porozumět obsahu balíčku {subject['name']}, vysvětlovat odpovědi a samostatně řešit jeho otázky a úlohy."])
            store.sources(subject["subject_id"])
        for group, item in exports:
            sid, tid = item["subject_id"], item["topic_id"]
            store.topic_add(sid, tid, group["title"],
                            [f"Vysvětlit odpovědi a samostatně zodpovědět otázky sady „{group['title']}“ předmětu {group['name']}."], [])
            note = (f"Odvozený export APKG {item['package_path']}, SHA-256 {item['package_sha256']}, verze {version}. "
                    "ZIP obsahuje přesná původní pole, šablony, makra, média a metadata karet včetně autorových příznaků. "
                    "Markdown je čitelný přepis přes HTMLParser; matematika a sub/sup zůstaly zachované. "
                    "Citace jsou transcript-line:N. Před použitím vzorců, obrázků a tabulek provést vizuální kontrolu. "
                    "Původní soubor APKG zůstal na místě; do knihovny se přesouvá vytvořený export a jeho přepis. "
                    "Příznaky chyb a pozastavení jsou upozorněním autora; nepředstavují výsledky studenta.")
            source = store.source_add(sid, item["source_id"], item.pop("archive"),
                                      f"FIT ČVUT Anki – {group['name']} – {group['title']}", version, "primary",
                                      transcript=item.pop("transcript"), note=note)
            if not source["indexed"]:
                raise ValueError(f"Unindexed source: {source['source_id']}")
            store.source_link(sid, source["source_id"], tid)
            item.update(file=source["file"], transcript_file=source["transcript_file"],
                        sha256=source["sha256"], transcript_sha256=source["transcript_sha256"])
            report["materials"].append(item)
            print(json.dumps({"imported": sid, "topic": tid, "cards": item["cards"],
                              "missing_media": item["missing_media"]}, ensure_ascii=False), flush=True)
        out = args.root / "imports" / "fit-cvut-anki-2026-10-17"
        out.mkdir(parents=True, exist_ok=True)
        (out / "manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        verification = verify(store, report, expected, baseline)
        (out / "verification.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({k: v for k, v in verification.items() if k != "search_samples"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
