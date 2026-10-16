"""Aurora stage 1. Standard library only; no semantic or pedagogical decisions."""
import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

FILES = ['01_matriz_competencias.json', '02_ementa_gestao_financeira.txt',
         '03_ementa_comportamento_organizacional.txt', '04_itens_legado.csv',
         '05_desempenho_itens.csv', '06_fila_revisao.txt', '07_historico_aplicacao.csv']
RULES = {
 'ID_HYPHEN': 'Inserir hífen apenas em ITM seguido de dígitos; vínculo só com destino único.',
 'EMPTY_NULL': 'Campo vazio convertido a null; conteúdo bruto preservado.',
 'ANSWER_CASE': 'Letra isolada a-e convertida para maiúscula.',
 'ANSWER_LABEL': 'Remover prefixo literal Alternativa de letra A-E.',
 'ANSWER_UNRESOLVED': 'Formato não inequívoco, inclusive número: canônico null, pendência.',
 'INTEGER': 'Converter inteiro decimal válido para número.',
 'DECIMAL': 'Converter decimal válido para número sem mudar escala.',
 'NUMBER_INVALID': 'Número inválido: canônico null, pendência.',
 'EMENTA_MANIFEST': 'Resolver nome da matriz pelo manifesto explícito, sem alterar matriz original.'}
EMENTAS = {'ementa_gestao_financeira.txt': FILES[1],
           'ementa_comportamento_organizacional.txt': FILES[2]}
HEADERS = {
    FILES[3]: 'id enunciado alternativa_a alternativa_b alternativa_c alternativa_d alternativa_e gabarito disciplina_informada ano_aplicacao origem_banco'.split(),
    FILES[4]: 'item_id semestre_referencia n_respondentes percentual_acerto indice_discriminacao tempo_medio_resposta_seg'.split(),
    FILES[6]: 'item_id prova_id curso semestre modalidade'.split()}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canonical_id(value):
    return re.sub(r'^ITM(\d+)$', r'ITM-\1', value)

def read_csv(data, filename, delimiter):
    reader = csv.DictReader(io.StringIO(data.decode('utf-8'), newline=''), delimiter=delimiter)
    if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
        raise ValueError(f'Cabeçalho inválido: {filename}')
    if filename in HEADERS and set(reader.fieldnames) != set(HEADERS[filename]):
        raise ValueError(f'Colunas inesperadas ou ausentes: {filename}')
    records = []
    previous = reader.line_num
    for n, raw in enumerate(reader, 1):
        if None in raw or any(v is None for v in raw.values()):
            raise ValueError(f'Colunas inválidas: {filename}, registro {n}')
        records.append({'record_id': f'{filename}:{n}', 'source': {
            'file': filename, 'record': n, 'line_start': previous + 1,
            'line_end': reader.line_num}, 'raw': raw, 'data': dict(raw)})
        previous = reader.line_num
    return records

def build(blobs):
    audit, issues = [], []
    def change(row, field, value, rule):
        before = row['data'][field]
        if before != value or type(before) is not type(value):
            row['data'][field] = value
            audit.append({'record_id': row['record_id'], 'source': row['source'],
                          'field': field, 'before': before, 'after': value,
                          'rule_id': rule, 'reason': RULES[rule]})
    def issue(row, code, field, detail):
        issues.append({'record_id': row['record_id'], 'source': row['source'],
                       'code': code, 'field': field, 'detail': detail,
                       'status': 'open', 'pedagogical_validation': False})
    items = read_csv(blobs[FILES[3]], FILES[3], ';')
    performance = read_csv(blobs[FILES[4]], FILES[4], ',')
    applications = read_csv(blobs[FILES[6]], FILES[6], ';')
    tables = {'itens': items, 'desempenho': performance, 'aplicacoes': applications}
    index = defaultdict(list)
    for row in items:
        candidate = canonical_id(row['raw']['id'])
        if re.fullmatch(r'ITM-\d+', candidate):
            index[candidate].append(row['record_id'])
    for table, rows in tables.items():
        id_field = 'id' if table == 'itens' else 'item_id'
        for row in rows:
            candidate = canonical_id(row['raw'][id_field])
            change(row, id_field, candidate, 'ID_HYPHEN')
            targets = index.get(candidate, [])
            row['item_record_id'] = targets[0] if len(targets) == 1 else None
            valid_id = bool(re.fullmatch(r'ITM-\d+', candidate))
            row['link_status'] = ('invalid' if not valid_id else
                                  ('matched' if len(targets) == 1 else ('ambiguous' if targets else 'unmatched')))
            if not valid_id:
                issue(row, 'INVALID_ID', id_field, {'raw': row['raw'][id_field], 'candidate': candidate})
            elif len(targets) != 1:
                issue(row, 'ID_COLLISION' if targets else 'ORPHAN', id_field,
                      {'candidate': candidate, 'target_records': targets})
            for field, value in list(row['data'].items()):
                if value == '':
                    change(row, field, None, 'EMPTY_NULL')
                    issue(row, 'MISSING_FIELD', field, 'Campo vazio na fonte; não imputado.')
            if table == 'itens':
                value = row['data']['gabarito']
                if value is not None:
                    if re.fullmatch('[A-Ea-e]', value):
                        change(row, 'gabarito', value.upper(), 'ANSWER_CASE')
                    elif re.fullmatch(r'Alternativa [A-E]', value):
                        change(row, 'gabarito', value[-1], 'ANSWER_LABEL')
                    else:
                        change(row, 'gabarito', None, 'ANSWER_UNRESOLVED')
                        issue(row, 'ANSWER_UNRESOLVED', 'gabarito', {'raw': value, 'decision': 'Confirmar convenção na origem.'})
                alternatives = {k: v for k, v in row['data'].items() if k.startswith('alternativa_') and v is not None}
                duplicates = [sorted(k for k, v in alternatives.items() if v == text)
                              for text, count in Counter(alternatives.values()).items() if count > 1]
                if duplicates:
                    issue(row, 'DUPLICATE_ALTERNATIVES', 'alternativas', duplicates)
                key = row['data']['gabarito']
                if key and row['data'].get('alternativa_' + key.lower()) is None:
                    issue(row, 'ANSWER_POINTS_TO_EMPTY', 'gabarito', key)
            number_fields = {'ano_aplicacao': int} if table == 'itens' else (
                {'n_respondentes': int, 'percentual_acerto': float, 'indice_discriminacao': float,
                 'tempo_medio_resposta_seg': float} if table == 'desempenho' else {})
            for field, converter in number_fields.items():
                value = row['data'][field]
                if value is None:
                    continue
                try:
                    pattern = r'-?\d+' if converter is int else r'-?\d+(?:\.\d+)?'
                    if not re.fullmatch(pattern, value):
                        raise ValueError(value)
                    change(row, field, converter(value), 'INTEGER' if converter is int else 'DECIMAL')
                except ValueError:
                    change(row, field, None, 'NUMBER_INVALID')
                    issue(row, 'NUMBER_INVALID', field, value)
    # Detect possible duplicate grain without deleting or inventing an observation key.
    grain = {'itens': ['id'], 'desempenho': ['item_id', 'semestre_referencia'],
             'aplicacoes': ['item_id', 'prova_id', 'semestre']}
    duplicate_groups = {}
    for table, rows in tables.items():
        groups = defaultdict(list)
        for row in rows:
            groups[tuple(row['data'][k] for k in grain[table])].append(row)
        duplicate_groups[table] = []
        for key, members in groups.items():
            if len(members) > 1:
                ids = [r['record_id'] for r in members]
                duplicate_groups[table].append({'key': list(key), 'records': ids})
                for row in members:
                    issue(row, 'DUPLICATE_GRAIN', grain[table], ids)
    matrix = json.loads(blobs[FILES[0]])
    resolutions = []
    for i, component in enumerate(matrix['componentes_curriculares']):
        before = component['fonte_conhecimento']
        after = EMENTAS.get(before)
        if after not in blobs:
            raise ValueError(f'Ementa sem resolução explícita: {before}')
        resolutions.append({'component_id': component['id'], 'source_file': FILES[0],
                            'json_pointer': f'/componentes_curriculares/{i}/fonte_conhecimento',
                            'before': before, 'after': after, 'rule_id': 'EMENTA_MANIFEST',
                            'reason': RULES['EMENTA_MANIFEST']})
    texts = [{'source': {'file': name, 'line_start': 1,
                        'line_end': len(blobs[name].decode('utf-8').splitlines())},
              'text': blobs[name].decode('utf-8'), 'semantic_classification': None}
             for name in [FILES[1], FILES[2], FILES[5]]]
    counts = {}
    for table, rows in tables.items():
        counts[table] = {'source_records': len(rows), 'output_records': len(rows),
                        'unique_record_ids': len({r['record_id'] for r in rows}),
                        'links': dict(Counter(r['link_status'] for r in rows))}
    checks = {'one_to_one_source_records': all(
        [r['source']['record'] for r in rows] == list(range(1, len(rows) + 1)) for rows in tables.values()),
        'separate_tables_no_fact_join': True,
        'unambiguous_links_only': all(r['item_record_id'] is None or len(index[r['data'].get('id', r['data'].get('item_id'))]) == 1
                                     for rows in tables.values() for r in rows)}
    return {'itens.json': items, 'desempenho.json': performance, 'aplicacoes.json': applications,
            'matriz.json': {'source': {'file': FILES[0], 'json_pointer': ''}, 'data': matrix},
            'textos.json': texts, 'ementas_manifest.json': resolutions,
            'audit.json': audit, 'rules.json': RULES, 'pendencias.json': issues,
            'integrity.json': {'checks': checks, 'counts': counts, 'duplicate_grain_groups': duplicate_groups,
                               'issues_by_code': dict(Counter(x['code'] for x in issues)),
                               'audit_events': len(audit), 'source_kind': 'synthetic_case_data',
                               'pedagogical_quality': 'not_evaluated', 'operational_gain': 'not_measured'}}

def run(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    if (source / 'data_pack').is_dir():
        source = source / 'data_pack'
    if output == source or output.is_relative_to(source) or source.is_relative_to(output):
        raise ValueError('Saída e fonte devem ser árvores separadas.')
    blobs = {name: (source / name).read_bytes() for name in FILES}
    results = build(blobs)
    output.mkdir(parents=True, exist_ok=True)
    originals = output / 'originals'
    originals.mkdir(exist_ok=True)
    manifest = []
    for name, data in blobs.items():
        target = originals / name
        if target.exists() and target.read_bytes() != data:
            raise ValueError(f'Original preservado difere; use nova pasta de saída: {name}')
    for name, data in blobs.items():
        target = originals / name
        target.write_bytes(data)
        before, after, copied = sha(data), sha((source / name).read_bytes()), sha(target.read_bytes())
        manifest.append({'file': name, 'bytes': len(data), 'source_sha256_before': before,
                         'source_sha256_after': after, 'copy_sha256': copied})
    results['integrity.json']['checks']['source_and_copy_hashes_match'] = all(
        m['source_sha256_before'] == m['source_sha256_after'] == m['copy_sha256'] for m in manifest)
    results['manifest.json'] = manifest
    for name, value in results.items():
        (output / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if not all(results['integrity.json']['checks'].values()):
        raise ValueError('Falha de integridade; consulte integrity.json')
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = run(args.source, args.output)
    print(json.dumps(result['integrity.json'], ensure_ascii=False, indent=2))
