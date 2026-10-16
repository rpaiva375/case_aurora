"""Freeze rubric/config before extracting prospective holdout; no inference."""
import hashlib
import json
import difflib
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DEST = Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(name, value):
    with (DEST/name).open('x', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')
def main():
    split = load(ROOT/'mapping/split.json')
    paths = ['evaluation/rubrica_reservados_v1.md', 'evaluation/freeze.py', 'mapping/split.json', 'output/itens.json', 'output/matriz.json', 'output/textos.json', 'output/ementas_manifest.json', 'run_local.py', 'decisions.py']
    write('freeze_manifest.json', dict(frozen_at=datetime.now(timezone.utc).isoformat(), source_hashes={n: sha(ROOT/n) for n in paths}, ids=[x['id'] for x in split['holdout']], rounds=1, retries=0, provider='session_agents', model='inherited_session_model_not_independently_identified', paid_api_authorized=False, api_client_executed=False, previous_exposure='prospective reserve; earlier diagnostic accessed corpus; not retrospectively blind', user_evidence_check='pending', specialist_pedagogical_review='pending'))
    old=(ROOT/'mapping/prompt_v2.md').read_text(encoding='utf-8')
    new=(DEST/'rubrica_reservados_v1.md').read_text(encoding='utf-8')
    with (DEST/'rubric_diff.patch').open('x',encoding='utf-8') as f:
        f.write(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='prompt_v2.md',tofile='rubrica_reservados_v1.md')))
    ids={x['id'] for x in split['holdout']}
    selected=[r for r in load(ROOT/'output/itens.json') if r['data']['id'] in ids]
    assert len(selected)==8 and len({r['data']['id'] for r in selected})==8
    write('packet.json',dict(items=selected,matrix=load(ROOT/'output/matriz.json'),ementas=[x for x in load(ROOT/'output/textos.json') if x['source']['file'].startswith(('02_','03_'))]))
    write('packet_manifest.json',dict(extracted_at=datetime.now(timezone.utc).isoformat(),packet_sha256=sha(DEST/'packet.json'),freeze_manifest_sha256=sha(DEST/'freeze_manifest.json'),count=8))
    print(json.dumps({'frozen':True,'count':8,'packet_sha256':sha(DEST/'packet.json')}))
if __name__=='__main__': main()
