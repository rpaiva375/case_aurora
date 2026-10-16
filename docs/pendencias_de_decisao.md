# Pendências além das verificações estruturais

As ocorrências de `output/pendencias.json` são achados determinísticos de ingestão, não um inventário completo dos problemas pedagógicos do acervo. Uma ocorrência pode ser um campo de um item já citado em outra ocorrência. Não somar essas ocorrências como se fossem itens distintos.

## Dados e contrato de origem

- **ITM-10048 e ITM-20021:** gabaritos brutos `2` e `1`; o usuário determinou manter pendentes. É necessário confirmar a convenção da origem. O campo canônico está null; o valor original permanece no campo raw, na cópia original e na auditoria.
- **ITM-10039 e ITM-20011:** registros de desempenho sem questão correspondente neste pacote. Foram preservados, sem criar questões artificiais. Solicitar esclarecimento da abrangência da exportação antes de associar a outro item.
- **ITM-10066:** duas observações, 2024.1 e 2025.1, permanecem distintas. Padronização de ID não significa deduplicação temporal.
- **Fila de revisão:** cabeçalho declara 16 registros, mas a unidade de registro não é definida. O texto foi preservado integralmente; não inferimos quantidade de reprovações a partir de blocos ou mensagens.
- **Estatísticas:** metodologia do índice de discriminação e critérios de interpretação não estão definidos. Não usar valores ausentes como zero nem índices negativos como prova automática de defeito.

## Questões identificadas no diagnóstico, sem resolução nesta etapa

- **ITM-20043:** referência a “texto acima” sem texto-base na exportação. Observação do diagnóstico, também relatada na fila; não é uma detecção semântica implementada pelo pipeline. Deve-se obter o contexto ou submeter à revisão, sem preencher por inferência.
- **ITM-10042/10043 e ITM-20020/20021:** pares apontados como semelhantes na fila. Não excluídos nem consolidados; proximidade temática não comprova equivalência avaliativa.
- **ITM-20042:** C e D iguais geram pendência estrutural. O gabarito registrado é B; a alegação histórica de prejuízo a quem marcou D não está comprovada apenas pelo CSV.
- **ITM-10045 e ITM-20044:** alternativas ausentes são registradas, mas o mínimo obrigatório de alternativas não foi definido.
- **Itens 30007–30010:** pertencimento ao recorte curricular não foi decidido. Nomes de disciplina não foram usados para impor classificação.
- **Exposição em provas:** repetição histórica é observável, mas limiar de exposição, versão do item e janelas de aplicação não estão definidos. Não há comprovação de vazamento nem quarentena aplicada.

## Decisões para o futuro mapeamento

- Definir a unidade de “1–3 nós” e a relação permitida entre objeto e competência; exemplos e pergunta preparada estão em `decisoes_etapa_1.md`.
- Definir o papel da revisão de coerência feita pelo usuário e o processo posterior de validação pedagógica especializada, sem confundir os dois.
- Construir medida de benefício operacional e referência humana para avaliar sugestões. Nenhum ganho operacional ou qualidade semântica foi medido na etapa de ingestão.

Estas pendências não impedem preservar e conferir os dados; impedem afirmar que o acervo está pedagogicamente aprovado ou que o benefício da solução foi comprovado.
