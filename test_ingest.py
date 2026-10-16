"""Integrity tests. Synthetic mutations below are fixtures, never quality evidence."""
import argparse
import csv
import io
import json
import tempfile
import unittest
from pathlib import Path
import ingest

SOURCE = None

class IntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.blobs = {n: (SOURCE / n).read_bytes() for n in ingest.FILES}
        cls.result = ingest.build(cls.blobs)

    def test_every_source_record_and_field_preserved(self):
        for filename, output, delimiter in [(ingest.FILES[3], 'itens.json', ';'),
                (ingest.FILES[4], 'desempenho.json', ','), (ingest.FILES[6], 'aplicacoes.json', ';')]:
            expected = list(csv.DictReader(io.StringIO(self.blobs[filename].decode('utf-8')), delimiter=delimiter))
            actual = self.result[output]
            self.assertEqual(expected, [r['raw'] for r in actual])
            for index, row in enumerate(actual, 1):
                self.assertEqual(row['source']['record'], index)
                self.assertEqual(row['source']['file'], filename)
                reconstructed = dict(row['raw'])
                for event in self.result['audit.json']:
                    if event['record_id'] == row['record_id']:
                        self.assertEqual(reconstructed[event['field']], event['before'])
                        reconstructed[event['field']] = event['after']
                self.assertEqual(reconstructed, row['data'])

    def test_real_counts_links_and_semesters(self):
        self.assertEqual([len(self.result[n]) for n in ['itens.json', 'desempenho.json', 'aplicacoes.json']], [68, 69, 142])
        perf = self.result['desempenho.json']
        self.assertEqual(sum(r['link_status'] == 'matched' for r in perf), 67)
        self.assertEqual({r['data']['item_id'] for r in perf if r['link_status'] == 'unmatched'}, {'ITM-10039', 'ITM-20011'})
        self.assertEqual({r['data']['semestre_referencia'] for r in perf if r['data']['item_id'] == 'ITM-10066'}, {'2024.1', '2025.1'})
        self.assertEqual(sum(r['link_status'] == 'matched' for r in self.result['aplicacoes.json']), 142)

    def test_answer_decisions(self):
        items = {r['data']['id']: r for r in self.result['itens.json']}
        for item, raw in [('ITM-10048', '2'), ('ITM-20021', '1')]:
            self.assertEqual(items[item]['raw']['gabarito'], raw)
            self.assertIsNone(items[item]['data']['gabarito'])
        self.assertEqual(items['ITM-10043']['data']['gabarito'], 'A')
        self.assertEqual(items['ITM-20030']['data']['gabarito'], 'B')
        self.assertIsNone(items['ITM-10068']['data']['gabarito'])

    def test_texts_matrix_and_manifest_preserved(self):
        self.assertEqual(self.result['matriz.json']['data'], json.loads(self.blobs[ingest.FILES[0]]))
        for record in self.result['textos.json']:
            self.assertEqual(record['text'], self.blobs[record['source']['file']].decode('utf-8'))
        self.assertEqual(len(self.result['ementas_manifest.json']), 2)

    def test_collision_fixture_blocks_all_ambiguous_links_without_loss(self):
        mutated = dict(self.blobs)
        text = mutated[ingest.FILES[3]].decode('utf-8')
        duplicate = text.splitlines()[1].replace('ITM-10041;', 'ITM10041;', 1)
        mutated[ingest.FILES[3]] = (text.rstrip('\n') + '\n' + duplicate + '\n').encode('utf-8')
        result = ingest.build(mutated)
        self.assertEqual(len(result['itens.json']), 69)
        for table in ['itens.json', 'desempenho.json', 'aplicacoes.json']:
            for row in result[table]:
                if row['data'].get('id', row['data'].get('item_id')) == 'ITM-10041':
                    self.assertIsNone(row['item_record_id'])
                    self.assertEqual(row['link_status'], 'ambiguous')

    def test_duplicate_semester_fixture_retained_and_flagged(self):
        mutated = dict(self.blobs)
        text = mutated[ingest.FILES[4]].decode('utf-8')
        mutated[ingest.FILES[4]] = (text.rstrip('\n') + '\n' + text.splitlines()[1] + '\n').encode('utf-8')
        result = ingest.build(mutated)
        self.assertEqual(len(result['desempenho.json']), 70)
        self.assertEqual(len(result['integrity.json']['duplicate_grain_groups']['desempenho']), 1)

    def test_hashes_and_deterministic_reexecution(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            output = Path(folder) / 'output'
            ingest.run(SOURCE, output)
            first = {str(p.relative_to(output)): p.read_bytes() for p in output.rglob('*') if p.is_file()}
            ingest.run(SOURCE, output)
            second = {str(p.relative_to(output)): p.read_bytes() for p in output.rglob('*') if p.is_file()}
            self.assertEqual(first, second)
            for name, data in self.blobs.items():
                self.assertEqual((output / 'originals' / name).read_bytes(), data)
                self.assertEqual((SOURCE / name).read_bytes(), data)
            self.assertTrue(all(json.loads((output / 'integrity.json').read_text('utf-8'))['checks'].values()))

    def test_source_overlap_rejected(self):
        with self.assertRaises(ValueError):
            ingest.run(SOURCE, SOURCE / 'output')

    def test_multiline_provenance_fixture(self):
        records = ingest.read_csv(b'id;txt\nx;"hello\nworld"\ny;ok\n', 'fixture.csv', ';')
        self.assertEqual([(r['source']['line_start'], r['source']['line_end']) for r in records], [(2, 3), (4, 4)])

    def test_missing_or_duplicate_headers_fail(self):
        for data in [b'id;id\nx;y\n', b'id;enunciado\nx;y\n']:
            with self.assertRaises(ValueError):
                ingest.read_csv(data, ingest.FILES[3], ';')

    def test_empty_and_invalid_ids_never_link_fixture(self):
        for replacement in ['', 'INVALID']:
            mutated = dict(self.blobs)
            for name in [ingest.FILES[3], ingest.FILES[4], ingest.FILES[6]]:
                mutated[name] = mutated[name].replace(b'ITM-10041', replacement.encode())
            result = ingest.build(mutated)
            affected = [r for name in ['itens.json', 'desempenho.json', 'aplicacoes.json']
                        for r in result[name] if r['raw'].get('id', r['raw'].get('item_id')) == replacement]
            self.assertTrue(affected)
            self.assertTrue(all(r['item_record_id'] is None and r['link_status'] == 'invalid' for r in affected))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True)
    args, rest = parser.parse_known_args()
    SOURCE = Path(args.source)
    if (SOURCE / 'data_pack').exists():
        SOURCE /= 'data_pack'
    unittest.main(argv=['test_ingest.py'] + rest)
