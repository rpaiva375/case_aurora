"""Independent adversarial software checks; no pedagogical evaluation."""
import copy
import csv
import hashlib
import json
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import run_local as cli

def hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}

class IndependentReview(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='cli-review-', dir=ROOT / 'review')
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.source = self.base / 'source'
        shutil.copytree(ROOT / 'output/originals', self.source)
        self.fixtures = self.base / 'fixtures'
        shutil.copytree(cli.FIXTURES, self.fixtures)
        self.frozen = {name: hashes(ROOT / name) for name in ('output', 'mapping', 'replay_fixtures')}
        self.addCleanup(self.check_frozen)

    def check_frozen(self):
        for name, expected in self.frozen.items():
            self.assertEqual(expected, hashes(ROOT / name), name)

    def run_case(self, **kwargs):
        before = hashes(self.source)
        with patch.object(socket, 'socket', side_effect=AssertionError('Network prohibited')), patch.object(socket, 'create_connection', side_effect=AssertionError('Network prohibited')):
            result = cli.run(self.source, self.base / 'out', self.fixtures, **kwargs)
        self.assertEqual(before, hashes(self.source))
        self.assertTrue(all(r['ready_for_exam'] is False and r['new_inference'] is False for r in result['items']))
        self.assertEqual(len(result['items']), len({r['record_id'] for r in result['items']}))
        return result

    def item(self, result):
        return next(r for r in result['items'] if r['item_id'] == 'ITM-10041')

    def mutate_item(self, field, value=None, duplicate=False):
        path = self.source / '04_itens_legado.csv'
        with path.open(encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f, delimiter=';')
            fields, rows = reader.fieldnames, list(reader)
        row = next(r for r in rows if r['id'] == 'ITM-10041')
        if duplicate:
            rows.append(copy.deepcopy(row))
        else:
            row[field] = value if value is not None else row[field] + ' ALTERADO'
        with path.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
            writer.writeheader(); writer.writerows(rows)

    def response(self, transform, malformed=False):
        manifest = cli.load(self.fixtures / 'manifest.json')
        entry = manifest['items']['ITM-10041']
        path = self.fixtures / entry['response_file']
        if malformed:
            raw = b'{invalid JSON'
        else:
            data = cli.load(path)
            transform(data)
            raw = json.dumps(data, ensure_ascii=False).encode()
        path.write_bytes(raw)
        # Update fixture checksum so validation, not merely checksum, is exercised.
        entry['response_sha256'] = hashlib.sha256(raw).hexdigest()
        cli.save(self.fixtures / 'manifest.json', manifest)

    def assert_error(self, result):
        row = self.item(result)
        self.assertEqual('error', row['processing_status'])
        self.assertIsNone(row['analysis'])

    def test_baseline_counts_and_holdout(self):
        result = self.run_case()
        self.assertEqual({k: result['summary'][k] for k in ('total','analyzed','pending','reserved','error')}, dict(total=68, analyzed=6, pending=54, reserved=8, error=0))
        reserved = {x['id'] for x in cli.load(ROOT / 'mapping/split.json')['holdout']}
        for row in result['items']:
            if row['item_id'] in reserved:
                self.assertEqual(row['processing_status'], 'reserved')
                self.assertIsNone(row['request_path']); self.assertIsNone(row['analysis'])
        self.assertEqual(len(list((self.base/'out/requests').glob('*.json'))), 6)
        self.assertEqual(len(cli.load(self.base/'out/ingestion/desempenho.json')),69)
        self.assertEqual(len(cli.load(self.base/'out/ingestion/aplicacoes.json')),142)

    def test_changed_stem(self):
        self.mutate_item('enunciado')
        self.assertEqual(self.item(self.run_case())['reason'], 'fixture_stale')

    def test_changed_alternative(self):
        self.mutate_item('alternativa_a')
        self.assertEqual(self.item(self.run_case())['reason'], 'fixture_stale')

    def test_changed_raw_same_normalized_answer(self):
        self.mutate_item('gabarito', 'a')
        result = self.run_case()
        self.assertEqual(self.item(result)['reason'], 'fixture_stale')
        self.assertEqual(cli.load(self.base/'out/ingestion/itens.json')[0]['data']['gabarito'], 'A')

    def test_changed_curriculum(self):
        path = self.source/'02_ementa_gestao_financeira.txt'
        path.write_bytes(path.read_bytes()+b'\nCHANGE')
        self.assertEqual(self.run_case()['summary']['analyzed'],0)

    def test_changed_rubric(self):
        path = self.base/'prompt.md'
        path.write_bytes((ROOT/'mapping/prompt_v2.md').read_bytes()+b'\nCHANGE')
        self.assertEqual(self.run_case(prompt=path)['summary']['analyzed'],0)

    def test_duplicate_identity_preserved_blocked(self):
        self.mutate_item(None, duplicate=True)
        result = self.run_case()
        self.assertEqual(result['summary']['total'],69)
        affected = [r for r in result['items'] if r['item_id']=='ITM-10041']
        self.assertEqual(len(affected),2)
        self.assertTrue(all(r['processing_status']=='error' and r['analysis'] is None for r in affected))

    def test_invalid_json(self):
        self.response(None, malformed=True)
        self.assert_error(self.run_case())

    def test_invalid_schema(self):
        self.response(lambda x: x['items'][0].pop('required_task'))
        self.assert_error(self.run_case())

    def test_false_citation(self):
        self.response(lambda x: x['items'][0]['evidence'][0].update(quote='FABRICATED'))
        self.assert_error(self.run_case())

    def test_readiness_cannot_be_true(self):
        self.response(lambda x: x['items'][0]['readiness'].update(ready=True))
        self.assert_error(self.run_case())

    def test_existing_destination_refused_preserved(self):
        self.run_case()
        before = hashes(self.base/'out')
        self.mutate_item('enunciado')
        with self.assertRaisesRegex(ValueError, 'nova'):
            cli.run(self.source, self.base/'out', self.fixtures)
        self.assertEqual(before, hashes(self.base/'out'))

    def test_cli_invalid_response_exit_two(self):
        self.response(None, malformed=True)
        result = subprocess.run([sys.executable, '-B', str(ROOT/'run_local.py'),
                                 '--source', str(self.source), '--output', str(self.base/'cli-out'),
                                 '--fixtures', str(self.fixtures)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(json.loads(result.stdout)['error'], 1)
        data = cli.load(self.base/'cli-out/results.json')
        self.assertEqual(data['summary']['total'], 68)
        self.assert_error(data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
