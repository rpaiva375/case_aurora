import json, tempfile, unittest, shutil, threading, http.client
from pathlib import Path
from queue_app import Queue, ROOT, handler, ThreadingHTTPServer

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=ROOT/'runs',prefix='queue_test_')
        self.base=Path(self.temp.name)
        self.q=Queue(ROOT/'runs/portabilidade/results.json',self.base/'events')
    def tearDown(self): self.temp.cleanup()
    def payload(self,item='ITM-10048'):
        return dict(item_id=item,actor='agente_demo',review_kind='operational',decision='request_source',note='Teste demonstrativo',demo=True,reference=self.q.detail(item)['reference'])
    def test_listing_usage_priority(self):
        listing=self.q.listing(); rows=listing['items']; by={x['item_id']:x for x in rows}
        self.assertEqual(len(rows),68); self.assertEqual(listing['latest_semester'],'2026.1')
        self.assertEqual(listing['summary'],dict(total=68,analyzed=6,pending=54,reserved=8,error=0))
        self.assertEqual(by['ITM-20025']['category'],'competency_pending')
        self.assertEqual(by['ITM-20018']['priority_tier'],0)
        self.assertEqual(by['ITM-10048']['last_application'],'2024.2')
        self.assertEqual(by['ITM-10066']['application_count'],2)
        self.assertEqual(sum(x['category']=='reserved' for x in rows),8)
    def test_three_paths_persist(self):
        for item in ['ITM-10048','ITM-10041','ITM-30007']:
            self.q.record(self.payload(item))
        q2=Queue(self.q.results,self.q.events)
        for item in ['ITM-10048','ITM-10041','ITM-30007']:
            detail=q2.detail(item); self.assertEqual(len(detail['history']),1); self.assertEqual(detail['history'][0]['applicability'],'current'); self.assertFalse(detail['ready_for_exam'])
    def test_stale_reference_blocked(self):
        data=self.payload(); data['reference']['item_hash']='changed'
        with self.assertRaises(ValueError): self.q.record(data)
        self.assertFalse(self.q.events.exists())
    def test_reserved_blocked(self):
        with self.assertRaises(ValueError): self.q.detail('ITM-10049')
    def test_changed_raw_blocked(self):
        target=self.base/'copy'; shutil.copytree(self.q.results.parent,target)
        path=target/'ingestion/itens.json'; rows=json.loads(path.read_text(encoding='utf8')); rows[7]['raw']['gabarito']='3'; path.write_text(json.dumps(rows),encoding='utf8')
        q=Queue(target/'results.json',self.base/'events')
        with self.assertRaises(ValueError): q.detail('ITM-10048')
    def test_duplicate_id_blocked(self):
        target=self.base/'copy'; shutil.copytree(self.q.results.parent,target)
        path=target/'results.json'; result=json.loads(path.read_text(encoding='utf8')); result['items'].append(dict(result['items'][7])); path.write_text(json.dumps(result),encoding='utf8')
        q=Queue(path,self.base/'events')
        with self.assertRaises(ValueError): q.detail('ITM-10048')
    def test_specialist_not_allowed(self):
        data=self.payload(); data['review_kind']='specialist_pedagogical'
        with self.assertRaises(ValueError): self.q.record(data)
    def test_http_origin_guard(self):
        server=ThreadingHTTPServer(('127.0.0.1',0),handler(self.q)); thread=threading.Thread(target=server.serve_forever,daemon=True); thread.start()
        try:
            conn=http.client.HTTPConnection('127.0.0.1',server.server_port)
            conn.request('POST','/api/decision',json.dumps(self.payload()),{'Origin':'http://evil.example','X-CSRF-Token':self.q.token})
            self.assertEqual(conn.getresponse().status,403); conn.close()
        finally: server.shutdown(); server.server_close(); thread.join()

if __name__=='__main__': unittest.main()
