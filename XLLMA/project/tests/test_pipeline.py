"""Regression checks; pipeline outputs are redirected to a temporary directory."""
import csv
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import classify_original as classifier
import generate_synthetic as generator
import build_category_dictionaries as dictionaries
import validate_data as validator
from data_paths import data_path, require_synthetic_reference


class ClassificationTests(unittest.TestCase):
    def category(self, merchant='', note='', kind='Odchozí úhrada'):
        return classifier.classify({'Nazev protiuctu': merchant, 'Typ transakce': kind,
                                    'Zprava pro prijemce': note, 'Popis pro me': ''})[0]

    def test_payment_processor_does_not_prove_restaurant(self):
        self.assertEqual(self.category('SUMUP*UNKNOWN'), 'neurčeno')

    def test_gift_requires_whole_word(self):
        self.assertEqual(self.category(note='standardní platba'), 'neurčeno')
        self.assertEqual(self.category(note='dárek'), 'dárky')

    def test_operation_overrides_merchant(self):
        self.assertEqual(self.category('alza.cz', kind='Vrácení nákupu'), 'vratka nákupu')


class PipelineTests(unittest.TestCase):
    def test_private_export_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'skutečný bankovní výpis'):
            require_synthetic_reference([{'Identifikace transakce': 'BANK-123'}])

    def test_isolated_pipeline_and_corruption_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ['data_all.csv', 'category_dictionary.csv']:
                shutil.copyfile(data_path(name), root / name)
            route = lambda name: root / name
            with patch.object(generator, 'data_path', route), patch.object(classifier, 'data_path', route), \
                 patch.object(dictionaries, 'data_path', route), patch.object(validator, 'data_path', route):
                generator.main()
                first = (root / 'data_synthetic.csv').read_bytes()
                generator.main()
                self.assertEqual(first, (root / 'data_synthetic.csv').read_bytes())
                classifier.main()
                dictionaries.main()
                validator.main()
                # Old source flag must no longer be accepted as real reference data.
                metadata_path = root / 'original_profiles.csv'
                safe_metadata = metadata_path.read_bytes()
                metadata_path.write_bytes(safe_metadata.replace(b';1;', b';0;', 1))
                with self.assertRaisesRegex(ValueError, 'Chybný zdroj metadat'):
                    validator.main()
                metadata_path.write_bytes(safe_metadata)
                with (root / 'data_synthetic.csv').open(encoding='utf-8', newline='') as handle:
                    rows = list(csv.DictReader(handle, delimiter=';'))
                self.assertEqual(len(rows), generator.TARGET)
                for row in rows:
                    for field in ['Datum zauctovani', 'Datum provedeni']:
                        day = __import__('datetime').datetime.strptime(row[field], '%d.%m.%Y').date()
                        self.assertTrue(generator.START <= day <= generator.END)
                # A duplicate saved category code must fail before files are overwritten.
                dictionary_path = root / 'category_dictionary.csv'
                with dictionary_path.open(encoding='utf-8', newline='') as handle:
                    reader = csv.DictReader(handle, delimiter=';'); header = reader.fieldnames; records = list(reader)
                records[1]['Kod kategorie'] = records[0]['Kod kategorie']
                with dictionary_path.open('w', encoding='utf-8', newline='') as handle:
                    writer = csv.DictWriter(handle, fieldnames=header, delimiter=';'); writer.writeheader(); writer.writerows(records)
                damaged = dictionary_path.read_bytes()
                with self.assertRaisesRegex(ValueError, 'Duplicitní kódy'):
                    dictionaries.main()
                self.assertEqual(damaged, dictionary_path.read_bytes())


if __name__ == '__main__':
    unittest.main()
