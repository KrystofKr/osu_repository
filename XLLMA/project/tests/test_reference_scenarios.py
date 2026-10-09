"""Generator scenario labels must exactly reproduce the synthetic reference."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import recover_reference_scenarios as recovery
from data_paths import data_path


class ScenarioRecoveryTests(unittest.TestCase):
    def test_labels_require_exact_transaction_reproduction(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            source=root/'data_all.csv'
            source.write_bytes(data_path('data_all.csv').read_bytes())
            with patch.object(recovery,'data_path',lambda name:root/name):
                recovery.main()
                target=root/'reference_scenarios.csv'
                original_target=target.read_bytes()
                with source.open(encoding='utf-8',newline='') as handle:
                    reader=csv.DictReader(handle,delimiter=';');fields=reader.fieldnames;rows=list(reader)
                rows[0]['Nazev protiuctu']='Changed transaction'
                with source.open('w',encoding='utf-8',newline='') as handle:
                    writer=csv.DictWriter(handle,fieldnames=fields,delimiter=';');writer.writeheader();writer.writerows(rows)
                with self.assertRaisesRegex(ValueError,'Reprodukce neodpovídá'):
                    recovery.main()
                self.assertEqual(original_target,target.read_bytes())


if __name__ == '__main__':
    unittest.main()
