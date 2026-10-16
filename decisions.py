"""Separate append-only decision events; never edits an item or approves exam use."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


KINDS = ('user_evidence_check', 'specialist_pedagogical', 'operational')
ACTIONS = ('defer', 'request_source', 'accept_evidence', 'reject_evidence')


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode('utf-8')).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def inspect(results, item_id, record_id=None, event=None):
    results = Path(results).resolve()
    content = results.read_bytes()
    rows = [x for x in json.loads(content)['items'] if x['item_id'] == item_id
            and (record_id is None or x['record_id'] == record_id)]
    if len(rows) != 1:
        raise ValueError('Item ausente ou ambíguo; informe --record-id quando necessário.')
    row = rows[0]
    if row['processing_status'] == 'reserved':
        raise ValueError('Item reservado: este fluxo não abre nem registra sua avaliação.')
    raw_rows = [x for x in load(results.parent / 'ingestion/itens.json')
                if x['record_id'] == row['record_id']]
    if len(raw_rows) != 1 or digest(raw_rows[0]) != row['source_hash']:
        raise ValueError('Origem da execução mudou ou ficou ambígua; execute novamente a ingestão.')
    ref = dict(results_sha256=hashlib.sha256(content).hexdigest(),
               item_id=item_id, record_id=row['record_id'], item_hash=row['source_hash'],
               fingerprint=row['fingerprint'])
    answer = dict(reference=ref, processing_status=row['processing_status'],
                  reason=row['reason'], ingestion_issues=row['ingestion_issues'],
                  source=raw_rows[0]['source'], raw=raw_rows[0]['raw'],
                  standardized=raw_rows[0]['data'], analysis=row['analysis'],
                  ready_for_exam=False)
    if event:
        recorded = load(event)
        answer['event'] = recorded
        answer['event_applicability'] = ('current' if recorded.get('reference') == ref else 'stale')
        answer['event_effect'] = 'Registro separado; nenhuma pendência ou liberação é alterada automaticamente.'
    return answer


def record(results, item_id, events, actor, review_kind, decision, note,
           demo=False, record_id=None):
    if review_kind not in KINDS or decision not in ACTIONS:
        raise ValueError('Classe ou decisão inválida.')
    if not actor.strip() or not note.strip():
        raise ValueError('Ator e justificativa são obrigatórios.')
    if demo != (actor == 'agente_demo'):
        raise ValueError('Demonstração exige --demo e --actor agente_demo; use ator explícito para registro real.')
    view = inspect(results, item_id, record_id)
    events = Path(events).resolve()
    # Keep added files out of the immutable execution and the legacy source.
    runs = Path(__file__).resolve().parent / 'runs'
    if not events.is_relative_to(runs) or events == runs:
        raise ValueError('Use uma pasta de eventos dentro de runs/.')
    if events.is_relative_to(Path(results).resolve().parent):
        raise ValueError('Eventos devem ficar em pasta separada da execução.')
    if any((p / 'results.json').exists() for p in [events, *events.parents] if p != runs):
        raise ValueError('Eventos não podem ser gravados dentro de outra execução.')
    event = dict(version='decision-event-v1', event_id=uuid4().hex,
                 created_at=datetime.now(timezone.utc).isoformat(), demo=demo,
                 actor=actor, review_kind=review_kind, decision=decision, note=note,
                 reference=view['reference'], issue_snapshot=view['ingestion_issues'],
                 ready_for_exam=False, changes_legacy=False,
                 effect='decision_record_only',
                 qualification_verified=False)
    events.mkdir(parents=True, exist_ok=True)
    path = events / (event['event_id'] + '.json')
    with path.open('x', encoding='utf-8') as handle:
        json.dump(event, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    for name in ('show', 'record'):
        sub = subs.add_parser(name)
        sub.add_argument('--results', type=Path, required=True)
        sub.add_argument('--item', required=True)
        sub.add_argument('--record-id')
        if name == 'show':
            sub.add_argument('--event', type=Path)
        else:
            sub.add_argument('--events', type=Path, required=True)
            sub.add_argument('--actor', required=True)
            sub.add_argument('--review-kind', choices=KINDS, required=True)
            sub.add_argument('--decision', choices=ACTIONS, required=True)
            sub.add_argument('--note', required=True)
            sub.add_argument('--demo', action='store_true')
    a = parser.parse_args()
    try:
        if a.command == 'show':
            value = inspect(a.results, a.item, a.record_id, a.event)
        else:
            value = {'event_path': str(record(a.results, a.item, a.events, a.actor,
                     a.review_kind, a.decision, a.note, a.demo, a.record_id))}
        print(json.dumps(value, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
