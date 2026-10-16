# Revisão independente da CLI local

Data: 2026-10-15. Revisor: agente separado da implementação. Escopo: software e rastreabilidade; sem revisão pedagógica e sem acesso semântico aos oito itens reservados.

## Resultado

Os **13 testes independentes passaram**. Com os arquivos originais, a execução produziu 68 registros únicos de origem: seis analisados por replay, 54 pendentes sem resposta gravada, oito reservados e zero erros técnicos. As seis análises são respostas anteriores dos agentes; não são inferência nova nem estimativa de acurácia.

Desempenho permaneceu com 69 registros e histórico de aplicação com 142, em arquivos separados. Nenhum item ficou liberado para prova. Os reservados não tiveram pedido nem análise gerados. Os testes manipulam dados em cópias temporárias e não imprimem enunciados reservados.

## Verificações adversariais reproduzíveis

Executar da pasta `case_aurora`, com Python 3.10+:

```powershell
python -B review/test_cli_independent.py
```

- Alterar enunciado ou alternativa de ITM-10041 impede o replay antigo (`fixture_stale`).
- Alterar somente gabarito bruto de `A` para `a`, mantendo o normalizado `A`, também impede o replay. O conteúdo bruto participa da identidade.
- Alterar ementa ou rubrica invalida as seis respostas gravadas.
- Resposta com JSON malformado, campo obrigatório ausente, citação inventada ou `readiness.ready=true` vira erro técnico; não contém análise aceita. O teste atualiza o checksum do arquivo alterado para exercitar o validador, além da proteção de checksum.
- Acrescentar uma cópia de ITM-10041 preserva 69 registros e bloqueia ambas as identidades em colisão, sem escolher silenciosamente um destino.
- Reexecutar no mesmo destino é recusado. O teste altera a fonte depois da primeira execução e verifica que todos os bytes da saída anterior permanecem iguais. Para uma nova execução, usa-se outra pasta; não há sobrescrita nem mistura de resultados antigos com novos.
- Os 12 casos que chamam a função diretamente rodam com criação de sockets bloqueada; o 13º testa a CLI em processo separado. As fontes copiadas e os diretórios congelados `output`, `mapping` e `replay_fixtures` são comparados por hash antes/depois.

## Problemas encontrados e limites

A CLI também foi executada em processo separado: respondeu com código 2 para JSON inválido e preservou os 68 registros, sinalizando um erro técnico.

Após os testes acima, o manager identificou um defeito real de apresentação: texto já corrompido foi gravado como UTF-8 no relatório, produzindo mojibake no título e em outros rótulos. Os 13 testes de integridade não cobriam a qualidade Unicode da apresentação, portanto seu sucesso não detectou esse defeito. O autor corrigiu os literais e acrescentou uma asserção Unicode aos testes. O manager regenerou a entrega em `runs/replay_final`.

O revisor confirmou na entrega regenerada o título Unicode exato `# Case Aurora — execução local de respostas gravadas` e ausência dos marcadores suspeitos `U+00C3`, `U+00E2 U+20AC` e `U+FFFD` tanto no relatório quanto no README. A contagem continuou 68 = 6 analisados + 54 pendentes + 8 reservados + 0 erros. O achado de apresentação fica registrado como **corrigido e reverificado**; nenhuma pendência impeditiva conhecida permanece no escopo testado. A verificação Unicode adicional não é uma revisão visual exaustiva de cada linha.

Há dois compromissos técnicos explícitos: a validação individual adapta o validador v2 de lote usando seis referências à mesma resposta em memória; somente um registro é exportado. Isso evita alterar a versão congelada, mas merece refatoração se o contrato crescer. O fingerprint usa a linha completa com sua proveniência, portanto mudança de posição/linhas pode invalidar replay mesmo sem mudar o texto. É um falso negativo conservador: gera pendência, não associação incorreta.

A primeira tentativa do verificador não chegou a executar a CLI: o diretório temporário padrão do sandbox negou acesso. O verificador foi ajustado para criar temporários sob `review/`, dentro da área gravável; a repetição completou os 13 testes. Essa falha ambiental não foi contabilizada como sucesso da aplicação.

A política de saída exige uma pasta nova. Isso impede resultado antigo de aparecer como uma execução atual, mas não fornece atualização incremental. Uma falha de ingestão anterior à leitura completa produz `run_error.json`; não é possível prometer um registro por questão se o próprio arquivo não puder ser interpretado.

O teste de sockets e a leitura do código apoiam a ausência de rede nesta implementação, sem constituir auditoria geral de segurança. O teste compara hashes locais; o manifesto de fixtures não é uma assinatura contra alteração deliberada simultânea de dados e manifesto. Validação literal não demonstra que a competência foi pedagogicamente avaliada, e concordância entre agentes não substitui especialista. Não houve API, uso semântico dos reservados, medição de ganho operacional ou teste de escala.

