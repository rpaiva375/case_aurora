"""Synthetic failure tests; these are not pedagogical quality measurements."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import run_local as r

class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=r.ROOT, prefix=".test-replay-")
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.source=self.root/'source'
        shutil.copytree(r.ROOT/'output/originals', self.source)
        self.fixtures=self.root/'fixtures'
        shutil.copytree(r.FIXTURES,self.fixtures)
        self.output=self.root/'result'

    def run_case(self, **kw):
        return r.run(self.source,self.output,self.fixtures,**kw)

    def row(self,data,ident='ITM-10041'):
        return next(x for x in data['items'] if x['item_id']==ident)

    def alter_response(self, mutation):
        p=self.fixtures/'ITM-10041.json'
        d=r.load(p);mutation(d);r.save(p,d)

    def test_baseline_no_network_and_complete_rows(self):
        with patch('socket.socket',side_effect=AssertionError('Network forbidden')):
            d=self.run_case()
        self.assertEqual(d['summary'],dict(total=68,analyzed=6,pending=54,reserved=8,error=0,semantic_statuses=dict(suggested=2,object_supported_competency_pending=1,abstained=3)))
        self.assertEqual(len({x['record_id'] for x in d['items']}),68)
        report=(self.output/'report.md').read_text(encoding='utf8')
        self.assertIn('Case Aurora — execução local de respostas gravadas',report)
        self.assertIn('Questões',report)
        self.assertNotIn('Ã',report)
        self.assertNotIn('â€',report)
        self.assertTrue(all(x['ready_for_exam'] is False for x in d['items']))
        self.assertTrue(all(x['analysis'] is None and x['request_path'] is None for x in d['items'] if x['processing_status']=='reserved'))

    def test_raw_change_same_normalized_value_stales_only_item(self):
        p=self.source/'04_itens_legado.csv'
        value=p.read_text(encoding='utf8')
        p.write_text(value.replace(';A;Gestão Financeira',';a;Gestão Financeira',1),encoding='utf8')
        d=self.run_case()
        self.assertEqual(self.row(d)['reason'],'fixture_stale')
        self.assertEqual(d['summary']['analyzed'],5)

    def test_curriculum_change_stales_all_six(self):
        p=self.source/'02_ementa_gestao_financeira.txt'
        p.write_text(p.read_text(encoding='utf8')+'\nAlteração sintética.',encoding='utf8')
        d=self.run_case()
        self.assertEqual(d['summary']['analyzed'],0)
        self.assertEqual(sum(x['reason']=='fixture_stale' for x in d['items']),6)

    def test_prompt_change_stales_all_six(self):
        p=self.root/'prompt.md'
        p.write_bytes((r.ROOT/'mapping/prompt_v2.md').read_bytes()+b'\nchanged')
        self.assertEqual(self.run_case(prompt=p)['summary']['analyzed'],0)

    def test_invalid_json_is_error_not_abstention(self):
        (self.fixtures/'ITM-10041.json').write_text('{invalid',encoding='utf8')
        d=self.run_case();x=self.row(d)
        self.assertEqual(x['processing_status'],'error');self.assertIsNone(x['semantic_status'])
        self.assertEqual(d['summary']['analyzed'],5)
        self.assertTrue((self.output/x['raw_response_path']).exists())

    def test_invalid_structure_is_error(self):
        self.alter_response(lambda d:d['items'][0].pop('readiness'))
        self.assertEqual(self.row(self.run_case())['processing_status'],'error')

    def test_ready_true_is_error(self):
        self.alter_response(lambda d:d['items'][0]['readiness'].update(ready=True))
        self.assertEqual(self.row(self.run_case())['processing_status'],'error')

    def test_corrupted_quote_is_error(self):
        self.alter_response(lambda d:d['items'][0]['evidence'][0].update(quote='fabricated'))
        self.assertEqual(self.row(self.run_case())['processing_status'],'error')

    def test_reexecution_does_not_overwrite(self):
        self.run_case();before=(self.output/'results.json').read_bytes()
        with self.assertRaises(ValueError):self.run_case()
        self.assertEqual((self.output/'results.json').read_bytes(),before)

    def test_reserve_wins_over_fixture_presence(self):
        m=r.load(self.fixtures/'manifest.json')
        m['items']['ITM-10049']=copy.deepcopy(m['items']['ITM-10041'])
        r.save(self.fixtures/'manifest.json',m)
        self.assertEqual(self.row(self.run_case(),'ITM-10049')['processing_status'],'reserved')

if __name__=='__main__':unittest.main()
