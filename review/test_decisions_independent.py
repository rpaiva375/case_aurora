import json
import unittest
from unittest.mock import patch
from pathlib import Path
import test_decisions
ROOT = test_decisions.ROOT
import decisions

class IndependentDecisionTests(unittest.TestCase):
    setUp = test_decisions.DecisionTests.setUp
    record = test_decisions.DecisionTests.record
    def test_outside_runs_and_legacy_destination_rejected(self):
        for dest in (ROOT / 'output/originals/events', ROOT.parent / 'outside_events', ROOT / 'runs'):
            self.events = dest
            with self.assertRaises(ValueError): self.record()
            if dest != ROOT / 'runs': self.assertFalse(dest.exists())

    def test_other_execution_destination_rejected(self):
        other = self.root / 'other_execution'
        other.mkdir()
        (other / 'results.json').write_text('{}', encoding='utf-8')
        self.events = other / 'notes'
        with self.assertRaises(ValueError): self.record()
        self.assertFalse(self.events.exists())

    def test_duplicate_item_requires_record_identity(self):
        data = decisions.load(self.results)
        duplicate = dict(data['items'][0], record_id='second-record')
        data['items'].append(duplicate)
        self.results.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaises(ValueError): self.record()
        event = self.record(record_id=data['items'][0]['record_id'])
        self.assertEqual(decisions.load(event)['reference']['record_id'], data['items'][0]['record_id'])

    def test_duplicate_source_identity_rejected(self):
        data = decisions.load(self.raw)
        self.raw.write_text(json.dumps(data + data), encoding='utf-8')
        with self.assertRaises(ValueError): self.record()

    def test_collision_never_overwrites_event(self):
        class Fixed: hex = 'fixed-id'
        with patch.object(decisions, 'uuid4', return_value=Fixed()):
            event = self.record()
            before = event.read_bytes()
            with self.assertRaises(FileExistsError): self.record()
            self.assertEqual(event.read_bytes(), before)

    def test_event_from_other_reference_is_stale(self):
        event = self.record()
        data = decisions.load(event)
        data['reference']['item_id'] = 'ITM-OTHER'
        event.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(decisions.inspect(self.results, 'ITM-10048', event=event)['event_applicability'], 'stale')

    def test_accept_evidence_does_not_resolve_issue(self):
        event = self.record(decision='accept_evidence')
        view = decisions.inspect(self.results, 'ITM-10048', event=event)
        self.assertIsNone(view['standardized']['gabarito'])
        self.assertTrue(view['ingestion_issues'])
        self.assertFalse(view['ready_for_exam'])
        self.assertFalse(view['event']['changes_legacy'])

if __name__ == '__main__': unittest.main()

