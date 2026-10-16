"""Independent output verification; fixtures test software only."""
import argparse, csv, io, json, hashlib, sys, re
from pathlib import Path
from collections import Counter
from decimal import Decimal
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source', type=Path, default=ROOT / 'output' / 'originals')
parser.add_argument('--report', type=Path, default=ROOT / 'review' / 'verification.json')
args = parser.parse_args()
SOURCE = args.source.resolve()
if (SOURCE / 'data_pack').is_dir():
    SOURCE /= 'data_pack'
OUT = ROOT / 'output'
started = datetime.now().astimezone().isoformat()
load = lambda n: json.loads((OUT/n).read_text('utf-8'))
hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCE.iterdir() if p.is_file()}
checks = []
def check(name, condition):
    assert condition, name
    checks.append(name)

for m in load('manifest.json'):
    check('hash '+m['file'], hashes[m['file']] == m['source_sha256_before'] == m['source_sha256_after'] == m['copy_sha256'] == hashlib.sha256((OUT/'originals'/m['file']).read_bytes()).hexdigest())
check('seven original files', len(load('manifest.json')) == 7)
audit = load('audit.json')
rules = load('rules.json')
allrows = {}
tables = {}
for source, target, sep in [('04_itens_legado.csv','itens',';'),('05_desempenho_itens.csv','desempenho',','),('07_historico_aplicacao.csv','aplicacoes',';')]:
    # Parse using csv.reader and explicit positional columns, independently of author DictReader.
    reader = csv.reader(io.StringIO((SOURCE/source).read_bytes().decode('utf-8'), newline=''), delimiter=sep)
    header = next(reader)
    source_rows = [dict(zip(header, cells, strict=True)) for cells in reader]
    rows = load(target+'.json'); tables[target] = rows
    check(target+' complete ordered raw records', source_rows == [r['raw'] for r in rows])
    for i, r in enumerate(rows,1):
        check(target+f' record {i} schema and provenance', set(r['data']) == set(header) and r['record_id'] == f'{source}:{i}' and r['source']['file'] == source and r['source']['record'] == i)
        replay = dict(r['raw'])
        for event in [e for e in audit if e['record_id'] == r['record_id']]:
            check('audit event '+r['record_id']+' '+event['field'], event['before'] == replay[event['field']] and type(event['before']) is type(replay[event['field']]) and event['rule_id'] in rules and event['source'] == r['source'])
            replay[event['field']] = event['after']
        check('replay '+r['record_id'], replay == r['data'])
        numeric = ['ano_aplicacao'] if target == 'itens' else ['n_respondentes','percentual_acerto','indice_discriminacao','tempo_medio_resposta_seg'] if target == 'desempenho' else []
        for f in numeric:
            check('numeric '+r['record_id']+' '+f, (r['raw'][f] == '' and r['data'][f] is None) or (r['raw'][f] != '' and isinstance(r['data'][f], (float,int)) and Decimal(r['raw'][f]) == Decimal(str(r['data'][f]))))
        allrows[r['record_id']] = r
check('no unknown audited records', all(e['record_id'] in allrows for e in audit))
for rows in tables.values():
    for r in rows:
        idvalue = r['data'].get('id',r['data'].get('item_id'))
        candidates = [it for it in tables['itens'] if it['data']['id'] == idvalue]
        check('association '+r['record_id'], (len(candidates)==1 and r['item_record_id']==candidates[0]['record_id'] and r['link_status']=='matched') or (not candidates and r['item_record_id'] is None and r['link_status']=='unmatched'))
check('counts', [len(v) for v in tables.values()] == [68,69,142])
check('distinct periods preserved', sorted(r['data']['semestre_referencia'] for r in tables['desempenho'] if r['data']['item_id']=='ITM-10066') == ['2024.1','2025.1'])
check('orphans preserved', sorted(r['data']['item_id'] for r in tables['desempenho'] if r['link_status']=='unmatched') == ['ITM-10039','ITM-20011'])
issues=load('pendencias.json')
for idvalue in ['ITM-10048','ITM-20021']:
    r=next(r for r in tables['itens'] if r['data']['id']==idvalue)
    check('numeric answer pending '+idvalue,r['data']['gabarito'] is None and any(p['record_id']==r['record_id'] and p['code']=='ANSWER_UNRESOLVED' for p in issues))
matrix=json.loads((SOURCE/'01_matriz_competencias.json').read_bytes())
check('matrix unchanged',load('matriz.json')['data']==matrix)
for t in load('textos.json'):
    check('text unchanged '+t['source']['file'],t['text']==(SOURCE/t['source']['file']).read_bytes().decode('utf-8'))
for ref in load('ementas_manifest.json'):
    c=next(c for c in matrix['componentes_curriculares'] if c['id']==ref['component_id'])
    check('ementa resolution '+c['id'], c['fonte_conhecimento']==ref['before'] and ref['after'] in hashes and ref['after'][3:]==ref['before'])

# Synthetic adversarial inputs kept in memory; no modification to supplied/output data.
sys.path.insert(0,str(ROOT))
import ingest
blobs={m['file']:(SOURCE/m['file']).read_bytes() for m in load('manifest.json')}
def mutate(filename, fn):
    updated=dict(blobs)
    delimiter=',' if filename.startswith('05') else ';'
    rr=list(csv.reader(io.StringIO(updated[filename].decode()),delimiter=delimiter))
    fn(rr)
    stream=io.StringIO(newline=''); csv.writer(stream,delimiter=delimiter).writerows(rr)
    updated[filename]=stream.getvalue().encode()
    return ingest.build(updated)
for value in ['', 'ITM10041']:
    result=mutate('04_itens_legado.csv',lambda rr: rr.append([value]+rr[1][1:]))
    check('fixture added row retained '+repr(value),len(result['itens.json'])==69)
    if value:
        affected=[r for table in ['itens.json','desempenho.json','aplicacoes.json'] for r in result[table] if r['data'].get('id',r['data'].get('item_id'))=='ITM-10041']
        check('fixture collision blocks every association',all(r['item_record_id'] is None and r['link_status']=='ambiguous' for r in affected))
    else:
        check('fixture empty id invalid',result['itens.json'][-1]['link_status']=='invalid' and result['itens.json'][-1]['item_record_id'] is None)
result=mutate('05_desempenho_itens.csv',lambda rr: rr.append(rr[1][:]))
check('fixture same semester duplicate retained',len(result['desempenho.json'])==70 and len(result['integrity.json']['duplicate_grain_groups']['desempenho'])==1)
check('source hashes unchanged during review',hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCE.iterdir() if p.is_file()})
report={'started':started,'finished':datetime.now().astimezone().isoformat(),'passed_assertions':len(checks),'checks':checks,'counts':{k:len(v) for k,v in tables.items()},'audit_events':len(audit),'pending_occurrences':dict(Counter(p['code'] for p in issues)),'findings':[],'scope':'Independent technical review; no pedagogical validation or operational-quality measurement.'}
args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))


