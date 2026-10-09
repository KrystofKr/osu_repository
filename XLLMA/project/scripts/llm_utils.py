"""Shared local Ollama client and experiment I/O; importing this module does no work."""
import csv
import json
import urllib.error
import urllib.request

ID = 'Identifikace transakce'
INPUT_FIELDS = [
    'Datum provedeni', 'Nazev protiuctu', 'Castka', 'Mena',
    'Typ transakce', 'Popis pro me', 'Zprava pro prijemce',
]


def read_csv(path):
    with path.open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle, delimiter=';'))


def api(base, endpoint, payload=None, timeout=180):
    request = urllib.request.Request(
        base.rstrip('/') + '/api/' + endpoint,
        data=None if payload is None else json.dumps(payload, ensure_ascii=False).encode(),
        headers={'Content-Type': 'application/json'},
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(request, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(
            f'Ollama HTTP {error.code}: {error.read().decode(errors="replace")}'
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(
            'Ollama není dostupná. Ověř ollama list a běh serveru na 127.0.0.1:11434.'
        ) from error


def load_journal(path, repair=False):
    if not path.exists():
        return {}
    records = {}
    lines = path.read_bytes().splitlines(keepends=True)
    valid_bytes = 0
    for index, line in enumerate(lines):
        if line.strip():
            try:
                row = json.loads(line)
            except (json.JSONDecodeError, UnicodeDecodeError) as error:
                if repair and index == len(lines) - 1 and not line.endswith(b'\n'):
                    with path.open('r+b') as handle:
                        handle.truncate(valid_bytes)
                    break
                raise ValueError(
                    'Poškozený journal; neúplný poslední řádek lze obnovit opakováním klasifikace.'
                ) from error
            if not isinstance(row, dict) or not isinstance(row.get(ID), str) or not row[ID]:
                raise ValueError('Záznam journalu musí mít neprázdný textový identifikátor.')
            if row[ID] in records:
                raise ValueError('Duplicitní záznam v journalu.')
            records[row[ID]] = row
        valid_bytes += len(line)
    if repair and path.stat().st_size and not path.read_bytes().endswith(b'\n'):
        with path.open('ab') as handle:
            handle.write(b'\n')
    return records


def write_json(path, data):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def load_taxonomy(path):
    """Read a frozen, model-proposed taxonomy without consulting existing labels."""
    document = json.loads(path.read_text(encoding='utf-8'))
    groups = document['groups']
    categories = document['categories']
    sample_ids = document.get('sample_ids')
    if (document.get('format_version') != 1 or not isinstance(groups,list) or not groups
        or not isinstance(categories,list) or not categories or not isinstance(sample_ids,list)
        or not sample_ids or any(not isinstance(i,str) or not i for i in sample_ids)
        or len(set(sample_ids)) != len(sample_ids)):
        raise ValueError('Neplatná navržená taxonomie.')
    for rows in (groups, categories):
        if any(not isinstance(r,dict) for r in rows):
            raise ValueError('Neplatné položky taxonomie.')
        for field in ('code', 'name'):
            values = [r[field] for r in rows]
            if any(not isinstance(v, str) or not v.strip() for v in values) or len({v.casefold() for v in values}) != len(values):
                raise ValueError('Prázdné nebo duplicitní kódy/názvy taxonomie.')
        if any(not isinstance(r.get('description'), str) or not r['description'].strip() for r in rows):
            raise ValueError('Kategorie musí mít definice.')
    group_codes = {r['code'] for r in groups}
    if any(r['group'] not in group_codes or type(r.get('unknown')) is not bool for r in categories):
        raise ValueError('Neplatná hierarchie taxonomie.')
    if {r['group'] for r in categories} != group_codes or sum(r['unknown'] for r in categories) != 1:
        raise ValueError('Každá hlavní skupina musí být použita; vyžadována je právě jedna neurčená kategorie.')
    dictionary = [{'Kod kategorie': r['code'], 'Kategorie': r['name'],
                   'Kod hlavni kategorie': r['group'], 'Definice': r['description'],
                   'Neurceno': r['unknown']} for r in categories]
    return document, dictionary, {r['code']: r['name'] for r in groups}
