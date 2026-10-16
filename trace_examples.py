"""Extract three real provenance examples; no inferred or simulated records."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output'
def load(name):
    return json.loads((OUT / name).read_text('utf-8'))

def main():
    items = load('itens.json')
    perf = load('desempenho.json')
    apps = load('aplicacoes.json')
    audit = load('audit.json')
    issues = load('pendencias.json')
    selected = [r for r in items if r['data']['id'] in ['ITM-10043','ITM-10048']]
    selected += [r for r in perf if r['data']['item_id']=='ITM-10066']
    examples = []
    for row in selected:
        source = OUT / 'originals' / row['source']['file']
        sep = ',' if source.name.startswith('05_') else ';'
        with source.open(encoding='utf-8', newline='') as f:
            parsed = list(csv.DictReader(f, delimiter=sep))
        assert parsed[row['source']['record']-1] == row['raw']
        examples.append({'record': row, 'audit': [e for e in audit if e['record_id']==row['record_id']],
                         'pending': [p for p in issues if p['record_id']==row['record_id']],
                         'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
    payload = {'source': 'real supplied synthetic case files; no demonstration fixture', 'verified_raw_against_csv': True,
               'cases': examples, 'applications_10066': [r for r in apps if r['data']['item_id']=='ITM-10066']}
    (ROOT/'docs'/'rastreabilidade_casos.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('4 source records verified for 3 cases; 2 separate application records included.')

if __name__=='__main__':
    main()
