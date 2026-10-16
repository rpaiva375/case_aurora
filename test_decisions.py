import json
import tempfile
import unittest
from pathlib import Path
import decisions


ROOT = Path(__file__).resolve().parent


class DecisionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / 'runs')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.run = self.root / 'execution'
        (self.run / 'ingestion').mkdir(parents=True)
        old = ROOT / 'runs/replay_final'
        row = next(x for x in decisions.load(old / 'results.json')['items'] if x['item_id'] == 'ITM-10048')
        origin = next(x for x in decisions.load(old / 'ingestion/itens.json') if x['record_id'] == row['record_id'])
        self.results = self.run / 'results.json'
        self.raw = self.run / 'ingestion/itens.json'
        self.results.write_text(json.dumps({'items': [row]}), encoding='utf-8')
        self.raw.write_text(json.dumps([origin]), encoding='utf-8')
        self.events = self.root / 'events'

    def record(self, **kwargs):
        defaults = dict(actor='agente_demo', review_kind='operational', decision='request_source',
                        note='Confirmar convenção numérica na fonte.', demo=True)
        defaults.update(kwargs)
        return decisions.record(self.results, 'ITM-10048', self.events, **defaults)

    def test_append_only_and_inputs_unchanged(self):
        before = [p.read_bytes() for p in (self.results, self.raw)]
        first = self.record()
        event_bytes = first.read_bytes()
        second = self.record(decision='defer')
        self.assertNotEqual(first, second)
        self.assertEqual(first.read_bytes(), event_bytes)
        self.assertEqual(before, [p.read_bytes() for p in (self.results, self.raw)])
        view = decisions.inspect(self.results, 'ITM-10048', event=first)
        self.assertEqual(view['event_applicability'], 'current')
        self.assertEqual(view['raw']['gabarito'], '2')
        self.assertIsNone(view['standardized']['gabarito'])
        self.assertFalse(view['ready_for_exam'])

    def test_changed_result_invalidates_event(self):
        event = self.record()
        data = decisions.load(self.results)
        data['items'][0]['fingerprint'] = 'changed-context'
        self.results.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(decisions.inspect(self.results, 'ITM-10048', event=event)['event_applicability'], 'stale')

    def test_changed_raw_refuses_inspection_and_record(self):
        data = decisions.load(self.raw)
        data[0]['raw']['gabarito'] = 'B'
        self.raw.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaises(ValueError):
            self.record()

    def test_review_classes_never_approve_exam_or_other_classes(self):
        for kind in decisions.KINDS:
            event = decisions.load(self.record(review_kind=kind, decision='accept_evidence'))
            self.assertEqual(event['review_kind'], kind)
            self.assertFalse(event['ready_for_exam'])
            self.assertFalse(event['qualification_verified'])
            self.assertNotIn('specialist_approved', event)

    def test_demo_actor_and_flag_required_together(self):
        for args in ({'demo': False}, {'actor': 'usuario'}):
            with self.assertRaises(ValueError):
                self.record(**args)
        event = decisions.load(self.record(demo=False, actor='revisor_identificado'))
        self.assertFalse(event['demo'])

    def test_reserved_blocked(self):
        data = decisions.load(self.results)
        data['items'][0]['processing_status'] = 'reserved'
        self.results.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaises(ValueError):
            self.record()

    def test_cannot_write_inside_execution(self):
        self.events = self.run / 'ingestion/events'
        with self.assertRaises(ValueError):
            self.record()

    def test_invalid_decision_and_empty_note(self):
        for args in ({'decision': 'approve_exam'}, {'review_kind': 'automatic'}, {'note': ' '}):
            with self.assertRaises(ValueError):
                self.record(**args)


if __name__ == '__main__':
    unittest.main()
