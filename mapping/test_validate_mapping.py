import copy
import json
import unittest
from validate_mapping import ROOT,validate,check_rules

class ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet=json.loads((ROOT/'sample_packet.json').read_text(encoding='utf-8-sig'))
        cls.base=json.loads((ROOT/'suggestions_v1.json').read_text(encoding='utf-8'))
    def test_baseline(self):
        self.assertEqual(validate(self.packet,self.base)['errors'],[])
    def test_quote_pointer_line_and_ids_corruption(self):
        for field,value,index in [('quote','INVENTED',0),('pointer','/missing',2),('line_end',999,5)]:
            s=copy.deepcopy(self.base); s['items'][0]['links'][0]['evidence'][index][field]=value
            self.assertEqual(validate(self.packet,s)['status'],'fail')
        s=copy.deepcopy(self.base); s['items'][0]['links'][0]['oc_id']='UNKNOWN'
        self.assertEqual(validate(self.packet,s)['status'],'fail')
    def test_missing_record_status_and_mutation(self):
        for mode in range(3):
            s=copy.deepcopy(self.base)
            if mode==0:s['items'].pop()
            if mode==1:s['items'][0]['status']='abstained'
            if mode==2:s['items'][0]['item_snapshot']['gabarito']='E'
            self.assertEqual(validate(self.packet,s)['status'],'fail')
    def test_abstention_not_applicable(self):
        rules=check_rules(self.base['items'],self.packet['matrix']['data'])
        self.assertEqual(rules['items'][2]['quantity_status'],'not_applicable')
    def test_synthetic_over_limit_retains_links(self):
        # Synthetic fixture only: not an additional sample decision.
        fixture=[{'record_id':'SYNTHETIC_LIMIT','links':[{'oc_id':'OC-GF-01','competency_id':'COMP-03'},{'oc_id':'OC-GF-03','competency_id':'COMP-01'}]}]
        before=copy.deepcopy(fixture)
        result=check_rules(fixture,self.packet['matrix']['data'])['items'][0]
        self.assertEqual(result['unique_node_count'],4)
        self.assertEqual(result['pair_count'],2)
        self.assertEqual(result['quantity_status'],'review_required')
        self.assertEqual(fixture,before)
    def test_permission_violation_retained(self):
        fixture=[{'record_id':'SYNTHETIC_PERMISSION','links':[{'oc_id':'OC-GF-01','competency_id':'COMP-06'}]}]
        result=check_rules(fixture,self.packet['matrix']['data'])['items'][0]
        self.assertEqual(result['oc_permission_status'],'review_required')
        self.assertEqual(len(fixture[0]['links']),1)
if __name__=='__main__': unittest.main()
