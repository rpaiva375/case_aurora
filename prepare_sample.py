"""Freeze a small development sample and a prospective holdout. No inference."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output'
DEST = ROOT / 'mapping'
DEV = ['ITM-10041', 'ITM-20018', 'ITM-20025', 'ITM-20043', 'ITM-30007', 'ITM-30008']
HOLDOUT = ['ITM-10049', 'ITM-10060', 'ITM-10069', 'ITM-20028', 'ITM-20034', 'ITM-20037', 'ITM-20044', 'ITM-30010']
REASONS = ['cálculo financeiro contextualizado', 'interpretação de situação organizacional',
           'possível ambiguidade entre bases de poder', 'referência a contexto ausente',
           'possível conteúdo fora dos dois componentes', 'fronteira entre custos e finanças']

def load(name):
    return json.loads((OUT / name).read_text('utf-8'))

def freeze(path, value):
    content = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    if path.exists() and path.read_text('utf-8') != content:
        raise ValueError(f'Frozen file differs: {path}; create a new explicit version')
    path.write_text(content, encoding='utf-8')

def main():
    DEST.mkdir(exist_ok=True)
    items = load('itens.json')
    lookup = {r['data']['id']: r for r in items}
    assert len(lookup) == len(items) and not set(DEV) & set(HOLDOUT)
    assert set(DEV + HOLDOUT) <= set(lookup)
    def digest(record):
        return hashlib.sha256(json.dumps(record, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    split = {
        'version': 'sample-v1', 'frozen_before_semantic_mapping': True,
        'selection': 'purposive_small_varied_sample_not_representative',
        'development': [{'id': i, 'selection_reason_not_gold_label': reason, 'record_sha256': digest(lookup[i])}
                        for i, reason in zip(DEV, REASONS)],
        'holdout': [{'id': i, 'record_sha256': digest(lookup[i])} for i in HOLDOUT],
        'remaining_unassigned_ids': [r['data']['id'] for r in items if r['data']['id'] not in DEV + HOLDOUT],
        'holdout_policy': 'No semantic outputs, labels, prompt examples or tuning on holdout until prompt/rules are frozen after user review. Evaluate once; after inspection it is no longer unseen for further tuning.',
        'exposure_limit': 'Manager and earlier diagnostic agents have inspected the corpus. This is a prospective development holdout, not a retrospectively blind or statistically representative test. New mapper/reviewer receive only the six-item packet and shared curriculum.',
        'human_review': {'user_coherence_review': 'not_performed', 'specialist_pedagogical_validation': 'not_performed'},
        'source_hashes': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.glob('*.json'))}
    }
    packet = {'sample_version': 'sample-v1', 'items': [lookup[i] for i in DEV],
              'matrix': load('matriz.json'),
              'ementas': [t for t in load('textos.json') if t['source']['file'].startswith(('02_', '03_'))],
              'ementas_manifest': load('ementas_manifest.json'),
              'limits': 'Only six sample items. No performance/history/reviewer messages supplied to avoid anchoring pedagogical suggestions in proxies.'}
    freeze(DEST / 'split.json', split)
    freeze(DEST / 'sample_packet.json', packet)
    print(json.dumps({'development_count': len(DEV), 'holdout_count': len(HOLDOUT),
                      'remaining_unassigned': len(items)-len(DEV)-len(HOLDOUT), 'overlap': 0}))

if __name__ == '__main__':
    main()
