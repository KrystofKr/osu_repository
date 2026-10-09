"""Contracts for label-blind taxonomy discovery and permutation-safe evaluation."""
import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import discover_categories as discovery
from classify_all_llm import build_discovered_prompt, payload
from evaluate_discovered import partition_scores, calibration_mapping
from llm_utils import ID, load_taxonomy
import classify_all_llm as classifier
from data_paths import data_path

PROPOSAL = {'groups':[{'name':'Spotřeba','description':'Výdaje na zboží a služby.'},
                       {'name':'Nejasné platby','description':'Účel nelze určit.'}],
            'categories':[{'name':'Potraviny','description':'Nákupy v supermarketu.',
                           'group':'Spotřeba','unknown':False},
                          {'name':'Neurčený účel','description':'Nedostatek údajů o účelu.',
                           'group':'Nejasné platby','unknown':True}]}


class DiscoveryTests(unittest.TestCase):
    def test_structural_errors_require_model_correction(self):
        response=lambda p:{'done':True,'message':{'content':json.dumps(p)}}
        self.assertEqual(discovery.validate_proposal(response(PROPOSAL),24,10),PROPOSAL)
        unused={**PROPOSAL,'groups':PROPOSAL['groups']+[{'name':'Prázdná','description':'Nepoužita'}]}
        cleaned=discovery.validate_proposal(response(unused),24,10)
        self.assertEqual(cleaned['groups'],PROPOSAL['groups'])
        self.assertEqual(cleaned['categories'],PROPOSAL['categories'])
        no_unknown=json.loads(json.dumps(PROPOSAL))
        no_unknown['categories'][1]['unknown']=False
        with self.assertRaisesRegex(ValueError,'unknown=true'):
            discovery.validate_proposal(response(no_unknown),24,10)

    def test_discovery_is_label_blind_and_resume_freezes_taxonomy(self):
        rows=[{ID:f'SYN-{i}','Nazev protiuctu':'Lidl','Castka':'-100,00',
               'Kategorie':'SECRET','Jmeno':'SECRET','Typ profilu':'SECRET'} for i in range(66)]
        requests=[]
        def fake_api(host,endpoint,request=None,timeout=180):
            if endpoint=='tags':return {'models':[{'name':'qwen3.5:4b','digest':'test'}]}
            if endpoint=='version':return {'version':'test'}
            requests.append(json.loads(json.dumps(request)))
            self.assertNotIn('SECRET',json.dumps(request))
            return {'done':True,'message':{'content':json.dumps(PROPOSAL)}}
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); source=root/'data_combined.csv';source.write_text('frozen source')
            output=root/'experiments/run'
            with patch.object(discovery,'DATA',root),patch.object(discovery,'data_path',lambda name:source),\
                 patch.object(discovery,'read_csv',lambda path:rows),patch.object(discovery,'api',fake_api):
                discovery.main(['--sample-size','64','--output',str(output)])
                self.assertEqual(len(requests),2)
                document,dictionary,groups=load_taxonomy(output/'taxonomy.json')
                self.assertEqual(len(document['sample_ids']),64)
                self.assertEqual(len(set(document['sample_ids'])),64)
                prompt=build_discovered_prompt(document)
                self.assertIn('Neurčený účel',prompt)
                self.assertNotIn('SECRET',json.dumps(payload('test',prompt,rows[:1],dictionary,groups)))
                discovery.main(['--sample-size','64','--output',str(output)])
                self.assertEqual(len(requests),2)
                document['categories'][0]['description']='changed'
                (output/'taxonomy.json').write_text(json.dumps(document))
                with self.assertRaisesRegex(ValueError,'Taxonomie nesouhlasí'):
                    discovery.main(['--sample-size','64','--output',str(output)])

    def test_classification_uses_only_frozen_proposed_categories_and_resumes(self):
        actual_reader=classifier.read_csv
        rows=actual_reader(data_path('data_combined.csv'))[:2]
        calls=[]
        def reader(path):
            if path.name=='data_combined.csv':return rows
            raise AssertionError('Existing category dictionaries must not be read into the model.')
        def fake_api(host,endpoint,request=None,timeout=180):
            if endpoint=='tags':return {'models':[{'name':'qwen3.5:4b','digest':'test'}]}
            if endpoint=='version':return {'version':'test'}
            calls.append(request)
            self.assertEqual(request['format']['items']['properties']['k']['enum'],['D001','D002'])
            inputs=json.loads(request['messages'][1]['content'])
            return {'done':True,'message':{'content':json.dumps([{'id':r['id'],'k':'D001','g':'H001'} for r in inputs])}}
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);output=root/'experiments/run';output.mkdir(parents=True)
            document={'format_version':1,'model':'qwen3.5:4b','digest':'test',
                      'transaction_sha256':hashlib.sha256(data_path('data_combined.csv').read_bytes()).hexdigest(),
                      'sample_ids':[rows[0][ID]],
                      'groups':[{'code':f'H{i:03}',**r} for i,r in enumerate(PROPOSAL['groups'],1)],
                      'categories':[{'code':'D001',**PROPOSAL['categories'][0],'group':'H001'},
                                    {'code':'D002',**PROPOSAL['categories'][1],'group':'H002'}]}
            path=output/'taxonomy.json';path.write_text(json.dumps(document))
            arguments=['--taxonomy',str(path),'--output',str(output)]
            with patch.object(classifier,'DATA',root),patch.object(classifier,'read_csv',reader),patch.object(classifier,'api',fake_api):
                classifier.main(arguments)
                classifier.main(arguments)
                self.assertEqual(len(calls),1)
                run=json.loads((output/'run.json').read_text())
                self.assertEqual(run['evaluation_context']['taxonomy_discovery_ids'],document['sample_ids'])
                document['categories'][0]['description']='New definition'
                path.write_text(json.dumps(document))
                with self.assertRaisesRegex(ValueError,'Nastavení nebo data se změnila'):
                    classifier.main(arguments)


class PartitionTests(unittest.TestCase):
    def test_renaming_categories_preserves_perfect_partition(self):
        result=partition_scores([('A','X'),('A','X'),('B','Y'),('B','Y')])
        for key in ['ari','homogeneity','completeness','v_measure','purity']:
            self.assertAlmostEqual(result[key],1)

    def test_split_and_merged_clusters_have_different_penalties(self):
        crossed=partition_scores([('A','X'),('A','Y'),('B','X'),('B','Y')])
        self.assertAlmostEqual(crossed['ari'],-.5)
        self.assertAlmostEqual(crossed['v_measure'],0)
        merged=partition_scores([('A','X'),('A','X'),('B','X'),('B','X')])
        self.assertAlmostEqual(merged['homogeneity'],0)
        self.assertAlmostEqual(merged['completeness'],1)
        self.assertAlmostEqual(merged['purity'],.5)
        split=partition_scores([('A','W'),('A','X'),('B','Y'),('B','Z')])
        self.assertAlmostEqual(split['homogeneity'],1)
        self.assertAlmostEqual(split['completeness'],.5)
        self.assertAlmostEqual(split['v_measure'],2/3)
        self.assertAlmostEqual(split['ari'],0)
        self.assertIsNone(partition_scores([])['ari'])

    def test_mapping_uses_only_supplied_calibration_labels(self):
        mapping=calibration_mapping([('A','X'),('A','X'),('B','X'),('B','Y'),('A','UNKNOWN')],{'UNKNOWN'})
        self.assertEqual(mapping,{'X':'A','Y':'B'})
        self.assertNotIn('UNSEEN',mapping)


if __name__=='__main__':
    unittest.main()
