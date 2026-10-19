#!/usr/bin/env python3
"""Export the explicitly assigned Anki decks through the study skills' store.

Reads Anki only. ZIP originals preserve raw fields, card IDs, note types and
referenced media; UTF-8 transcripts provide stable, searchable line citations.
"""

import argparse
import base64
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import sqlite3
import tempfile
import unicodedata
from urllib.parse import unquote, urlparse
from zoneinfo import ZoneInfo
import zipfile


ASSIGNMENTS = {
    "Goodfellow": ("goodfellow", "Goodfellow"),
    "before OSU::2 LLMs whitepapers": ("llms-whitepapers", "LLMs whitepapers"),
    "before OSU::3 BI-ML1": ("bi-ml1", "BI-ML1"),
    "before OSU::4 BI-ML2": ("bi-ml2", "BI-ML2"),
    "before OSU::5 BI-ZUM": ("bi-zum", "BI-ZUM"),
    **{f"before OSU::{name}": (name.lower(), name) for name in (
        "BI-AG1", "BI-DML", "BI-LA1", "BI-MA1", "BI-MA2", "BI-PA1",
        "BI-PA2", "NI-MKY", "NI-MPI", "NI-VSM",
    )},
    "before OSU::Pravděpodobnost a statistika": (
        "pravdepodobnost-a-statistika", "Pravděpodobnost a statistika"
    ),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")[:44].rstrip("-") or "obsah"


class ReadableHTML(HTMLParser):
    """Keep math notation and code whitespace; mark images without guessing them."""

    blocks = {"p", "div", "section", "article", "blockquote", "pre", "h1", "h2", "h3", "h4"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.lists = []
        self.skip = 0
        self.links = []
        self.media = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style"}:
            self.skip += 1
        if self.skip:
            return
        if tag in self.blocks:
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag in {"ul", "ol"}:
            self.lists.append([tag, 0])
            self.parts.append("\n")
        elif tag == "li":
            if self.lists:
                self.lists[-1][1] += 1
            prefix = f"{self.lists[-1][1]}. " if self.lists and self.lists[-1][0] == "ol" else "- "
            self.parts.append("\n" + prefix)
        elif tag in {"b", "strong"}:
            self.parts.append("**")
        elif tag in {"sub", "sup"}:
            self.parts.append(f"<{tag}>")
        elif tag == "code":
            self.parts.append("`")
        elif tag == "tr":
            self.parts.append("\n| ")
        elif tag in {"td", "th"}:
            pass
        elif tag == "a":
            self.links.append(attrs.get("href", ""))
        elif tag in {"img", "audio", "video", "source"}:
            ref = attrs.get("src", "")
            if ref:
                self.media.add(ref)
                label = "Obrázek" if tag == "img" else "Médium"
                self.parts.append(f" [{label}: {ref}; soubor je v media/ v doprovodném ZIP] ")
                if attrs.get("alt"):
                    self.parts.append(f"(původní alt: {attrs['alt']}) ")

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in self.blocks:
            self.parts.append("\n\n")
        elif tag in {"ul", "ol"}:
            if self.lists:
                self.lists.pop()
            self.parts.append("\n")
        elif tag in {"b", "strong"}:
            self.parts.append("**")
        elif tag in {"sub", "sup"}:
            self.parts.append(f"</{tag}>")
        elif tag == "code":
            self.parts.append("`")
        elif tag in {"td", "th"}:
            self.parts.append(" | ")
        elif tag == "a" and self.links:
            href = self.links.pop()
            if href:
                self.parts.append(f" ({href})")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def readable(self, value):
        self.feed(value)
        self.close()
        result = "".join(self.parts).replace("\xa0", " ")
        return re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", result).strip()


def plain(value):
    return ReadableHTML().readable(value)


def protobuf_strings(data):
    """Read top-level string fields, retaining the full config separately."""
    def varint(pos):
        result = shift = 0
        while pos < len(data):
            byte = data[pos]
            pos += 1
            result |= (byte & 127) << shift
            if not byte & 128:
                return result, pos
            shift += 7
            if shift > 70:
                raise ValueError("Invalid protobuf varint")
        raise ValueError("Truncated protobuf")

    result = {}
    pos = 0
    while pos < len(data):
        key, pos = varint(pos)
        wire = key & 7
        if wire == 0:
            _, pos = varint(pos)
        elif wire in {1, 5}:
            pos += 8 if wire == 1 else 4
        elif wire == 2:
            length, pos = varint(pos)
            raw = data[pos:pos + length]
            pos += length
            try:
                result[key >> 3] = raw.decode("utf-8")
            except UnicodeDecodeError:
                pass
        else:
            raise ValueError(f"Unsupported protobuf wire type: {wire}")
    return result


def jsonable(row):
    return {k: ({"base64": base64.b64encode(v).decode()} if isinstance(v, bytes) else v)
            for k, v in dict(row).items()}


def subject_for(deck):
    matches = [(root, value) for root, value in ASSIGNMENTS.items()
               if deck == root or deck.startswith(root + "::")]
    if len(matches) != 1:
        raise ValueError(f"Deck has no unambiguous approved assignment: {deck}")
    return matches[0]


def group_for(root, subject, deck, note, position, deck_total):
    if deck != root:
        title = deck[len(root) + 2:]
        return slug(title), title
    tags = note["tags"].split()
    if subject == "goodfellow":
        start = (position // 100) * 100 + 1
        return f"blok-{position // 100 + 1:02}", f"Blok {position // 100 + 1:02} – karty {start}–{min(start + 99, deck_total)}"
    patterns = {
        "llms-whitepapers": r"B(\d+)_\d+",
        "bi-ml2": r"Prednaska_(\d+)",
        "bi-zum": r"AI_combined::(.+)",
        "pravdepodobnost-a-statistika": r"konsolidace::blok_(\d+)",
    }
    if subject in patterns:
        found = [re.fullmatch(patterns[subject], tag, re.I) for tag in tags]
        values = sorted({m.group(1) for m in found if m})
        if values:
            label = values[0]
            if subject == "bi-zum":
                title = label.replace("_", " ")
            elif subject == "bi-ml2":
                title = f"Přednáška {int(label):02}"
            else:
                title = f"Původní blok {int(label):02}"
            return slug(title), title
    specific = sorted(tag for tag in tags if re.fullmatch(re.escape(subject) + r"::p\d+", tag, re.I))
    if not specific:
        specific = sorted(tag for tag in tags if re.fullmatch(re.escape(subject) + r"::c\d+", tag, re.I))
    if specific:
        label = specific[0].split("::")[-1]
        title = ("Přednáška " if label[0] == "p" else "Cvičení ") + label[1:]
        return slug(title), title
    return "zakladni-sada", "Základní sada otázek"


def build_groups(con):
    decks = {r["id"]: dict(r) for r in con.execute("SELECT * FROM decks")}
    for deck in decks.values():
        deck["name"] = deck["name"].replace(chr(31), "::")
    notes = {r["id"]: dict(r) for r in con.execute("SELECT * FROM notes")}
    cards = [dict(r) for r in con.execute("SELECT id,nid,did,ord,odid FROM cards ORDER BY id")]
    by_deck = defaultdict(list)
    for card in cards:
        by_deck[card["odid"] or card["did"]].append(card)
    groups = {}
    for did, deck_cards in sorted(by_deck.items(), key=lambda item: decks[item[0]]["name"]):
        deck = decks[did]["name"]
        root, (subject, subject_name) = subject_for(deck)
        deck_notes = sorted({c["nid"] for c in deck_cards})
        for position, nid in enumerate(deck_notes):
            note = notes[nid]
            topic_id, topic_title = group_for(root, subject, deck, note, position, len(deck_notes))
            # Root topics and subdeck topics must not accidentally share an ID.
            if deck != root:
                topic_id = "balicek-" + topic_id
            key = subject, topic_id
            group = groups.setdefault(key, dict(subject=subject, name=subject_name,
                                               topic_id=topic_id, title=topic_title,
                                               root=root, decks=set(), notes={}, cards=[]))
            group["decks"].add(did)
            group["notes"][nid] = note
            group["cards"].extend(c for c in deck_cards if c["nid"] == nid)
    return groups, decks, notes, cards


def media_refs(value):
    parser = ReadableHTML()
    parser.readable(value)
    refs = parser.media
    refs.update(re.findall(r"\[sound:([^\]]+)\]", value))
    refs.update(re.findall(r"url\([\"']?([^\)\"']+)", value, re.I))
    return refs


def export_group(con, group, decks, media_dir, staging, version, snapshot_hash,
                 origin_label="místní Anki, profil User 1", source_notice=None):
    sid = "anki-" + group["topic_id"] + "-v1"
    if len(sid) > 64:
        raise ValueError(f"Source ID too long: {sid}")
    target = staging / group["subject"] / sid
    target.mkdir(parents=True)
    archive = target / (sid + ".zip")
    transcript = target / (sid + ".md")
    type_ids = {n["mid"] for n in group["notes"].values()}
    types = []
    field_names = {}
    refs = set()
    macros = set()
    for ntid in sorted(type_ids):
        nt = con.execute("SELECT * FROM notetypes WHERE id=?", (ntid,)).fetchone()
        fields = con.execute("SELECT * FROM fields WHERE ntid=? ORDER BY ord", (ntid,)).fetchall()
        templates = con.execute("SELECT * FROM templates WHERE ntid=? ORDER BY ord", (ntid,)).fetchall()
        field_names[ntid] = [row["name"] for row in fields]
        configs = protobuf_strings(nt["config"])
        decoded_templates = []
        refs.update(media_refs(configs.get(3, "")))
        for template in templates:
            strings = protobuf_strings(template["config"])
            for raw in (strings.get(1, ""), strings.get(2, "")):
                refs.update(media_refs(raw))
                # Keep the complete original macro lines; do not expand math by guesswork.
                macros.update(line.strip() for line in raw.splitlines() if line.strip().startswith("\\def\\"))
            decoded_templates.append(dict(original=jsonable(template), string_fields=strings))
        types.append(dict(original=jsonable(nt), fields=[jsonable(r) for r in fields],
                          string_fields=configs, templates=decoded_templates))
    lines = [f"# {group['name']} – {group['title']}", "",
             f"Původ: {origin_label}. Jde o export kartiček, nikoli ověřené znění učebnice.",
             f"Verze exportu: {version}. Původní kolekce SHA-256: {snapshot_hash}.",
             "Původní balíčky: " + "; ".join(decks[did]["name"] for did in sorted(group["decks"])),
             f"Rozsah: {len(group['notes'])} poznámek, {len(group['cards'])} karet.",
             "ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.",
             "Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.",
             "Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.", ""]
    if source_notice:
        lines.extend([source_notice, ""])
    if group["subject"] == "goodfellow":
        lines.extend(["Bloky jsou pracovní dělení po 100 otázkách v pořadí ID poznámek; neoznačují kapitoly knihy.", ""])
    if macros:
        lines += ["## Původní definice matematických maker", "", "```tex", *sorted(macros), "```", ""]
    raw_notes = []
    card_index = []
    for note in sorted(group["notes"].values(), key=lambda n: n["id"]):
        values = note["flds"].split(chr(31))
        labels = field_names[note["mid"]]
        if len(labels) != len(values):
            raise ValueError(f"Field count differs for note {note['id']}")
        note_cards = [c for c in group["cards"] if c["nid"] == note["id"]]
        lines.extend([f"## Poznámka Anki {note['id']}", "",
                      "Karty Anki: " + ", ".join(str(c["id"]) for c in note_cards),
                      f"GUID: {note['guid']}; štítky: {note['tags'].strip() or '(žádné)' }.", ""])
        for card in note_cards:
            flag = card.get("flags", 0) & 7
            messages = {1: "červený příznak autora: chyba nebo určeno ke kontrole",
                        2: "oranžový příznak autora: určeno k odstranění",
                        3: "zelený příznak autora: duplicita",
                        4: "modrý příznak autora: v poslední verzi upraveno"}
            status = []
            if flag:
                status.append(messages.get(flag, f"původní příznak autora {flag}"))
            if card.get("queue") == -1:
                status.append("v původním balíčku pozastavená karta")
            if status:
                lines.extend([f"Metadata původního zdroje pro kartu {card['id']}: " + "; ".join(status) + ".", ""])
        start_line = len(lines) + 1
        raw_fields = []
        for label, value in zip(labels, values):
            refs.update(media_refs(value))
            readable = plain(value)
            friendly = {"Front": "Otázka (Front)", "Back": "Odpověď (Back)",
                        "Extra": "Doplňující pole (Extra)"}.get(label, label)
            lines.extend([f"### {friendly}", "", *(readable.splitlines() or ["(prázdné pole)"]), ""])
            raw_fields.append(dict(name=label, html=value))
        raw_notes.append(dict(id=note["id"], guid=note["guid"], note_type_id=note["mid"],
                              tags=note["tags"], original_flds=note["flds"], fields=raw_fields))
        card_index.append(dict(note_id=note["id"], card_ids=[c["id"] for c in note_cards],
                               locator=f"transcript-line:{start_line}",
                               question=" ".join(plain(values[0]).split())[:240]))
    media = []
    missing = []
    external = []
    for ref in sorted(refs):
        if "{{" in ref:
            continue  # Anki template placeholders are resolved by the note fields.
        if urlparse(ref).scheme or ref.startswith("//"):
            external.append(ref)
            continue
        filename = unquote(ref)
        path = media_dir / filename
        if path.is_file() and path.resolve().is_relative_to(media_dir.resolve()):
            media.append((ref, path))
        else:
            missing.append(ref)
    if missing:
        lines += ["## Chybějící místní média", "", *(f"- {ref}" for ref in missing), ""]
    if external:
        lines += ["## Externí média", "", "Odkazy zůstaly zachované, obsah nebyl stažen.", "",
                  *(f"- {ref[:300]}" for ref in external), ""]
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("original-notes.json", json.dumps(raw_notes, ensure_ascii=False, indent=2) + "\n")
        z.writestr("cards.json", json.dumps(group["cards"], ensure_ascii=False, indent=2) + "\n")
        z.writestr("note-types.json", json.dumps(types, ensure_ascii=False, indent=2) + "\n")
        z.writestr("decks.json", json.dumps([jsonable(decks[did]) for did in sorted(group["decks"])], ensure_ascii=False, indent=2) + "\n")
        media_hashes = []
        for ref, path in media:
            member = "media/" + path.name
            data = path.read_bytes()
            if member not in z.namelist():
                z.writestr(member, data)
            media_hashes.append(dict(reference=ref, member=member, sha256=sha(data)))
        package = dict(format="anki-study-export-v1", version=version, subject_id=group["subject"],
                       topic_id=group["topic_id"], source_id=sid, collection_sha256=snapshot_hash,
                       media=media_hashes, missing_media=missing, external_media=external,
                       note_count=len(raw_notes), card_count=len(group["cards"]),
                       card_index=card_index)
        z.writestr("manifest.json", json.dumps(package, ensure_ascii=False, indent=2) + "\n")
    transcript.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dict(subject_id=group["subject"], topic_id=group["topic_id"], source_id=sid,
                title=group["title"], archive=str(archive), transcript=str(transcript),
                notes=len(raw_notes), cards=len(group["cards"]), media=len(media),
                missing_media=missing, external_media=external, card_index=card_index)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collection", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--store-script", type=Path, required=True)
    parser.add_argument("--apply", action="store_true", help="Register the user-approved assignment")
    args = parser.parse_args()
    if not args.root.is_absolute() or not args.collection.is_absolute():
        parser.error("Collection and store root must be absolute paths")
    spec = importlib.util.spec_from_file_location("shared_study_store", args.store_script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    store = module.StudyStore(args.root)
    existing = {s["subject_id"] for s in store.subjects()}
    assigned = {sid for sid, _ in ASSIGNMENTS.values()}
    if args.apply and assigned & existing:
        raise ValueError("Import will not overwrite existing subjects: " + ", ".join(sorted(assigned & existing)))
    version = datetime.now(ZoneInfo("Europe/Prague")).isoformat(timespec="seconds")
    report = dict(format="anki-study-import-v1", export_version=version,
                  assignment_confirmed="User approved 16 separate subjects in this conversation.",
                  collection=str(args.collection), subjects=[], materials=[])
    with tempfile.TemporaryDirectory(prefix="anki-study-import-") as temporary:
        temporary = Path(temporary)
        database = temporary / "collection.anki2"
        # Copy only into temporary storage. Never open the live Anki DB for writes.
        for attempt in range(3):
            originals = {}
            for suffix in ("", "-wal"):
                incoming = Path(str(args.collection) + suffix)
                destination = Path(str(database) + suffix)
                if incoming.exists():
                    data = incoming.read_bytes()
                    destination.write_bytes(data)
                    originals[suffix] = sha(data)
                else:
                    destination.unlink(missing_ok=True)
            if all(sha(Path(str(args.collection) + suffix).read_bytes()) == digest
                   for suffix, digest in originals.items()):
                break
        else:
            raise ValueError("Anki collection is changing; could not obtain a stable snapshot")
        report["original_hashes_before"] = originals
        con = sqlite3.connect(database)
        con.row_factory = sqlite3.Row
        con.create_collation("unicase", lambda a, b: (a.casefold() > b.casefold()) - (a.casefold() < b.casefold()))
        con.execute("PRAGMA query_only=ON")
        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise ValueError(f"Snapshot integrity check failed: {integrity}")
        groups, decks, notes, cards = build_groups(con)
        seen_subjects = {key[0] for key in groups}
        if seen_subjects != assigned:
            raise ValueError(f"Subjects missing from snapshot: {assigned - seen_subjects}")
        for subject, name in sorted(ASSIGNMENTS.values()):
            materials = [g for (sid, _), g in groups.items() if sid == subject]
            summary = dict(subject_id=subject, name=name, topics=len(materials),
                           notes=len({nid for g in materials for nid in g["notes"]}),
                           cards=sum(len(g["cards"]) for g in materials))
            report["subjects"].append(summary)
        report.update(snapshot_integrity=integrity, total_notes=len(notes), total_cards=len(cards),
                      nonempty_decks=len({c["odid"] or c["did"] for c in cards}),
                      total_topics=len(groups))
        if not args.apply:
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return
        # Validate every export before creating subjects or registering sources.
        staging = temporary / "exports"
        exports = {}
        for key, group in sorted(groups.items()):
            exports[key] = export_group(con, group, decks, args.collection.parent / "collection.media",
                                        staging, version, originals[""])
        # State is changed exclusively through the skills' shared storage tool.
        for subject, name in sorted(ASSIGNMENTS.values()):
            store.init(subject, name, [f"Porozumět obsahu Anki balíčku {name}, vysvětlovat odpovědi a samostatně řešit jeho otázky a úlohy."])
            store.sources(subject)
        for key, group in sorted(groups.items()):
            result = exports[key]
            sid = group["subject"]
            tid = group["topic_id"]
            store.topic_add(sid, tid, group["title"],
                            [f"Vysvětlit odpovědi a samostatně zodpovědět otázky sady „{group['title']}“ z balíčku {group['name']}."], [])
            provenance = (
                f"Export z místního Anki profilu User 1, kolekce {args.collection}, verze {version}. "
                "ZIP je původní strojový export polí HTML, identifikátorů, šablon a médií; "
                "Markdown je odvozený čitelný přepis pomocí HTMLParser, bez doplňování učiva. "
                "Podtržítka a horní indexy HTML zůstávají jako sub/sup, MathJax/TeX se zachovává. "
                "Přesný přepis se cituje transcript-line:N. Obrázky a vzorce vyžadují před výukou vizuální kontrolu. "
                "Odkazy na externí dokumenty nebyly načtené. Import nezapisuje výsledky studenta."
            )
            source = store.source_add(sid, result["source_id"], result.pop("archive"),
                                      f"Anki – {group['name']} – {group['title']}", version, "primary",
                                      transcript=result.pop("transcript"), note=provenance)
            if not source["indexed"]:
                raise ValueError(f"Transcript not indexed: {source['source_id']}")
            store.source_link(sid, source["source_id"], tid)
            result.update(file=source["file"], transcript_file=source["transcript_file"],
                          sha256=source["sha256"], transcript_sha256=source["transcript_sha256"])
            report["materials"].append(result)
            print(json.dumps({"imported": sid, "topic": tid, "cards": result["cards"],
                              "missing_media": result["missing_media"]}, ensure_ascii=False), flush=True)
        con.close()
        report["original_hashes_after"] = {
            suffix: sha(Path(str(args.collection) + suffix).read_bytes())
            for suffix in originals
        }
        report["anki_files_unchanged"] = report["original_hashes_after"] == originals
        report["imported_cards"] = sum(m["cards"] for m in report["materials"])
        if report["imported_cards"] != len(cards):
            raise ValueError("Card coverage mismatch")
        out = args.root / "imports" / "anki-2026-10-17"
        out.mkdir(parents=True, exist_ok=True)
        (out / "manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"report": str(out / 'manifest.json'), "subjects": len(report['subjects']),
                          "topics": report['total_topics'], "cards": report['imported_cards'],
                          "anki_files_unchanged": report['anki_files_unchanged']}, ensure_ascii=False))


if __name__ == "__main__":
    main()
