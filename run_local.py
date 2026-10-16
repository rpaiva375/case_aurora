"""Local replay only. No network, credentials, inference or pedagogical approval."""
import argparse
import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
import ingest
from mapping import validate_v2

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT / 'replay_fixtures'
CONTRACT = 'aurora-replay-v1/raw-data-curriculum-prompt-validator'


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def context(matrix, ementas, manifest, prompt):
    return dict(matrix=matrix, ementas=ementas, ementas_manifest=manifest,
                prompt_sha256=hashlib.sha256(Path(prompt).read_bytes()).hexdigest(),
                validator_sha256=hashlib.sha256(Path(validate_v2.__file__).read_bytes()).hexdigest(), contract=CONTRACT)


def fingerprint(row, ctx):
    return digest(dict(item=row, context=ctx))


def validate_response(row, ctx, response):
    # v2 validates six-item batches. Six copies here adapt its unchanged contract
    # to a single response; these copies are never exported or counted as results.
    packet = dict(items=[row], matrix=ctx['matrix'], ementas=ctx['ementas'])
    if not isinstance(response, dict) or not isinstance(response.get('items'), list) or len(response['items']) != 1:
        raise ValueError('Response must be an envelope with exactly one item')
    item = response['items'][0]
    if not isinstance(item, dict):
        raise ValueError('Item response must be an object')
    for field, cls in {'subject': str, 'required_task': dict, 'object_alignment': dict,
                       'competency_alignment': dict, 'use_issues': list, 'links': list,
                       'evidence': list, 'readiness': dict, 'rejected_candidates': list}.items():
        if not isinstance(item.get(field), cls):
            raise ValueError('Invalid or missing field: ' + field)
    if not item['subject'].strip() or not isinstance(item['required_task'].get('operation'), str) or not item['required_task']['operation'].strip():
        raise ValueError('Missing subject or required task')
    for field in ('object_alignment', 'competency_alignment'):
        if any(not isinstance(item[field].get(k), str) or not item[field][k].strip() for k in ('status', 'reason')):
            raise ValueError('Missing alignment status/reason: ' + field)
    if not isinstance(item['object_alignment'].get('supported_oc_ids'), list) or not all(isinstance(x, str) for x in item['object_alignment']['supported_oc_ids']):
        raise ValueError('Invalid supported object IDs')
    if not all(isinstance(x, str) and x.strip() for x in item['use_issues']):
        raise ValueError('Invalid use issues')
    if 'scope' in item['competency_alignment'] and not isinstance(item['competency_alignment']['scope'], str):
        raise ValueError('Invalid competency scope')
    adapted = copy.deepcopy(response)
    adapted['items'] = [item] * 6
    result = validate_v2.validate(packet, adapted, verify_hashes=False)
    if not result['valid']:
        raise ValueError('; '.join(sorted(set(result['errors']))))
    return item, validate_v2.check_rules({'items': [item]})['items'][0]


def report(data):
    s = data['summary']
    lines = ['# Case Aurora — execução local de respostas gravadas', '',
             '**MOCK/REPLAY: nenhuma inferência nova, chamada de API ou validação pedagógica.**', '',
             f"Registros: {s['total']}; analisados por replay: {s['analyzed']}; pendentes sem análise: {s['pending']}; reservados: {s['reserved']}; erros técnicos: {s['error']}.",
             'Analisados incluem sugestões, objeto com competência pendente e abstenções. Essas classes não medem acurácia.',
             'Nenhum item está liberado para prova. Revisão de coerência e validação pedagógica especializada continuam pendentes.',
             'Desempenho e aplicações permanecem separados em ingestion/. Ocorrências estruturais não são somadas à quantidade de questões.', '',
             '## Questões', '']
    labels = {'analyzed': 'ANALISADO (replay)', 'pending': 'PENDENTE — sem análise', 'reserved': 'RESERVADO — sem análise', 'error': 'ERRO TÉCNICO — sem análise'}
    for r in data['items']:
        lines += [f"### {r['item_id']} — {labels[r['processing_status']]}", '',
                  f"Origem: {r['record_id']}, linhas {r['source']['line_start']}–{r['source']['line_end']}. Motivo: {r['reason']}."]
        if r['ingestion_issues']:
            lines += ['Pendências estruturais: ' + '; '.join(f"{x['code']} ({x['field']}): {json.dumps(x['detail'], ensure_ascii=False)}" for x in r['ingestion_issues'])]
        if r['error']:
            lines += ['Erro: ' + r['error']]
        x = r['analysis']
        if x:
            lines += [f"Estado semântico: {r['semantic_status']}", 'Assunto: ' + x['subject'],
                      'Tarefa exigida: ' + x['required_task']['operation'],
                      'Objeto (' + x['object_alignment']['status'] + '): ' + (', '.join(x['object_alignment']['supported_oc_ids']) or 'nenhum sustentado') + '. ' + x['object_alignment']['reason'],
                      'Competência (' + x['competency_alignment']['status'] + '): ' + x['competency_alignment']['reason'] + ' Escopo: ' + x['competency_alignment'].get('scope', 'pendente'),
                      'Vínculos: ' + (', '.join(l['oc_id'] + ' → ' + l['competency_id'] for l in x['links']) or 'nenhum'),
                      'Problemas de uso: ' + ('; '.join(x['use_issues']) or 'nenhum adicional registrado; isso não libera uso'),
                      f"Regra provisória de nós (separada): {r['rule_check']['identified_node_count']} nós identificados; {r['rule_check']['pair_count']} pares; estado {r['rule_check']['status']}. Nenhum vínculo truncado.",
                      f"Resposta bruta: [{r['raw_response_path']}]({r['raw_response_path']})", 'Evidências:']
            seen = set()
            for e in validate_v2.citations(x):
                signature = digest(e)
                if signature not in seen:
                    seen.add(signature)
                    locator = e.get('field') or e.get('pointer') or f"linhas {e.get('line_start')}–{e.get('line_end')}"
                    lines += [f"- {e['kind']}: {e.get('file', e.get('record_id'))}, {locator}: {json.dumps(e['quote'], ensure_ascii=False)}"]
        lines += ['Liberado para prova: **não**.', '']
    return '\n\n'.join(line for line in lines if line)


def run(source, output, fixtures=FIXTURES, prompt=ROOT / 'mapping/prompt_v2.md'):
    output, source, fixtures = Path(output).resolve(), Path(source).resolve(), Path(fixtures).resolve()
    if output.exists():
        raise ValueError('Use uma pasta de saída nova; execução existente não é sobrescrita.')
    if output == source or output.is_relative_to(source) or source.is_relative_to(output):
        raise ValueError('Fonte e saída devem ser árvores separadas.')
    if output == fixtures or output.is_relative_to(fixtures) or fixtures.is_relative_to(output):
        raise ValueError('Fixtures e saída devem ser árvores separadas.')
    output.mkdir(parents=True)
    try:
        ing = ingest.run(source, output / 'ingestion')
        split = load(ROOT / 'mapping/split.json')
        reserved = {x['id'] for x in split['holdout']}
        ctx = context(ing['matriz.json'], [x for x in ing['textos.json'] if x['source']['file'].startswith(('02_', '03_'))], ing['ementas_manifest.json'], prompt)
        (output / 'raw_responses').mkdir()
        (output / 'requests').mkdir()
        save(output / 'context.json', ctx)
        (output / 'prompt.md').write_bytes(Path(prompt).read_bytes())
        manifest_error = None
        try:
            manifest_bytes = (fixtures / 'manifest.json').read_bytes()
            (output / 'fixture_manifest.json').write_bytes(manifest_bytes)
            manifest = json.loads(manifest_bytes)
            if manifest.get('contract') != CONTRACT or not isinstance(manifest.get('items'), dict):
                raise ValueError('Invalid fixture manifest contract/items')
        except (OSError, ValueError, TypeError, AttributeError) as exc:
            manifest, manifest_error = {'items': {}}, str(exc)
        rows = []
        for row in ing['itens.json']:
            ident = row['data']['id']
            r = dict(item_id=ident, record_id=row['record_id'], source=row['source'], source_hash=digest(row),
                     processing_status='pending', semantic_status=None, reason='fixture_missing',
                     fingerprint=fingerprint(row, ctx), analysis=None, rule_check=None, error=None,
                     raw_response_path=None, request_path=None, ready_for_exam=False,
                     user_coherence_review='pending', specialist_pedagogical_review='pending',
                     ingestion_issues=[x for x in ing['pendencias.json'] if x['record_id'] == row['record_id']],
                     provider_mode='mock', response_origin=None, new_inference=False)
            rows.append(r)
            if ident in reserved:
                r.update(processing_status='reserved', reason='prospective_holdout_excluded')
                continue
            if row['link_status'] != 'matched':
                r.update(processing_status='error', reason='ambiguous_or_invalid_item_identity', error='Identidade não única ou inválida; replay bloqueado.')
                continue
            if manifest_error:
                r.update(processing_status='error', reason='fixture_manifest_invalid', error=manifest_error)
                continue
            entry = manifest['items'].get(ident)
            if entry is None:
                continue
            try:
                if not isinstance(entry, dict) or not isinstance(entry.get('fingerprint'), str):
                    raise ValueError('Invalid manifest entry')
                if r['fingerprint'] != entry['fingerprint']:
                    r['reason'] = 'fixture_stale'
                    continue
                r['request_path'] = f"requests/{row['source']['record']:03d}.json"
                save(output / r['request_path'], dict(item=row, context_file='../context.json', fingerprint=r['fingerprint']))
                filename = entry['response_file']
                if not isinstance(filename, str) or Path(filename).name != filename:
                    raise ValueError('Response path must be a filename inside fixture directory')
                raw = (fixtures / filename).read_bytes()
                r['raw_response_path'] = f"raw_responses/{row['source']['record']:03d}.json"
                (output / r['raw_response_path']).write_bytes(raw)
                r['raw_response_sha256'] = hashlib.sha256(raw).hexdigest()
                response = json.loads(raw)
                item, rule = validate_response(row, ctx, response)
                # Immutable recording: valid but edited answers must not masquerade as the original.
                if r['raw_response_sha256'] != entry['response_sha256']:
                    raise ValueError('Recorded response hash changed')
                r.update(processing_status='analyzed', semantic_status=item['status'], reason='recorded_response_replayed',
                         analysis=item, rule_check=rule, response_origin='session_agent_recording')
            except (OSError, ValueError, KeyError, TypeError, IndexError, AttributeError) as exc:
                r.update(processing_status='error', reason='invalid_recorded_response', error=str(exc))
        counts = Counter(r['processing_status'] for r in rows)
        data = dict(version='local-replay-v1', provider_mode='mock', new_inference=False, api_calls=0,
                    pedagogical_validation=False, operational_gain='not_measured',
                    summary=dict(total=len(rows), **{k: counts[k] for k in ('analyzed', 'pending', 'reserved', 'error')},
                                 semantic_statuses=dict(Counter(r['semantic_status'] for r in rows if r['processing_status'] == 'analyzed'))), items=rows)
        save(output / 'results.json', data)
        (output / 'report.md').write_text(report(data), encoding='utf-8')
        return data
    except Exception as exc:
        save(output / 'run_error.json', dict(status='failed_before_complete_output', error=str(exc), api_calls=0))
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--fixtures', default=str(FIXTURES), help='Local recordings directory; no generation or network')
    args = parser.parse_args()
    try:
        data = run(args.source, args.output, args.fixtures)
    except Exception as exc:
        print('ERRO: ' + str(exc), file=sys.stderr)
        return 1
    print(json.dumps(data['summary'], ensure_ascii=False))
    return 2 if data['summary']['error'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
