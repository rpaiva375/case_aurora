"""Replay three existing cases and record explicitly simulated analyst routing."""
import argparse
import hashlib
import json
from pathlib import Path
import decisions

ROOT = Path(__file__).resolve().parent
CASES = (
    ('ITM-10041', 'Sugestão', 'defer', 'Demonstração: encaminhar a sugestão parcial e suas evidências à revisão especializada; não liberar para prova.'),
    ('ITM-30007', 'Abstenção', 'defer', 'Demonstração: encaminhar ao responsável pelo componente jurídico para conferir o recorte curricular; não descartar nem aprovar o item.'),
    ('ITM-10048', 'Pendência', 'request_source', 'Demonstração: solicitar à origem confirmação da convenção do gabarito numérico; preservar 2 bruto e nulo padronizado até evidência documentada.'),
)


def hashes(paths):
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for folder in paths for p in sorted(folder.rglob('*')) if p.is_file()}


def run(results, target):
    results, target = Path(results).resolve(), Path(target).resolve()
    runs = ROOT / 'runs'
    if target == runs or not target.is_relative_to(runs):
        raise ValueError('A saída deve ser uma pasta nova dentro de runs/.')
    if target.is_relative_to(results.parent) or results.parent.is_relative_to(target):
        raise ValueError('A saída deve estar separada da execução de origem.')
    # Inspect all cases before creating any output; this performs no inference.
    views = [(case, decisions.inspect(results, case[0])) for case in CASES]
    protected = [results.parent, ROOT / 'output/originals', ROOT / 'mapping', ROOT / 'evaluation']
    before = hashes(protected)
    target.mkdir(parents=True, exist_ok=False)
    records = []
    lines = ['# Demo dos três caminhos', '',
             '**Demonstração do agente: não contém decisões do usuário nem validação pedagógica.**', '',
             'Reutiliza respostas gravadas. Não gera inferência, não envia mensagens e não faz chamadas de API.', '']
    for (item, label, action, note), view in views:
        event = decisions.record(results, item, target / 'events', 'agente_demo',
                                 'operational', action, note, demo=True)
        checked = decisions.inspect(results, item, event=event)
        assert checked['event_applicability'] == 'current'
        assert checked['ready_for_exam'] is False
        (target / (item + '.json')).write_text(json.dumps(checked, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        records.append({'item_id': item, 'pathway': label, 'processing_status': view['processing_status'],
                        'event': str(event.relative_to(target)), 'event_applicability': 'current',
                        'ready_for_exam': False, 'decision': action})
        analysis = view['analysis'] or {}
        details = [f"Estado semântico: `{analysis.get('status', 'not_analyzed')}`.", '',
                   '> ' + view['raw']['enunciado'], '']
        if analysis:
            details += ['Justificativa preservada: ' + analysis.get('competency_alignment', {}).get('reason', analysis.get('object_alignment', {}).get('reason', 'Consulte evidências.')), '']
            for link in analysis.get('links', []):
                details += [f"Vínculo sugerido: {link['oc_id']} → {link['competency_id']}; habilidades: {', '.join(link.get('skill_ids', []))}.", '']
            for ev in analysis.get('evidence', []):
                if ev.get('kind') in ('matrix', 'ementa'):
                    locator = ev.get('pointer') or f"linhas {ev.get('line_start')}–{ev.get('line_end')}"
                    details += [f"Referência: {ev.get('file')} ({locator}):", '', '> ' + ev['quote'].replace('\n', '\n> '), '']
        if item == 'ITM-10048':
            details += [f"Gabarito bruto: `{view['raw']['gabarito']}`; padronizado: `null`. Regra: `ANSWER_UNRESOLVED`. A convenção numérica precisa de confirmação na origem.", '']
        lines += [f'## {label}: {item}', '', *details, f"Estado observado: `{view['processing_status']}`. Motivo: `{view['reason']}`.", '',
                  note, '', f'Evento: [{event.name}](events/{event.name}). Evidências e origem: [{item}.json]({item}.json).', '',
                  'A pendência permanece aberta; nenhum conteúdo ou vínculo é alterado pelo evento.', '']
    after = hashes(protected)
    unchanged = before == after
    evidence = {'demo': True, 'actor': 'agente_demo', 'api_calls': 0, 'new_inference': False,
                'results': str(results.relative_to(ROOT)), 'events_count': len(records), 'cases': records,
                'protected_files': len(before), 'unchanged': unchanged, 'hashes_before': before, 'hashes_after': after,
                'pedagogical_validation': False, 'human_time_measured': False, 'substantive_issues_resolved': 0}
    (target / 'verification.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines += ['## O que foi demonstrado', '',
              f'Três encaminhamentos demonstrativos; {len(before)} arquivos protegidos comparados; preservação: {unchanged}.', '',
              'Zero pendências substantivamente resolvidas. Não medimos tempo humano, qualidade pedagógica ou economia operacional.']
    (target / 'report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    if not unchanged:
        raise ValueError('Um arquivo protegido mudou durante a demonstração; consulte verification.json.')
    return {'output': str(target), 'events': len(records), 'protected_files': len(before), 'unchanged': unchanged}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results', type=Path, default=ROOT / 'runs/portabilidade/results.json')
    p.add_argument('--output', type=Path, default=ROOT / 'runs/demo_tres_caminhos')
    a = p.parse_args()
    try:
        print(json.dumps(run(a.results, a.output), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        p.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()

