"""Verificação estrutural/citações; não avalia correção pedagógica. Python stdlib."""
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
def resolve(value,pointer):
    if not pointer.startswith('/'): raise ValueError('pointer deve ser absoluto')
    for key in pointer[1:].split('/'):
        key=key.replace('~1','/').replace('~0','~')
        value=value[int(key)] if isinstance(value,list) else value[key]
    return value

def check_rules(items,matrix):
    ocs={o['id']:o for c in matrix['componentes_curriculares'] for o in c['objetos_conhecimento']}
    reports=[]
    for item in items:
        links=item['links']; oc={x['oc_id'] for x in links}; comp={x['competency_id'] for x in links}
        n=len(oc)+len(comp)
        reports.append({'record_id':item['record_id'],'pair_count':len(links),'unique_pair_count':len({(x['oc_id'],x['competency_id']) for x in links}),'unique_oc_count':len(oc),'unique_competency_count':len(comp),'unique_node_count':n,'quantity_status':('not_applicable' if not links else 'pass' if 1<=n<=3 else 'review_required'),'oc_permission_status':('not_applicable' if not links else 'pass' if all(x['competency_id'] in ocs.get(x['oc_id'],{}).get('competencias',[]) for x in links) else 'review_required')})
    return {'premise_status':'provisional_manager_assumption_not_pedagogical_decision','counting':'Unique OC + COMP nodes; skills excluded; min 1 max 3; abstentions not_applicable. Violations retained for review.','items':reports}

def validate(packet,suggestions):
    errors=[]
    def require(ok,msg):
        if not ok: errors.append(msg)
    items={x['record_id']:x for x in packet['items']}; matrix=packet['matrix']['data']
    comps={x['id']:x for x in matrix['competencias']}
    ocs={o['id']:o for c in matrix['componentes_curriculares'] for o in c['objetos_conhecimento']}
    ementas={x['source']['file']:x for x in packet['ementas']}
    rows=suggestions.get('items',[])
    ids=[r.get('record_id') for r in rows]
    require(len(ids)==6 and len(set(ids))==6 and set(ids)==set(items),'coverage: exactly six packet records')
    require(suggestions.get('authorship')=='session_agent_authored','authorship')
    require(suggestions.get('api_integration_executed') is False,'API provenance')
    def evidence(e,rid):
        try:
            kind=e['kind']; q=e['quote']; require(isinstance(q,str) and bool(q),'empty quote')
            if kind=='item':
                require(e['record_id']==rid,'citation references different item')
                actual=items[e['record_id']]['data'][e['field']]
                require(isinstance(actual,str) and q in actual,'item literal mismatch')
            elif kind=='matrix':
                require(e['file']==packet['matrix']['source']['file'],'matrix file')
                actual=resolve(matrix,e['pointer'])
                require(isinstance(actual,str) and q in actual,'matrix literal mismatch')
            elif kind=='ementa':
                src=ementas[e['file']]; a=e['line_start']; b=e['line_end']; lines=src['text'].splitlines(); offset=src['source']['line_start']
                require(type(a)==int and type(b)==int and offset<=a<=b<offset+len(lines),'ementa range')
                require(q=='\n'.join(lines[a-offset:b-offset+1]),'ementa literal mismatch')
            else: require(False,'unknown evidence kind')
        except (KeyError,ValueError,IndexError,TypeError) as exc: errors.append('invalid evidence: '+str(exc))
    for row in rows:
        rid=row.get('record_id'); prefix=str(rid)+': '
        if rid not in items: continue
        require(row.get('item_id')==items[rid]['data']['id'],'item ID')
        require(row.get('item_snapshot')==items[rid]['data'],prefix+'item/gabarito changed')
        require(row.get('status') in ('suggested','abstained'),prefix+'status')
        require(bool(row.get('links'))==(row.get('status')=='suggested'),prefix+'status/links mismatch')
        for name in ('reason','response_demand','scope_limit'): require(bool(row.get(name)),prefix+name)
        require(row.get('human_review')=='pending',prefix+'human review')
        require(isinstance(row.get('pending'),list),prefix+'pending')
        require(not any(k in row for k in ('quantity_status','rule_checks','pedagogical_validated','confidence')),prefix+'semantic/rule or validation conflation')
        require(bool(row.get('item_evidence')),prefix+'item evidence missing')
        for e in row.get('item_evidence',[]): evidence(e,rid)
        for group in ('links','rejected_candidates'):
            require(isinstance(row.get(group),list),prefix+group)
            for link in row.get(group,[]):
                ocid=link.get('oc_id'); cid=link.get('competency_id')
                require(ocid in ocs and cid in comps,prefix+'unknown IDs')
                if group=='rejected_candidates': require(link.get('status')=='rejected' and bool(link.get('reason')),prefix+'rejected reason/status')
                else:
                    kinds={e.get('kind') for e in link.get('evidence',[])}
                    require({'item','matrix','ementa'}<=kinds,prefix+'link missing source class')
                    skills={s['id'] for s in comps.get(cid,{}).get('habilidades',[])}
                    require(set(link.get('skill_ids',[]))<=skills,prefix+'skill IDs/parent')
                    citations=[e for e in link.get('evidence',[]) if e.get('kind')=='matrix']
                    require(any(e.get('quote')==ocs.get(ocid,{}).get('nome') for e in citations),prefix+'OC citation')
                    require(any(e.get('quote')==comps.get(cid,{}).get('descricao') for e in citations),prefix+'COMP citation')
                for e in link.get('evidence',[]): evidence(e,rid)
    return {'generated_at':datetime.now(timezone.utc).isoformat(),'status':'pass' if not errors else 'fail','errors':errors,'scope':'Structural integrity and exact citations only; no semantic/pedagogical validation; no accuracy estimate.','item_count':len(rows),'api_called':False}

if __name__=='__main__':
    packet=json.loads((ROOT/'sample_packet.json').read_text(encoding='utf-8-sig'))
    suggestions=json.loads((ROOT/'suggestions_v1.json').read_text(encoding='utf-8'))
    result=validate(packet,suggestions)
    for name,value in [('validation_v1.json',result),('rule_checks_v1.json',check_rules(suggestions['items'],packet['matrix']['data']))]:
        (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))
    raise SystemExit(bool(result['errors']))
