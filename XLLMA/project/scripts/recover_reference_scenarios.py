"""Recover generator labels only after exact reproduction of every REF transaction."""
import csv
import random
import tempfile
from pathlib import Path
from unittest.mock import patch

import generate_synthetic as generator
from data_paths import PROFILE_COLUMNS, data_path, require_synthetic_reference

ID = 'Identifikace transakce'


def read(path):
    with path.open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle, delimiter=';'))


def main():
    reference = read(data_path('data_all.csv'))
    require_synthetic_reference(reference)
    with tempfile.TemporaryDirectory() as directory:
        directory = Path(directory)
        (directory / 'data_all.csv').write_bytes(data_path('data_all.csv').read_bytes())
        with patch.object(generator, 'data_path', lambda name: directory / name), patch.object(generator, 'SEED', 20261010):
            generator.main()
        generated = read(directory / 'data_synthetic.csv')
        metadata = {r[ID]: r for r in read(directory / 'synthetic_profiles.csv')}
        selected = random.Random(20261011).sample(generated, 1625)
        actual = {r[ID]: r for r in reference}
        labels = []
        for index, row in enumerate(selected, 1):
            identity = f'REF-{index:08d}'
            regenerated = {**row, ID: identity}
            if actual.get(identity) != regenerated:
                raise ValueError(f'Reprodukce neodpovídá referenci: {identity}; scénář nelze obnovit.')
            labels.append({**metadata[row[ID]], ID: identity})
        if len(actual) != len(labels):
            raise ValueError('Reprodukce má jiný počet transakcí.')
    output = data_path('reference_scenarios.csv')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=PROFILE_COLUMNS, delimiter=';')
        writer.writeheader(); writer.writerows(labels)
    print(f'Obnoveno {len(labels)} scénářových kategorií po přesném ověření všech bankovních sloupců.')


if __name__ == '__main__':
    main()
