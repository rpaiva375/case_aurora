"""Formal checks only; artificial corruptions never enter delivered responses."""
import copy
import unittest
from pathlib import Path
import present

class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet=present.load(present.HERE/'packet.json')
        cls.raw=present.load(present.HERE/'raw_round1.json')
        cls.before=present.sha(present.HERE/'raw_round1.json')
    def tearDown(self):
        self.assertEqual(self.before,present.sha(present.HERE/'raw_round1.json'))
    def pair(self):
        answer=next(a for a in self.raw['items'] if a['status']=='suggested')
        item=next(i for i in self.packet['items'] if i['data']['id']==answer['item_id'])
        return item,copy.deepcopy(answer)
    def test_all_eight_accounted_once(self):
        expected=[x['data']['id'] for x in self.packet['items']]
        actual=[x['item_id'] for x in self.raw['items']]
        self.assertEqual(len(actual),8)
        self.assertCountEqual(expected,actual)
    def test_recorded_shapes_and_raw_references_supported(self):
        for answer in self.raw['items']:
            item=next(i for i in self.packet['items'] if i['data']['id']==answer['item_id'])
            errors,citations,rule=present.check(self.packet,item,answer)
            self.assertEqual(errors,[],answer['item_id'])
            self.assertTrue(all(c['valid'] for c in citations))
    def test_invalid_quote_detected(self):
        item,answer=self.pair()
        answer['evidence'][0]['quote']='ARTIFICIAL TEST NONEXISTENT CITATION'
        self.assertIn('Citação não localizada literalmente',present.check(self.packet,item,answer)[0])
    def test_readiness_detected(self):
        item,answer=self.pair();answer['ready_for_exam']=True
        self.assertIn('Liberação indevida',present.check(self.packet,item,answer)[0])
    def test_wrong_item_detected(self):
        item,answer=self.pair();answer['record_id']='wrong'
        self.assertIn('Identidade incorreta',present.check(self.packet,item,answer)[0])
    def test_missing_response_is_error(self):
        self.assertTrue(present.check(self.packet,self.packet['items'][0],None)[0])
    def test_malformed_schema_is_error(self):
        item,answer=self.pair();del answer['links']
        self.assertTrue(present.check(self.packet,item,answer)[0])

if __name__=='__main__': unittest.main()
