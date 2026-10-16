import sys, unittest, tempfile, shutil, json, threading, http.client
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import queue_app
ROOT=queue_app.ROOT
class IndependentQueueTest(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(prefix='review_queue_',dir=ROOT/'runs'); self.base=Path(self.tmp.name); source=ROOT/'runs/replay_final'
  (self.base/'run').mkdir(); shutil.copy(source/'results.json',self.base/'run/results.json'); shutil.copytree(source/'ingestion',self.base/'run/ingestion')
  self.q=queue_app.Queue(self.base/'run/results.json',self.base/'events',demo=True)
 def tearDown(self): self.tmp.cleanup()
 def payload(self,item):
  return dict(item_id=item,actor='agente_demo',review_kind='operational',decision='request_source' if item=='ITM-10048' else 'defer',note='Teste independente, sem decisão do usuário.',demo=True,reference=self.q.detail(item)['reference'])
 def test_three_paths_persist_and_do_not_approve(self):
  for item in ['ITM-10048','ITM-10041','ITM-30007']:
   self.q.record(self.payload(item))
  reopened=queue_app.Queue(self.q.results,self.q.events,demo=True)
  for item in ['ITM-10048','ITM-10041','ITM-30007']:
   view=reopened.detail(item); self.assertEqual(len(view['history']),1); self.assertEqual(view['history'][0]['applicability'],'current'); self.assertFalse(view['ready_for_exam']); self.assertTrue(view['history'][0]['demo'])
 def test_stale_after_execution_changes(self):
  old=self.payload('ITM-10041'); self.q.record(old)
  v=json.loads(self.q.results.read_text(encoding='utf8')); v['review_marker']='changed'; self.q.results.write_text(json.dumps(v),encoding='utf8')
  self.assertEqual(self.q.detail('ITM-10041')['history'][0]['applicability'],'stale')
  with self.assertRaises(ValueError):self.q.record(old)
 def test_changed_raw_rejects_detail_and_write(self):
  old=self.payload('ITM-10048'); path=self.q.results.parent/'ingestion/itens.json'; rows=json.loads(path.read_text(encoding='utf8')); rows[7]['raw']['gabarito']='A'; path.write_text(json.dumps(rows),encoding='utf8')
  with self.assertRaises(ValueError):self.q.record(old)
  row=next(x for x in self.q.listing()['items'] if x['item_id']=='ITM-10048');self.assertTrue(row['read_only']);self.assertEqual(row['category'],'error')
 def test_holdout_read_and_write_blocked(self):
  for item in ['ITM-10049','ITM-10060','ITM-10069','ITM-20028','ITM-20034','ITM-20037','ITM-20044','ITM-30010']:
   with self.assertRaises(ValueError): self.q.detail(item)
 def test_application_counts_use_matched_record_not_performance(self):
  rows=self.q.listing()['items']; applications=json.loads((self.q.results.parent/'ingestion/aplicacoes.json').read_text(encoding='utf8'))
  for row in rows:self.assertEqual(row['application_count'],sum(a['link_status']=='matched' and a['item_record_id']==row['record_id'] for a in applications))
  row=next(x for x in rows if x['item_id']=='ITM-10066');self.assertEqual(row['application_count'],2);self.assertEqual(row['last_application'],'2024.1')
 def test_ambiguous_id_blocks(self):
  v=json.loads(self.q.results.read_text(encoding='utf8'));v['items'].append(v['items'][0].copy());self.q.results.write_text(json.dumps(v),encoding='utf8')
  with self.assertRaises(ValueError):self.q.detail('ITM-10041')
 def test_bad_fields_and_specialist_blocked(self):
  for changes in [dict(note=''),dict(note='x'*6001),dict(review_kind='specialist_pedagogical'),dict(decision='approve_exam'),dict(reference={})]:
   with self.assertRaises(ValueError):self.q.record(dict(self.payload('ITM-10041'),**changes))
 def test_unmatched_application_never_affects_priority(self):
  before=self.q.listing(); path=self.q.results.parent/'ingestion/aplicacoes.json'; rows=json.loads(path.read_text(encoding='utf8')); rows.append(dict(record_id='fake',link_status='unmatched',item_record_id='04_itens_legado.csv:1',data=dict(semestre='2099.2')));path.write_text(json.dumps(rows),encoding='utf8')
  after=self.q.listing();self.assertEqual(before['latest_semester'],after['latest_semester']);self.assertEqual(before['items'],after['items'])
 def test_http_security_and_invalid_json(self):
  server=queue_app.ThreadingHTTPServer(('127.0.0.1',0),queue_app.handler(self.q));thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();host='127.0.0.1:'+str(server.server_port)
  def req(body,headers):
   conn=http.client.HTTPConnection('127.0.0.1',server.server_port,timeout=5);conn.request('POST','/api/decision',body,headers);r=conn.getresponse();code=r.status;r.read();conn.close();return code
  try:
   payload=json.dumps(self.payload('ITM-10048')); valid={'Origin':'http://'+host,'X-CSRF-Token':self.q.token,'Content-Type':'application/json'}
   self.assertEqual(req(payload,{}),403);self.assertEqual(req(payload,dict(valid,Origin='https://evil.test')),403);self.assertEqual(req(payload,dict(valid,Host='evil.test')),403);self.assertEqual(req('{',valid),400);self.assertEqual(req('[]',valid),400);self.assertEqual(req(payload,valid),201)
  finally:server.shutdown();server.server_close();thread.join()
if __name__=='__main__':unittest.main(verbosity=2)
