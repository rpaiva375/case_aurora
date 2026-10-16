import argparse, json, re, secrets
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, parse_qs
import decisions
ROOT=Path(__file__).resolve().parent

def semester(v):
    return int(v[:4])*2+int(v[-1]) if re.fullmatch(r'\d{4}\.[12]',str(v)) else 0

class Queue:
    def __init__(self,results,events,demo=False):
        self.results=Path(results).resolve(); self.events=Path(events).resolve(); self.demo=demo; self.token=secrets.token_urlsafe(32)
        runs=ROOT/'runs'
        if not self.events.is_relative_to(runs) or self.events==runs or self.events.is_relative_to(self.results.parent):
            raise ValueError('Use pasta de eventos separada dentro de runs/.')
    def rows(self): return decisions.load(self.results)['items']
    def applications(self): return [x for x in decisions.load(self.results.parent/'ingestion/aplicacoes.json') if x.get('link_status')=='matched']
    def history(self,item_id,reference=None):
        values=[]
        for path in sorted(self.events.glob('*.json')):
            v=decisions.load(path)
            if v.get('reference',{}).get('item_id')==item_id:
                v['applicability']='current' if reference and v['reference']==reference else 'stale'; values.append(v)
        return sorted(values,key=lambda x:(x.get('created_at',''),x.get('event_id','')))
    @staticmethod
    def workflow(history):
        current=[x for x in history if x['applicability']=='current']
        if not current: return 'Registro anterior desatualizado; revisar novamente' if history else 'Sem encaminhamento registrado'
        return ('Demonstração: ' if current[-1].get('demo') else '')+{'request_source':'Aguardando confirmação da origem','defer':'Aguardando revisão ou encaminhamento','accept_evidence':'Evidência conferida; revisão especializada pendente','reject_evidence':'Evidência contestada; revisão pendente'}.get(current[-1]['decision'],'Encaminhamento registrado')
    def listing(self):
        rows=self.rows(); apps=self.applications(); latest=max((x['data'].get('semestre','') for x in apps),key=semester,default=None); items=[]
        for r in rows:
            reserved=r['processing_status']=='reserved'; usage=[x for x in apps if x['item_record_id']==r['record_id']]
            last=max((x['data'].get('semestre','') for x in usage),key=semester,default=None)
            issues=len(r.get('ingestion_issues',[]))+len((r.get('analysis') or {}).get('use_issues',[]))
            sem=r.get('semantic_status')
            category='reserved' if reserved else 'error' if r['processing_status']=='error' else 'suggestion' if sem=='suggested' else 'abstention' if sem=='abstained' else 'competency_pending' if sem=='object_supported_competency_pending' else 'pending'
            error=None; history=[]
            if not reserved:
                try: history=self.history(r['item_id'],decisions.inspect(self.results,r['item_id'])['reference'])
                except (ValueError,KeyError,OSError,TypeError) as exc: error=str(exc); category='error'
            problem=bool(issues or error); tier=0 if problem and last and last==latest else 1 if problem and last else 2 if problem else 3
            if reserved: tier=4
            why='Avaliação reservada separada; conteúdo não aberto nesta fila.' if reserved else ('Há problema de origem/uso ou integridade; ' if problem else 'Sem problema de origem/uso identificado; ')+(f'{len(usage)} aplicação(ões) associada(s); última em {last}'+(' (semestre mais recente observado no pacote).' if last==latest else '.') if usage else 'sem aplicação associada no histórico fornecido.')
            items.append(dict(item_id=r['item_id'],record_id=r['record_id'],processing_status=r['processing_status'],semantic_status=r.get('semantic_status'),category=category,has_issues=problem,issue_count=issues,application_count=len(usage),last_application=last,priority_reason=why,latest_event=history[-1] if history else None,workflow_status=self.workflow(history),read_only=reserved or bool(error),error=error,priority_tier=tier,ready_for_exam=False))
        items.sort(key=lambda x:(x['priority_tier'],-semester(x['last_application']),x['item_id'],x['record_id']))
        summary=dict(total=len(items),analyzed=sum(x['processing_status']=='analyzed' and x['category']!='error' for x in items),pending=sum(x['category']=='pending' for x in items),reserved=sum(x['category']=='reserved' for x in items),error=sum(x['category']=='error' for x in items))
        return dict(items=items,summary=summary,latest_semester=latest,csrf_token=self.token,demo=self.demo,priority_policy='Problemas com aplicação no último semestre observado; outros problemas com uso; problemas sem uso; demais por uso. Ordem operacional, não pedagógica.',provenance='6 respostas gravadas em replay; 54 sem análise; 8 reservados com avaliação separada. Nenhuma nova inferência nesta fila.')
    def detail(self,item_id):
        v=decisions.inspect(self.results,item_id); history=self.history(item_id,v['reference']); listing=next(x for x in self.listing()['items'] if x['item_id']==item_id)
        v.update(item_id=item_id,history=history,workflow_status=self.workflow(history),applications=[x for x in self.applications() if x['item_record_id']==v['reference']['record_id']],priority_reason=listing['priority_reason'],category=listing['category'],demo=self.demo)
        return v
    def record(self,data):
        if not isinstance(data,dict): raise ValueError('Objeto JSON obrigatório.')
        if self.demo: data=dict(data,actor='agente_demo',demo=True)
        for field,limit in [('item_id',100),('actor',160),('note',6000)]:
            if not isinstance(data.get(field),str) or not data[field].strip() or len(data[field])>limit: raise ValueError('Campo obrigatório ou tamanho inválido: '+field)
        kind=data.get('review_kind','operational'); action=data.get('decision')
        if action not in {'operational':('defer','request_source'),'user_evidence_check':('accept_evidence','reject_evidence','defer')}.get(kind,()): raise ValueError('Encaminhamento não permitido para essa classe.')
        if type(data.get('demo',False)) is not bool: raise ValueError('demo deve ser booleano.')
        v=self.detail(data['item_id'])
        if data.get('reference')!=v['reference']: raise ValueError('A entrada mudou ou a referência está ausente; reabra a questão.')
        path=decisions.record(self.results,data['item_id'],self.events,data['actor'],kind,action,data['note'],data.get('demo',False))
        return dict(event=decisions.load(path),detail=self.detail(data['item_id']))

def handler(queue):
    class Handler(BaseHTTPRequestHandler):
        def respond(self,status,value,mime='application/json; charset=utf-8'):
            body=value if isinstance(value,bytes) else json.dumps(value,ensure_ascii=False).encode('utf8')
            self.send_response(status); self.send_header('Content-Type',mime); self.send_header('Content-Length',str(len(body))); self.send_header('Cache-Control','no-store'); self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; frame-ancestors 'none'"); self.end_headers(); self.wfile.write(body)
        def allowed(self,post=False):
            host='127.0.0.1:'+str(self.server.server_port)
            if self.headers.get('Host')!=host: return False
            origin=self.headers.get('Origin')
            if origin and origin!='http://'+host: return False
            return not post or (origin=='http://'+host and secrets.compare_digest(self.headers.get('X-CSRF-Token',''),queue.token))
        def do_GET(self):
            if not self.allowed(): return self.respond(403,{'error':'Origem local inválida.'})
            try:
                u=urlsplit(self.path)
                if u.path=='/': return self.respond(200,(ROOT/'queue_ui.html').read_bytes(),'text/html; charset=utf-8')
                if u.path=='/api/queue': return self.respond(200,queue.listing())
                if u.path=='/api/item': return self.respond(200,queue.detail(parse_qs(u.query).get('id',[''])[0]))
                return self.respond(404,{'error':'Rota inexistente.'})
            except (ValueError,KeyError,TypeError,OSError) as exc: return self.respond(400,{'error':str(exc)})
        def do_POST(self):
            if not self.allowed(True): return self.respond(403,{'error':'Origem local ou token inválido.'})
            if self.path!='/api/decision': return self.respond(404,{'error':'Rota inexistente.'})
            try:
                size=int(self.headers.get('Content-Length','0'))
                if not 0<size<=32768: raise ValueError('Corpo ausente ou grande demais.')
                return self.respond(201,queue.record(json.loads(self.rfile.read(size))))
            except (ValueError,KeyError,TypeError,OSError) as exc: return self.respond(400,{'error':str(exc)})
    return Handler

def main():
    p=argparse.ArgumentParser(description='Fila local da analista; sem inferência ou liberação para prova.')
    p.add_argument('--results',type=Path,default=ROOT/'runs/portabilidade/results.json'); p.add_argument('--events',type=Path,default=ROOT/'runs/fila_visual'); p.add_argument('--port',type=int,default=8765); p.add_argument('--demo',action='store_true'); a=p.parse_args()
    a.events.mkdir(parents=True,exist_ok=True)
    q=Queue(a.results,a.events,a.demo); q.listing(); server=ThreadingHTTPServer(('127.0.0.1',a.port),handler(q))
    print(f'Fila local: http://127.0.0.1:{server.server_port} (Ctrl+C para encerrar)',flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
if __name__=='__main__': main()
