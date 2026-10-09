"""Read-only integrity checks for the transaction dataset and derived artifacts."""
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from data_paths import require_synthetic_reference, data_path

ID = 'Identifikace transakce'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(name):
    with data_path(name).open(encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle, delimiter=';')
        rows = list(reader)
        require(bool(rows), f'{name}: prázdný soubor')
        require(all(None not in row and None not in row.values() for row in rows), f'{name}: poškozená struktura CSV')
        require(all('\ufffd' not in value for row in rows for value in row.values()), f'{name}: poškozené kódování')
        return reader.fieldnames, rows


def unique(rows, column, name):
    result = {row[column]: row for row in rows}
    require(len(result) == len(rows), f'{name}: duplicitní {column}')
    require(all(result), f'{name}: prázdný {column}')
    return result


def main():
    loaded = {name: read(name) for name in [
        'data_all.csv', 'data_synthetic.csv', 'data_combined.csv',
        'original_profiles.csv', 'synthetic_profiles.csv', 'category_dictionary.csv',
        'category_mapping.csv', 'main_category_dictionary.csv', 'original_classification_audit.csv']}
    reference = loaded['data_all.csv'][1]
    require_synthetic_reference(reference)
    synthetic = loaded['data_synthetic.csv'][1]
    require(all(row[ID].startswith('SYN-') for row in synthetic), 'Hlavní sada musí mít identifikátory SYN-')
    combined = loaded['data_combined.csv'][1]
    header = loaded['data_all.csv'][0]
    require(header == loaded['data_synthetic.csv'][0] == loaded['data_combined.csv'][0], 'Výpisy mají různá schémata')
    signature = lambda row: tuple(row[key] for key in header)
    require(Counter(map(signature, combined)) == Counter(map(signature, reference + synthetic)), 'Společný výpis neodpovídá zdrojům')
    require(len(set(map(signature, combined))) == len(combined), 'Zcela duplicitní transakce')
    om = unique(loaded['original_profiles.csv'][1], ID, 'Referenční syntetická metadata')
    sm = unique(loaded['synthetic_profiles.csv'][1], ID, 'Syntetická metadata')
    require(set(om).isdisjoint(sm), 'Identifikátory zdrojů se překrývají')
    metadata = {**om, **sm}
    for rows, index, flag in [(reference, om, '1'), (synthetic, sm, '1')]:
        require({row[ID] for row in rows} == set(index), 'Metadata neodpovídají výpisu')
        require(all(row['Synteticka'] == flag for row in index.values()), 'Chybný zdroj metadat')
    groups = defaultdict(list)
    for row in combined:
        require(bool(row['Mena'].strip()), 'Prázdná měna')
        amount = Decimal(row['Castka'].replace(',', '.'))
        require(amount.is_finite(), 'Neplatná částka')
        for field in ['Datum zauctovani', 'Datum provedeni']:
            datetime.strptime(row[field], '%d.%m.%Y')
        groups[row[ID]].append(row)
    for identity, rows in groups.items():
        if len(rows) > 1:
            require(identity in om and len(rows) == 2 and {r['Mena'] for r in rows} == {'CZK', 'EUR'}
                    and all('vyrovnávací' in r['Typ transakce'].lower() for r in rows)
                    and Decimal(rows[0]['Castka'].replace(',', '.')) * Decimal(rows[1]['Castka'].replace(',', '.')) < 0
                    and metadata[identity]['Kategorie'] == 'směna měn', f'Nejasná duplicita: {identity}')
    require(len(sm) == len(synthetic), 'Syntetický výpis má duplicitní ID')
    mapping = unique(loaded['category_mapping.csv'][1], 'Puvodni kategorie', 'Mapování')
    dictionary = unique(loaded['category_dictionary.csv'][1], 'Kod kategorie', 'Číselník')
    require(len({r['Kategorie'] for r in dictionary.values()}) == len(dictionary), 'Duplicitní názvy kategorií')
    for row in metadata.values():
        require(row['Kategorie'] in mapping, 'Kategorie bez mapování')
    for row in mapping.values():
        require(row['Kod kategorie'] in dictionary, 'Mapování na neexistující kód')
        expected = dictionary[row['Kod kategorie']]
        require(all(row[col] == expected[col] for col in ['Kategorie', 'Kod hlavni kategorie', 'Hlavni kategorie']), 'Nesoulad mapování a číselníku')
    def counts(rows):
        return Counter(mapping[row['Kategorie']]['Kod kategorie'] for row in rows)
    for rows, column in [
        ([om[r[ID]] for r in reference], 'Cetnost originalni radky'),
        (list(om.values()), 'Cetnost originalni identifikatory'),
        ([sm[r[ID]] for r in synthetic], 'Cetnost synteticke radky'),
        (list(sm.values()), 'Cetnost synteticke identifikatory'),
        ([metadata[r[ID]] for r in combined], 'Cetnost spolecne radky')]:
        actual = counts(rows)
        require(all(int(row[column]) == actual[code] for code, row in dictionary.items()), f'Neaktuální četnost: {column}')
    main_groups = unique(loaded['main_category_dictionary.csv'][1], 'Kod hlavni kategorie', 'Hlavní skupiny')
    require({r['Kod hlavni kategorie'] for r in dictionary.values()} <= set(main_groups), 'Chybějící hlavní skupina')
    for code, row in main_groups.items():
        members = [r for r in dictionary.values() if r['Kod hlavni kategorie'] == code]
        require(int(row['Pocet kategorii']) == len(members), 'Nesoulad počtu kategorií ve skupině')
        for col in row:
            if col.startswith('Cetnost '):
                require(int(row[col]) == sum(int(r[col]) for r in members), f'Neaktuální skupina: {code}, {col}')
    audit = unique(loaded['original_classification_audit.csv'][1], ID, 'Audit')
    require(set(audit) == set(om), 'Nesoulad identifikátorů auditu')
    require(all(audit[key]['Kategorie'] == row['Kategorie'] for key, row in om.items()), 'Neaktuální kategorie auditu')
    catalog = json.loads(Path(__file__).with_name('merchant_catalog.json').read_text(encoding='utf-8'))
    for row in synthetic:
        category = sm[row[ID]]['Kategorie']
        require(category in catalog or category == 'osobní převod', f'Kategorie není v katalogu: {category}')
        allowed = ({r['Jmeno'] for r in sm.values()} if category == 'osobní převod'
                   else {r['name'] for r in catalog[category] if r.get('enabled_for_generation')})
        require(row['Nazev protiuctu'] in allowed, f'Nepovolená syntetická protistrana: {category}')
        amount = Decimal(row['Castka'].replace(',', '.'))
        require(not ('Příchozí' in row['Typ transakce'] and amount <= 0), 'Záporná příchozí úhrada')
        require(not ('Odchozí' in row['Typ transakce'] and amount >= 0), 'Kladná odchozí úhrada')
    print(f'OK: {len(combined)} řádků, {len(metadata)} identifikátorů, {len(dictionary)} kategorií; návaznosti jsou konzistentní.')


if __name__ == '__main__':
    main()
