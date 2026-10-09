"""Check class-level evaluation metrics against a hand-calculated example."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from evaluate_llm import scores


class EvaluationTests(unittest.TestCase):
    def test_accuracy_and_macro_f1_use_individual_target_classes(self):
        result=scores([('A','A'),('A','A'),('A','B'),('B','B')])
        self.assertAlmostEqual(result['accuracy'],.75)
        self.assertAlmostEqual(result['macro_f1'],(.8+2/3)/2)
        self.assertEqual(scores([])['accuracy'],None)

if __name__ == '__main__':
    unittest.main()
