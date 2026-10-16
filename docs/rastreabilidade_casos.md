# Três casos reais de rastreabilidade

Estes casos foram extraídos da base entregue e conferidos contra os CSVs originais preservados. Não são fixtures. O script `trace_examples.py` reproduz `rastreabilidade_casos.json`, com cada registro completo, campos raw/data, eventos, pendências e hash da fonte.

## 1. Padronização — ITM-10043

- Fonte: `04_itens_legado.csv`, registro 3, linha física 4.
- `record_id`: `04_itens_legado.csv:3`.
- Origem: `gabarito = "a"`.
- Saída: `data.gabarito = "A"`; `raw.gabarito = "a"` preservado.
- Auditoria: `field=gabarito`, `before="a"`, `after="A"`, `rule_id=ANSWER_CASE`.
- Justificativa da regra: letra isolada a–e convertida para maiúscula.
- O ano também passou de string `"2020"` para inteiro `2020` pela regra `INTEGER`. Não houve alteração do enunciado ou classificação curricular.

## 2. Pendência — ITM-10048

- Fonte: `04_itens_legado.csv`, registro 8, linha física 9.
- `record_id`: `04_itens_legado.csv:8`.
- Origem: `gabarito = "2"`.
- Saída: `data.gabarito = null`; `raw.gabarito = "2"` preservado.
- Auditoria: `before="2"`, `after=null`, `rule_id=ANSWER_UNRESOLVED`.
- Pendência: confirmar a convenção da origem. Não foi assumido `2 = B`, mesmo que uma IA consiga inferir a alternativa plausível a partir do conteúdo.
- O null significa **não resolvido**, não “não havia valor na origem”. O bruto, a regra e a pendência distinguem esses casos.

## 3. Dois semestres — ITM-10066

Primeira observação:

- Fonte: `05_desempenho_itens.csv`, registro 26, linha 27.
- Origem e saída do ID: `ITM-10066`, sem mudança.
- Semestre: `2025.1`; respondentes `"1533" → 1533`; acerto `"0.67" → 0.67`.
- `record_id = 05_desempenho_itens.csv:26`.

Segunda observação:

- Fonte: `05_desempenho_itens.csv`, registro 67, linha 68.
- ID: `ITM10066 → ITM-10066`, regra `ID_HYPHEN`.
- Semestre: `2024.1`; respondentes `"1588" → 1588`; acerto `"0.64" → 0.64`.
- `record_id = 05_desempenho_itens.csv:67`.

As duas apontam para `item_record_id = 04_itens_legado.csv:26`, destino único no cadastro. Nenhuma substituiu a outra. Seus dois registros de aplicação continuam em outra tabela: provas `PRV-2021-0171` (2021.1) e `PRV-2024-0211` (2024.1).

Uma junção somente pelo ID entre 2 observações e 2 aplicações produziria 4 linhas; elas **não foram produzidas na base**. Também não se inferiu correspondência entre o desempenho de 2025.1 e uma prova de outro semestre. O histórico não traz prova de 2025.1 para esse item: a completude entre as exportações não está demonstrada.

## Limite

Rastreabilidade e preservação técnica não validam gabarito pedagogicamente, nem provam ganho operacional.
