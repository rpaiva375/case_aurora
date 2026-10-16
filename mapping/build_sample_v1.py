"""Materializa decisões semânticas redigidas pelo agente; não é classificador/API."""
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
p = json.loads((ROOT / 'sample_packet.json').read_text(encoding='utf-8-sig'))
m = p['matrix']['data']
def mc(pointer):
    v=m
    for key in pointer.strip('/').split('/'):
        v=v[int(key)] if isinstance(v,list) else v[key]
    return {'kind':'matrix','file':p['matrix']['source']['file'],'pointer':pointer,'quote':v}
def ec(n,a,b):
    e=p['ementas'][n]
    return {'kind':'ementa','file':e['source']['file'],'line_start':a,'line_end':b,'quote':'\n'.join(e['text'].splitlines()[a-1:b])}
def ic(i,field):
    return {'kind':'item','record_id':p['items'][i]['record_id'],'field':field,'quote':p['items'][i]['data'][field]}
def candidate(oc,comp,reason,evidence):
    return {'oc_id':oc,'competency_id':comp,'status':'rejected','reason':reason,'evidence':evidence}
decisions = [
 dict(status='suggested',reason='Aplicar capitalização simples para obter montante é evidência direta do aspecto de matemática financeira de COMP-03.',response_demand='Calcular 12000 × (1 + 0,02 × 7) = 13680 e selecionar A.',scope_limit='Mede resolução de um problema simples (HAB-03.1), não comparação de financiamentos, equivalência de capitais ou domínio integral de COMP-03.',pending=[],links=[dict(oc_id='OC-GF-01',competency_id='COMP-03',skill_ids=['HAB-03.1'],evidence=[ic(0,'enunciado'),ic(0,'alternativa_a'),mc('/componentes_curriculares/0/objetos_conhecimento/0/nome'),mc('/competencias/2/descricao'),mc('/competencias/2/habilidades/0/descricao'),ec(0,38,40)])],rejected_candidates=[]),
 dict(status='suggested',reason='Interpretar remuneração adequada e ausência de reconhecimento/crescimento por Herzberg exige explicar comportamento no trabalho por teoria motivacional, aspecto explícito de COMP-04/HAB-04.1.',response_demand='Distinguir fatores higiênicos de motivacionais e aplicar a distinção à situação para escolher B.',scope_limit='Interpretação localizada; não demonstra decisão de gestão, diagnóstico completo de clima ou toda COMP-04.',pending=['A alternativa B usa insatisfacao para ausência de motivadores; a ementa distingue ausência de satisfação de insatisfação por fatores higiênicos. Revisar precisão teórica e validade do gabarito, que foi preservado.'],links=[dict(oc_id='OC-CO-02',competency_id='COMP-04',skill_ids=['HAB-04.1'],evidence=[ic(1,'enunciado'),ic(1,'alternativa_b'),mc('/componentes_curriculares/1/objetos_conhecimento/1/nome'),mc('/competencias/3/descricao'),mc('/competencias/3/habilidades/0/descricao'),ec(1,69,75)])],rejected_candidates=[candidate('OC-CO-07','COMP-04','A pesquisa interna é contexto; não exige diagnóstico de cultura ou clima.',[mc('/componentes_curriculares/1/objetos_conhecimento/6/nome')])]),
 dict(status='abstained',reason='A demanda é reconhecer uma base de poder; não avaliar efeitos de estilos de liderança ou sustentar decisões. Correspondência temática com OC-CO-04 não basta para COMP-04 ou COMP-05.',response_demand='Reconhecer admiração/identificação como poder de referência (B), distinguindo conhecimento técnico (E).',scope_limit='Pode evidenciar compreensão do conceito do OC, mas a rubrica não converte automaticamente isso em par com competência ampla.',pending=['Trajetoria tecnica também evoca poder de especialista; identificação favorece B. Revisão humana deve decidir se a classificação localizada é evidência suficiente de COMP-04.'],links=[],rejected_candidates=[candidate('OC-CO-04','COMP-04','Não exige avaliar efeito da liderança nos resultados ou engajamento.',[ic(2,'enunciado'),ic(2,'alternativa_b'),ic(2,'alternativa_e'),mc('/componentes_curriculares/1/objetos_conhecimento/3/nome'),mc('/competencias/3/descricao'),mc('/competencias/3/habilidades/2/descricao'),ec(1,118,124)]),candidate('OC-CO-04','COMP-05','Não exige conduzir comunicação, negociação ou mediação.',[mc('/competencias/4/descricao')])]),
 dict(status='abstained',reason='O texto acima não está no item fornecido. Sem comportamento descrito, não é possível determinar a operação interpretativa nem justificar o vínculo.',response_demand='Pretende relacionar comportamento de gestor a uma teoria; estímulo necessário ausente.',scope_limit='O gabarito B não permite reconstruir o estímulo ou aferir competência.',pending=['Recuperar texto-base na origem antes de reapreciar.'],links=[],rejected_candidates=[candidate('OC-CO-02','COMP-04','Alternativas citam teorias, mas falta o caso para sustentar aplicação.',[ic(3,'enunciado'),ic(3,'alternativa_b'),mc('/componentes_curriculares/1/objetos_conhecimento/1/nome'),mc('/competencias/3/descricao'),ec(1,65,75)])]),
 dict(status='abstained',reason='Reconhecer requisitos legais de validade de negócio jurídico não encontra OC jurídico na matriz fornecida; não implica decisão ética de gestão.',response_demand='Selecionar a lista de requisitos legais indicada em A; não aplicar a um caso de gestão.',scope_limit='Não houve consulta jurídica externa nem validação da completude legal da alternativa. Escopo limitado às duas ementas e à matriz do packet.',pending=[],links=[],rejected_candidates=[candidate('OC-GF-08','COMP-06','Legalidade de negócio jurídico não é evidência de ética/transparência financeira.',[ic(4,'enunciado'),ic(4,'alternativa_a'),mc('/componentes_curriculares/0/objetos_conhecimento/7/nome'),mc('/competencias/5/descricao'),ec(0,18,18)])]),
 dict(status='abstained',reason='Reconhecer fórmula de ponto de equilíbrio não exige diagnosticar demonstrações/indicadores, e não há OC de custo-volume-lucro na matriz.',response_demand='Reconhecer custos fixos divididos pela margem de contribuição unitária (A), sem cálculo numérico ou diagnóstico.',scope_limit='Proximidade com finanças não transforma recordação de fórmula em diagnóstico econômico-financeiro.',pending=[],links=[],rejected_candidates=[candidate('OC-GF-04','COMP-01','Não requer interpretar demonstrações nem comparar indicadores financeiros.',[ic(5,'enunciado'),ic(5,'alternativa_a'),mc('/componentes_curriculares/0/objetos_conhecimento/3/nome'),mc('/competencias/0/descricao'),ec(0,15,16)])])
]
for item,d in zip(p['items'],decisions):
    d.update(record_id=item['record_id'],item_id=item['data']['id'],human_review='pending',item_snapshot=item['data'],item_evidence=[ic(p['items'].index(item),'enunciado')])
result={'version':'v1','authorship':'session_agent_authored','started_at':'2026-10-14T18:51:00Z','finished_at':datetime.now(timezone.utc).isoformat(),'time_note':'Início aproximado da leitura; fim registrado na materialização.','api_integration_executed':False,'sources_consulted':['mapping/sample_packet.json'],'evidence_limit':'Apenas seis itens e matriz/duas ementas incorporadas. Amostra não representativa. Sem holdout, fontes externas, métricas de acurácia, confiança calibrada ou validação humana.','items':decisions}
target=ROOT/'suggestions_v1.json'
with target.open('x',encoding='utf-8') as f: json.dump(result,f,ensure_ascii=False,indent=2)
lines=['# Amostra v1 — sugestões para revisão','',result['evidence_limit'],'','Autoria: session_agent_authored. Integração API não executada. Revisão humana pendente.','']
for d in decisions:
    lines += ['## '+d['item_id']+' — '+d['status'],'',d['item_snapshot']['enunciado'],'']
    lines += [f"- {letter.upper()}: {d['item_snapshot']['alternativa_'+letter]}" for letter in 'abcde']
    lines += ['', 'Gabarito preservado: '+d['item_snapshot']['gabarito'],'',d['response_demand'],d['reason'],d['scope_limit'],'']
    for label,group in [('Sugerido',d['links']),('Rejeitado',d['rejected_candidates'])]:
        for g in group:
            lines += [f"{label}: {g['oc_id']} → {g['competency_id']}. "+g.get('reason',''),'']
            for e in g['evidence']:
                loc=e.get('pointer') or e.get('field') or f"linhas {e['line_start']}–{e['line_end']}"
                lines += [f"- {e.get('file',e.get('record_id'))}, {loc}: «{e['quote']}»"]
            lines += ['']
    lines += ['Pendência: '+x for x in d['pending']]+['']
(ROOT/'amostra_v1.md').write_text('\n'.join(lines),encoding='utf-8')
