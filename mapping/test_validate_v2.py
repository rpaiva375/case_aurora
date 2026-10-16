import unittest,copy,subprocess,sys
from pathlib import Path
from validate_v2 import load,validate,check_rules
class IntegrityTests(unittest.TestCase):
    def setUp(self):self.p=load("sample_packet.json");self.d=load("suggestions_v2.json")
    def test_baseline(self):self.assertTrue(validate(self.p,self.d)["valid"])
    def test_user_criterion_is_not_user_decision(self):
        self.d["decision_source"]="user_criterion_v2"
        self.assertFalse(validate(self.p,self.d)["valid"])
    def test_false_quote(self):
        self.d["items"][0]["links"][0]["evidence"][0]["quote"]="invented"
        self.assertFalse(validate(self.p,self.d)["valid"])
    def test_snapshot_mutation(self):
        self.d["items"][0]["item_snapshot"]["gabarito"]="B"
        self.assertFalse(validate(self.p,self.d)["valid"])
    def test_no_unreviewed_ready(self):
        self.d["items"][1]["readiness"]["ready"]=True
        self.assertFalse(validate(self.p,self.d)["valid"])
    def test_pending_object_not_pair(self):
        r=check_rules(self.d)["items"][2]
        self.assertEqual((r["pair_count"],r["identified_node_count"],r["status"]),(0,1,"incomplete_mapping"))
    def test_pending_cannot_claim_suggested(self):
        self.d["items"][2]["status"]="suggested"
        self.assertFalse(validate(self.p,self.d)["valid"])
    def test_rule_does_not_truncate(self):
        x=self.d["items"][0];x["links"].append(dict(oc_id="OC-GF-04",competency_id="COMP-01"))
        before=copy.deepcopy(self.d);r=check_rules(self.d)["items"][0]
        self.assertEqual(r["identified_node_count"],4);self.assertEqual(r["status"],"review_limit_exceeded");self.assertEqual(self.d,before)
    def test_wrong_pointer(self):
        self.d["items"][0]["evidence"][2]["pointer"]="/missing"
        self.assertFalse(validate(self.p,self.d)["valid"])
    def test_cli_can_recheck_without_rewriting_frozen_reports(self):
        base=Path(__file__).resolve().parent
        files=[base/name for name in ["suggestions_v2.json","validation_v2.json","rule_checks_v2.json"]]
        before=[p.read_bytes() for p in files]
        for _ in range(2):
            result=subprocess.run([sys.executable,"-B",str(base/"validate_v2.py")],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(before,[p.read_bytes() for p in files])
if __name__=="__main__":unittest.main()
