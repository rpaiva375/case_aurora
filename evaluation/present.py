"""Check and present a single saved inference. Never invokes or repairs a model."""
import hashlib
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pointer(data,path):
    for key in path.strip('/').split('/'):
        key=key.replace('~1','/').replace('~0','~')
        data=data[int(key)] if isinstance(data,list) else data[key]
    return data
def check(packet,item,answer):
    errors=[]; citations=[]
    def require(ok,msg):
        if not ok: errors.append(msg)
    if not isinstance(answer,dict): return ['Resposta ausente ou não é objeto'],[],{}
    matrix=packet['matrix']['data']
    ocs={o['id']:o for c in matrix['componentes_curriculares'] for o in c['objetos_conhecimento']}
    comps={c['id']:c for c in matrix['competencias']}
    try:
        for k in ('subject','required_task','rationale','user_check_question'):
            require(isinstance(answer.get(k),str) and bool(answer[k].strip()),'Campo textual inválido: '+k)
        action=answer.get('analyst_next_action')
        require((isinstance(action,str) and bool(action.strip())) or (isinstance(action,dict) and bool(action) and all(isinstance(v,str) and bool(v.strip()) for v in action.values())),'Encaminhamento inválido')
        for k in ('supported_oc_ids','links','evidence','use_issues'):
            require(isinstance(answer.get(k),list),'Lista inválida: '+k)
        require(answer['item_id']==item['data']['id'] and answer['record_id']==item['record_id'],'Identidade incorreta')
        require(answer['ready_for_exam'] is False,'Liberação indevida')
        require(answer['user_evidence_check']=='pending' and answer['specialist_pedagogical_review']=='pending','Revisão humana atribuída')
        state=answer['status']; supported=answer['supported_oc_ids']; links=answer['links']
        require(state in ('suggested','object_supported_competency_pending','abstained','error'),'Estado inválido')
        require(all(x in ocs for x in supported),'Objeto desconhecido')
        require((state=='suggested')==bool(links),'Estado e vínculos incompatíveis')
        if state=='object_supported_competency_pending': require(bool(supported) and not links,'Objeto pendente inválido')
        if state in ('abstained','error'): require(not links and not supported,'Abstenção/erro com vínculo ou objeto')
        if state!='suggested': require(bool(answer.get('abstention_or_pending_reason')),'Falta motivo de pendência/abstenção/erro')
        for link in links:
            oc,comp=link['oc_id'],link['competency_id']
            require(oc in supported and comp in ocs.get(oc,{}).get('competencias',[]),'Par curricular incompatível')
            require(bool(link['scope']),'Falta escopo parcial')
            require(all(h in {x['id'] for x in comps.get(comp,{}).get('habilidades',[])} for h in link['skill_ids']),'Habilidade desconhecida')
        for e in answer['evidence']:
            ok=False
            try:
                kind=e['kind']
                if kind=='item':
                    require(e['record_id']==item['record_id'],'Citação de outro item')
                    field=e['field']
                    if field.startswith(('raw.','data.')):
                        section,key=field.split('.',1); actual=item[section][key]
                    else: actual=item['data'][field]
                elif kind=='matrix':
                    require(e['file']==packet['matrix']['source']['file'],'Arquivo matriz incorreto')
                    actual=pointer(matrix,e['pointer'])
                elif kind=='ementa':
                    src=next(x for x in packet['ementas'] if x['source']['file']==e['file'])
                    a,b=e['line_start'],e['line_end']; lines=src['text'].splitlines()
                    require(1<=a<=b<=len(lines),'Intervalo de linhas inválido')
                    actual='\n'.join(lines[a-1:b])
                else: raise ValueError('kind')
                ok=isinstance(e['quote'],str) and bool(e['quote'].strip()) and isinstance(actual,str) and e['quote'] in actual
            except (KeyError,TypeError,ValueError,IndexError,StopIteration): pass
            require(ok,'Citação não localizada literalmente')
            citations.append({'valid':ok,'evidence':e})
        if supported: require({e['kind'] for e in answer['evidence']}>={'item','matrix','ementa'},'Classes de evidência insuficientes')
        pairs={(x['oc_id'],x['competency_id']) for x in links}
        orphan=set(supported)-{o for o,c in pairs}; nodes={n for p in pairs for n in p}|orphan
        status='incomplete_mapping' if orphan else ('not_applicable' if not nodes else ('review_limit_exceeded' if len(nodes)>3 else 'within_provisional_limit'))
        rule=dict(identified_nodes=sorted(nodes),count=len(nodes),pair_count=len(pairs),objects_without_pair=sorted(orphan),status=status,limit_exceeded=len(nodes)>3,truncated=False)
    except (KeyError,TypeError,ValueError,IndexError) as exc:
        errors.append('Estrutura inválida: '+str(exc)); rule={}
    return errors,citations,rule
def main():
    packet=load(HERE/'packet.json'); freeze=load(HERE/'freeze_manifest.json'); pm=load(HERE/'packet_manifest.json')
    integrity={k:sha(ROOT/k)==v for k,v in freeze['source_hashes'].items()}
    integrity['packet']=sha(HERE/'packet.json')==pm['packet_sha256']
    integrity['freeze_manifest']=sha(HERE/'freeze_manifest.json')==pm['freeze_manifest_sha256']
    raw_error=None
    try:
        raw=load(HERE/'raw_round1.json')
        answers=raw['items']
        assert isinstance(answers,list)
        assert raw['authorship']=='session_agent_new_inference' and raw['api_client_executed'] is False
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as exc:
        raw_error=str(exc) or 'Envelope inválido'; answers=[]
    rows=[]; lines=['# Oito reservados — caderno de conferência das evidências','',
        'Uma rodada de inferência nova por agente da sessão; sem cliente de API, sem replay e sem segunda tentativa. Nenhum item está liberado para prova.',
        'Sua conferência das evidências continua pendente e não é validação pedagógica. A revisão independente do registro de decisões continua incompleta.',
        'Depois desta abertura, os oito deixam de ser inéditos para ajustes futuros. A reserva era prospectiva, não retrospectivamente cega.','']
    ids={x['data']['id'] for x in packet['items']}
    extra=[a.get('item_id') for a in answers if isinstance(a,dict) and a.get('item_id') not in ids]
    for item in packet['items']:
        ident=item['data']['id']; found=[a for a in answers if isinstance(a,dict) and a.get('item_id')==ident]
        answer=found[0] if len(found)==1 else None
        errors,citations,rule=check(packet,item,answer)
        if raw_error: errors.append(raw_error)
        if not all(integrity.values()): errors.append('Entrada congelada alterada')
        if len(found)>1: errors.append('Respostas duplicadas')
        if extra: errors.append('Resposta contém IDs não autorizados')
        status='error' if errors else answer['status']
        rows.append(dict(item_id=ident,status=status,declared_status=answer.get('status') if answer else None,errors=errors,citations=citations,rule_check=rule,answer=answer,ready_for_exam=False,user_evidence_check='pending',specialist_pedagogical_review='pending'))
        lines += ['## '+ident,'', '**Estado técnico/semântico:** '+status+'. Conferência do usuário: pendente.','',
                  '**Questão:** '+str(item['data']['enunciado']),'']
        for key,value in item['data'].items():
            if key.startswith('alternativa_'): lines += [key[-1].upper()+') '+(str(value) if value is not None else '[ausente]'),'']
        lines += ['Gabarito informado na origem: '+str(item['raw'].get('gabarito'))+' — não validado nesta rodada.','',
                  'Origem: '+item['record_id']+', linha física '+str(item['source']['line_start'])+'.','']
        if errors: lines += ['**Erros preservados, sem nova tentativa:** '+'; '.join(errors),'']
        if answer:
            for label,key in [('Assunto','subject'),('Tarefa exigida','required_task'),('Justificativa do agente','rationale'),('Pendência ou motivo de abstenção','abstention_or_pending_reason'),('Encaminhamento sugerido para a analista','analyst_next_action'),('Pergunta para sua conferência','user_check_question')]:
                value=answer.get(key)
                if isinstance(value,dict):
                    names={'evidence_check':'Conferir evidências','information_request':'Confirmar informação','specialist_review':'Encaminhar ao especialista'}
                    lines += ['**'+label+':**','']
                    lines += ['- '+names.get(k,k)+': '+str(v) for k,v in value.items()]
                    lines += ['']
                else: lines += ['**'+label+':** '+(str(value) if value is not None else 'Nenhuma adicional declarada.'),'']
            lines += ['**Objetos sustentados:** '+', '.join(answer.get('supported_oc_ids',[])),'','**Vínculos sugeridos:**','']
            for link in answer.get('links',[]): lines += ['- '+link['oc_id']+' → '+link['competency_id']+'; '+', '.join(link['skill_ids'])+'. Escopo: '+link['scope']]
            if not answer.get('links'): lines += ['Nenhum par sugerido.']
            lines += ['','**Problemas de uso apontados pelo agente:**','']
            for issue in answer.get('use_issues',[]): lines += ['- '+(issue if isinstance(issue,str) else json.dumps(issue,ensure_ascii=False))]
            if not answer.get('use_issues'): lines += ['Nenhum adicional apontado; isso não libera aplicação.']
            lines += ['','**Trechos e referências usados:**','']
            for c in citations:
                e=c['evidence']; locator=e.get('field') or e.get('pointer') or 'linhas '+str(e.get('line_start'))+'–'+str(e.get('line_end'))
                lines += ['- '+str(e.get('file',e.get('record_id')))+' — '+locator+(' [literal conferido]' if c['valid'] else ' [NÃO CONFERIDO]'),'', '> '+str(e.get('quote','')).replace('\n','\n> '),'']
            lines += ['**Regra provisória separada:** '+str(rule.get('count'))+' nós; '+str(rule.get('status'))+'. Nenhum vínculo cortado.','']
        lines += ['**Seu registro (ainda não preenchido):** evidências coerentes / contestadas / inconclusivas; justificativa; próximo encaminhamento; minutos ativos.','',
                  '**Revisão pedagógica especializada:** pendente. **Liberado para prova:** não.','']
    summary=dict(total=len(rows),statuses=dict(Counter(x['status'] for x in rows)),citations_presented=sum(len(x['citations']) for x in rows),citations_literal_valid=sum(c['valid'] for x in rows for c in x['citations']),user_reviews_completed=0,specialist_reviews_completed=0,api_calls=0)
    result=dict(summary=summary,frozen_integrity=integrity,raw_sha256=sha(HERE/'raw_round1.json') if (HERE/'raw_round1.json').exists() else None,items=rows,limits='Formal checks only; no pedagogical accuracy or operational savings measured')
    for name,content in [('verification_v2.json',json.dumps(result,ensure_ascii=False,indent=2)+'\n'),('CONFERENCIA_v2.md','\n'.join(lines))]:
        with (HERE/name).open('x',encoding='utf-8') as f:f.write(content)
    print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__':main()
