"""Contracts for complete, leakage-free two-level classification and resume."""
import json
import sys
import tempfile
from unittest.mock import patch
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from classify_all_llm import payload,validate
from llm_utils import load_journal
import classify_all_llm as full

DICTIONARY=[{'Kod kategorie':'K001','Kategorie':'potraviny','Kod hlavni kategorie':'G03'}]
GROUPS={'G03':'Potraviny','G99':'Neurčeno'}


class FullClassificationTests(unittest.TestCase):
    def test_metadata_cannot_enter_batch_prompt(self):
        p=payload('test','prompt',[{'Nazev protiuctu':'Lidl','Kategorie':'SECRET',
                                   'Jmeno':'SECRET','Typ profilu':'SECRET','Duvod':'SECRET','Identifikace transakce':'SECRET'}],DICTIONARY,GROUPS)
        self.assertNotIn('SECRET',p['messages'][1]['content'])
        self.assertEqual(json.loads(p['messages'][1]['content'])[0]['id'],0)

    def test_each_transaction_must_have_exactly_one_result(self):
        good={'done':True,'message':{'content':json.dumps([{'id':1,'k':'K001','g':'G03'},
                                                          {'id':0,'k':'K001','g':'G03'}])}}
        self.assertEqual(validate(good,2,DICTIONARY,GROUPS)[0]['id'],0)
        bad={'done':True,'message':{'content':json.dumps([{'id':0,'k':'K001','g':'G03'},
                                                         {'id':0,'k':'K001','g':'G03'}])}}
        with self.assertRaises(ValueError):validate(bad,2,DICTIONARY,GROUPS)

    def test_invalid_code_and_truncated_reply_are_rejected(self):
        good={'done':True,'message':{'content':json.dumps([{'id':0,'k':'K001','g':'G03'}])}}
        with self.assertRaises(ValueError):validate({**good,'done_reason':'length'},1,DICTIONARY,GROUPS)
        bad={'done':True,'message':{'content':json.dumps([{'id':0,'k':'K999','g':'G03'}])}}
        with self.assertRaises(ValueError):validate(bad,1,DICTIONARY,GROUPS)
        with self.assertRaises(ValueError):validate({'done':True,'message':None},1,DICTIONARY,GROUPS)

    def test_resume_repairs_only_incomplete_trailing_record(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'predictions.jsonl'
            path.write_bytes(b'{"Identifikace transakce":"REF-1"}\n{"Ident')
            with self.assertRaises(ValueError):load_journal(path)
            self.assertEqual(set(load_journal(path,repair=True)),{'REF-1'})
            self.assertTrue(path.read_bytes().endswith(b'\n'))
            path.write_bytes(b'broken\n{"Identifikace transakce":"REF-1"}\n')
            with self.assertRaises(ValueError):load_journal(path,repair=True)

    def test_resume_upgrades_manifest_without_repeating_model_calls(self):
        actual_reader=full.read_csv
        chat_calls=[]
        def small_reader(path):
            rows=actual_reader(path)
            return rows[:2] if path.name=='data_combined.csv' else rows
        def local_api(host,endpoint,request=None,timeout=180):
            if endpoint=='tags':return {'models':[{'name':'qwen3.5:4b','digest':'test-model'}]}
            if endpoint=='version':return {'version':'test'}
            chat_calls.append(request)
            inputs=json.loads(request['messages'][1]['content'])
            return {'done':True,'message':{'content':json.dumps([{'id':r['id'],'k':'K001','g':'G05'} for r in inputs])}}
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            output=root/'experiments/test'
            with patch.object(full,'DATA',root),patch.object(full,'read_csv',small_reader),patch.object(full,'api',local_api):
                full.main(['--output',str(output)])
                self.assertEqual(len(chat_calls),1)
                manifest=output/'run.json'
                record=json.loads(manifest.read_text())
                context={'prompt_development_ids':['REF-00000001']}
                record['evaluation_context']=context
                for key in ['format_version','input_fields','generation_limit_rule']:
                    record['configuration'].pop(key)
                record['configuration']['options']['num_predict']=80
                manifest.write_text(json.dumps(record))
                full.main(['--output',str(output)])
                self.assertEqual(len(chat_calls),1)
                updated=json.loads(manifest.read_text())
                self.assertEqual(updated['configuration']['options']['num_predict'],1280)
                self.assertEqual(updated['evaluation_context'],context)

if __name__=='__main__':unittest.main()
