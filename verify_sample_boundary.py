"""Check frozen packet, split and untouched ingestion outputs, without evaluating holdout."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MAPPING=ROOT/'mapping'
def load(path): return json.loads(path.read_text('utf-8'))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def digest(row): return hashlib.sha256(json.dumps(row,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def main():
    split=load(MAPPING/'split.json')
    packet=load(MAPPING/'sample_packet.json')
    suggestions=load(MAPPING/'suggestions_v1.json')
    items=load(ROOT/'output'/'itens.json')
    lookup={r['data']['id']:r for r in items}
    dev=[r['id'] for r in split['development']]
    reserve=[r['id'] for r in split['holdout']]
    rest=split['remaining_unassigned_ids']
    checks={
        'partition_6_8_54': [len(dev),len(reserve),len(rest)]==[6,8,54],
        'no_overlap_or_omission': len(set(dev+reserve+rest))==68 and set(dev+reserve+rest)==set(lookup),
        'packet_is_exact_development_slice': packet['items']==[lookup[i] for i in dev],
        'frozen_record_hashes_match': all(digest(lookup[r['id']])==r['record_sha256'] for r in split['development']+split['holdout']),
        'ingestion_outputs_unchanged': all(sha(ROOT/'output'/f)==value for f,value in split['source_hashes'].items()),
        'semantic_outputs_only_development_ids': len(suggestions['items'])==6 and {r['item_id'] for r in suggestions['items']}==set(dev),
        'shared_matrix_exact': packet['matrix']==load(ROOT/'output'/'matriz.json'),
        'shared_ementas_exact': packet['ementas']==[t for t in load(ROOT/'output'/'textos.json') if t['source']['file'].startswith(('02_','03_'))],
    }
    report={'status':'pass' if all(checks.values()) else 'fail','checks':checks,
            'scope':'Technical partition/content checks only. Holdout records hashed, not semantically evaluated. No proof of access-control isolation or pedagogical quality.',
            'split_sha256':sha(MAPPING/'split.json'),'packet_sha256':sha(MAPPING/'sample_packet.json'),
            'suggestions_v1_sha256':sha(MAPPING/'suggestions_v1.json')}
    (MAPPING/'boundary_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))
    raise SystemExit(not all(checks.values()))

if __name__=='__main__': main()
