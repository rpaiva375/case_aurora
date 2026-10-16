# Case Aurora â€” execuÃ§Ã£o local de respostas gravadas

**MOCK/REPLAY: nenhuma inferÃªncia nova, chamada de API ou validaÃ§Ã£o pedagÃ³gica.**

Registros: 68; analisados por replay: 6; pendentes sem anÃ¡lise: 54; reservados: 8; erros tÃ©cnicos: 0.
Analisados incluem sugestÃµes, objeto com competÃªncia pendente e abstenÃ§Ãµes. Essas classes nÃ£o medem acurÃ¡cia.
Nenhum item estÃ¡ liberado para prova. RevisÃ£o de coerÃªncia e validaÃ§Ã£o pedagÃ³gica especializada continuam pendentes.
Desempenho e aplicaÃ§Ãµes permanecem separados em ingestion/. OcorrÃªncias estruturais nÃ£o sÃ£o somadas Ã  quantidade de questÃµes.

## QuestÃµes

### ITM-10041 â€” ANALISADO (replay)

Origem: 04_itens_legado.csv:1, linhas 2â€“2. Motivo: recorded_response_replayed.
Estado semÃ¢ntico: suggested
Assunto: Capitalizacao simples e montante.
Tarefa exigida: Calcular montante em juros simples com capital, taxa e prazo fornecidos: 12000*(1+0.02*7)=13680.
Objeto (supported): OC-GF-01. Resolver capitalizacao simples e parte textual explicita de HAB-03.1. A operacao e simples, mas executa a habilidade, nao apenas um pre-requisito; nao exige demonstrar capitalizacao composta ou toda COMP-03.
CompetÃªncia (partial_suggestion): Resolver capitalizacao simples e parte textual explicita de HAB-03.1. A operacao e simples, mas executa a habilidade, nao apenas um pre-requisito; nao exige demonstrar capitalizacao composta ou toda COMP-03. Escopo: Somente resolver capitalizacao simples; nao composta, equivalencia ou competencia integral.
VÃ­nculos: OC-GF-01 â†’ COMP-03
Problemas de uso: nenhum adicional registrado; isso nÃ£o libera uso
Regra provisÃ³ria de nÃ³s (separada): 2 nÃ³s identificados; 1 pares; estado within_provisional_limit. Nenhum vÃ­nculo truncado.
Resposta bruta: [raw_responses/001.json](raw_responses/001.json)
EvidÃªncias:
- item: 04_itens_legado.csv:1, enunciado: "Um capital de R$ 12.000,00 foi aplicado a juros simples de 2% ao mes durante 7 meses. Qual o montante ao final do periodo?"
- item: 04_itens_legado.csv:1, alternativa_a: "R$ 13.680,00"
- matrix: 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/0/nome: "Valor do dinheiro no tempo: capitalização simples e composta"
- matrix: 01_matriz_competencias.json, /competencias/2/descricao: "Aplicar instrumentos de matemática financeira na análise de operações de crédito, investimento e financiamento."
- matrix: 01_matriz_competencias.json, /competencias/2/habilidades/0/descricao: "Resolver problemas de capitalização simples e composta e de equivalência de capitais."
- ementa: 02_ementa_gestao_financeira.txt, linhas 38â€“40: "1.1 Capitalização simples e composta\nNo regime de juros simples, os juros incidem sempre sobre o capital inicial, de\nmodo que o montante cresce linearmente: M = C x (1 + i x n). No regime de juros"
Liberado para prova: **nÃ£o**.

### ITM-10042 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:2, linhas 3â€“3. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10043 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:3, linhas 4â€“4. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10044 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:4, linhas 5â€“5. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10045 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:5, linhas 6â€“6. Motivo: fixture_missing.
PendÃªncias estruturais: MISSING_FIELD (alternativa_e): "Campo vazio na fonte; não imputado."
Liberado para prova: **nÃ£o**.

### ITM-10046 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:6, linhas 7â€“7. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10047 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:7, linhas 8â€“8. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10048 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:8, linhas 9â€“9. Motivo: fixture_missing.
PendÃªncias estruturais: ANSWER_UNRESOLVED (gabarito): {"raw": "2", "decision": "Confirmar convenção na origem."}
Liberado para prova: **nÃ£o**.

### ITM-10049 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:9, linhas 10â€“10. Motivo: prospective_holdout_excluded.
Liberado para prova: **nÃ£o**.

### ITM-10050 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:10, linhas 11â€“11. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10051 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:11, linhas 12â€“12. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10052 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:12, linhas 13â€“13. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10053 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:13, linhas 14â€“14. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10054 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:14, linhas 15â€“15. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10055 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:15, linhas 16â€“16. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10056 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:16, linhas 17â€“17. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10057 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:17, linhas 18â€“18. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10058 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:18, linhas 19â€“19. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10059 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:19, linhas 20â€“20. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10060 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:20, linhas 21â€“21. Motivo: prospective_holdout_excluded.
Liberado para prova: **nÃ£o**.

### ITM-10061 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:21, linhas 22â€“22. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10062 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:22, linhas 23â€“23. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10063 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:23, linhas 24â€“24. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10064 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:24, linhas 25â€“25. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10065 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:25, linhas 26â€“26. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10066 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:26, linhas 27â€“27. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10067 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:27, linhas 28â€“28. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10068 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:28, linhas 29â€“29. Motivo: fixture_missing.
PendÃªncias estruturais: MISSING_FIELD (gabarito): "Campo vazio na fonte; não imputado."
Liberado para prova: **nÃ£o**.

### ITM-10069 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:29, linhas 30â€“30. Motivo: prospective_holdout_excluded.
Liberado para prova: **nÃ£o**.

### ITM-10070 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:30, linhas 31â€“31. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10071 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:31, linhas 32â€“32. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-10072 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:32, linhas 33â€“33. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20015 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:33, linhas 34â€“34. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20016 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:34, linhas 35â€“35. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20017 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:35, linhas 36â€“36. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20018 â€” ANALISADO (replay)

Origem: 04_itens_legado.csv:36, linhas 37â€“37. Motivo: recorded_response_replayed.
Estado semÃ¢ntico: suggested
Assunto: Motivacao no trabalho por Herzberg.
Tarefa exigida: Interpretar o cenario de remuneracao, reconhecimento e crescimento usando a distincao de fatores de Herzberg; nao confirmar B como correta.
Objeto (supported): OC-CO-02. Interpretar comportamento no trabalho por teoria motivacional executa aspecto explicito de HAB-04.1. O vinculo tematico e cognitivo subsiste mesmo com validade de B contestada.
CompetÃªncia (partial_suggestion): Interpretar comportamento no trabalho por teoria motivacional executa aspecto explicito de HAB-04.1. O vinculo tematico e cognitivo subsiste mesmo com validade de B contestada. Escopo: Somente interpretacao motivacional localizada; nao decisao de pessoas nem competencia integral.
VÃ­nculos: OC-CO-02 â†’ COMP-04
Problemas de uso: Validade de B contestada: atribui insatisfacao a ausencia de motivadores, enquanto ementa distingue sua atuacao em satisfacao/esforco de ausencia de fatores higienicos. Remuneracao adequada nao prova adequacao de todos fatores higienicos. Revisar antes de usar acerto como evidencia.
Regra provisÃ³ria de nÃ³s (separada): 2 nÃ³s identificados; 1 pares; estado within_provisional_limit. Nenhum vÃ­nculo truncado.
Resposta bruta: [raw_responses/036.json](raw_responses/036.json)
EvidÃªncias:
- item: 04_itens_legado.csv:36, enunciado: "Uma equipe de suporte tecnico apresenta alta rotatividade. A pesquisa interna aponta salarios compativeis com o mercado, mas ausencia de reconhecimento e de perspectiva de crescimento. A luz da teoria dos dois fatores de Herzberg, qual interpretacao e correta?"
- item: 04_itens_legado.csv:36, alternativa_b: "Os fatores motivacionais estao ausentes, o que explica a insatisfacao apesar da remuneracao adequada"
- matrix: 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/1/nome: "Motivação no trabalho: teorias de conteúdo e de processo"
- matrix: 01_matriz_competencias.json, /competencias/3/descricao: "Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas."
- matrix: 01_matriz_competencias.json, /competencias/3/habilidades/0/descricao: "Explicar comportamentos no trabalho a partir de teorias de motivação, percepção e atitudes."
- ementa: 03_ementa_comportamento_organizacional.txt, linhas 69â€“75: "razoavelmente atendido. A teoria dos dois fatores, de Herzberg, distingue fatores\nhigiênicos — salário, condições de trabalho, políticas da empresa, supervisão —,\ncuja ausência gera insatisfação mas cuja presença não motiva, dos fatores\nmotivacionais — reconhecimento, responsabilidade, conteúdo do trabalho,\ncrescimento —, que atuam sobre a satisfação e o esforço. A consequência prática é\nque corrigir apenas fatores higiênicos remove insatisfação sem produzir\nengajamento."
- matrix: 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/6/nome: "Cultura e clima organizacional"
Liberado para prova: **nÃ£o**.

### ITM-20019 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:37, linhas 38â€“38. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20020 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:38, linhas 39â€“39. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20021 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:39, linhas 40â€“40. Motivo: fixture_missing.
PendÃªncias estruturais: ANSWER_UNRESOLVED (gabarito): {"raw": "1", "decision": "Confirmar convenção na origem."}
Liberado para prova: **nÃ£o**.

### ITM-20022 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:40, linhas 41â€“41. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20023 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:41, linhas 42â€“42. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20024 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:42, linhas 43â€“43. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20025 â€” ANALISADO (replay)

Origem: 04_itens_legado.csv:43, linhas 44â€“44. Motivo: recorded_response_replayed.
Estado semÃ¢ntico: object_supported_competency_pending
Assunto: Bases de poder e influencia sobre equipe.
Tarefa exigida: Classificar a base de poder descrita por admiracao/identificacao, distinguindo-a de conhecimento tecnico. O efeito adesao e sua causa ja sao informados.
Objeto (supported): OC-CO-04. OC-CO-04 sustentado por classificacao contextual de bases de poder. COMP-04 permanece pendente: nomear a base cuja causa e adesao ja foram dadas nao demonstra por si analisar seu efeito (objetivo 3) ou avaliar efeito de estilos (HAB-04.3). Nao se exige competencia inteira nem se veta operacao simples; falta correspondencia operacional suficiente com um aspecto explicito.
CompetÃªncia (pending): OC-CO-04 sustentado por classificacao contextual de bases de poder. COMP-04 permanece pendente: nomear a base cuja causa e adesao ja foram dadas nao demonstra por si analisar seu efeito (objetivo 3) ou avaliar efeito de estilos (HAB-04.3). Nao se exige competencia inteira nem se veta operacao simples; falta correspondencia operacional suficiente com um aspecto explicito. Escopo: Nenhum aspecto de COMP aprovado; classificacao de base e OC sustentado.
VÃ­nculos: nenhum
Problemas de uso: Trajetoria tecnica também evoca poder de especialista; identificação favorece B. Revisão humana deve decidir se a classificação localizada é evidência suficiente de COMP-04.
Regra provisÃ³ria de nÃ³s (separada): 1 nÃ³s identificados; 0 pares; estado incomplete_mapping. Nenhum vÃ­nculo truncado.
Resposta bruta: [raw_responses/043.json](raw_responses/043.json)
EvidÃªncias:
- item: 04_itens_legado.csv:43, enunciado: "Um gerente recem-promovido obtem adesao da equipe principalmente porque os colaboradores admiram sua trajetoria tecnica e desejam ser associados a ele. Qual base de poder predomina?"
- item: 04_itens_legado.csv:43, alternativa_b: "Poder de referencia"
- item: 04_itens_legado.csv:43, alternativa_e: "Poder de especialista"
- matrix: 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/3/nome: "Liderança e poder nas organizações"
- matrix: 01_matriz_competencias.json, /competencias/3/descricao: "Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas."
- matrix: 01_matriz_competencias.json, /competencias/3/habilidades/2/descricao: "Avaliar o efeito de estilos de liderança sobre resultados e sobre o engajamento da equipe."
- ementa: 03_ementa_comportamento_organizacional.txt, linhas 118â€“124: "3.2 Bases de poder\nPoder é a capacidade de influenciar o comportamento de outra pessoa. As bases\nformais incluem o poder legítimo, decorrente do cargo, o poder de recompensa e o\npoder coercitivo. As bases pessoais incluem o poder de competência, derivado de\nconhecimento técnico reconhecido, e o poder de referência, derivado de admiração\ne identificação. Bases pessoais tendem a produzir comprometimento; bases\ncoercitivas tendem a produzir apenas obediência."
- matrix: 01_matriz_competencias.json, /competencias/4/descricao: "Conduzir processos de comunicação, negociação e mediação de conflitos em equipes de trabalho."
- ementa: 03_ementa_comportamento_organizacional.txt, linhas 30â€“30: "3. Analisar o efeito de estilos de liderança e de bases de poder sobre a equipe."
Liberado para prova: **nÃ£o**.

### ITM-20026 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:44, linhas 45â€“45. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20027 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:45, linhas 46â€“46. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20028 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:46, linhas 47â€“47. Motivo: prospective_holdout_excluded.
Liberado para prova: **nÃ£o**.

### ITM-20029 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:47, linhas 48â€“48. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20030 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:48, linhas 49â€“49. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20031 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:49, linhas 50â€“50. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20032 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:50, linhas 51â€“51. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20033 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:51, linhas 52â€“52. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20034 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:52, linhas 53â€“53. Motivo: prospective_holdout_excluded.
Liberado para prova: **nÃ£o**.

### ITM-20035 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:53, linhas 54â€“54. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20036 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:54, linhas 55â€“55. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20037 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:55, linhas 56â€“56. Motivo: prospective_holdout_excluded.
Liberado para prova: **nÃ£o**.

### ITM-20038 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:56, linhas 57â€“57. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20039 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:57, linhas 58â€“58. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20040 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:58, linhas 59â€“59. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20041 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:59, linhas 60â€“60. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-30007 â€” ANALISADO (replay)

Origem: 04_itens_legado.csv:60, linhas 61â€“61. Motivo: recorded_response_replayed.
Estado semÃ¢ntico: abstained
Assunto: Requisitos de validade de negocio juridico.
Tarefa exigida: Reconhecer uma lista de requisitos juridicos entre alternativas; completude normativa nao verificada.
Objeto (outside_provided_scope): nenhum sustentado. Nao existe OC juridico especifico na matriz fornecida. Reconhecer requisitos legais nao exige reconhecer dilema etico ou avaliar impactos de gestao. Ausencia de escopo nao declara invalidade juridica.
CompetÃªncia (not_established): Nao existe OC juridico especifico na matriz fornecida. Reconhecer requisitos legais nao exige reconhecer dilema etico ou avaliar impactos de gestao. Ausencia de escopo nao declara invalidade juridica. Escopo: Sem inferencia juridica normativa ou aconselhamento.
VÃ­nculos: nenhum
Problemas de uso: Gabarito A preservado como dado; completude legal nao verificada pelas fontes disponiveis.
Regra provisÃ³ria de nÃ³s (separada): 0 nÃ³s identificados; 0 pares; estado not_applicable. Nenhum vÃ­nculo truncado.
Resposta bruta: [raw_responses/060.json](raw_responses/060.json)
EvidÃªncias:
- item: 04_itens_legado.csv:60, enunciado: "Sao requisitos de validade do negocio juridico, nos termos do Codigo Civil:"
- item: 04_itens_legado.csv:60, alternativa_a: "Agente capaz, objeto licito e forma prescrita ou nao defesa em lei"
- matrix: 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/7/nome: "Ética e transparência na informação financeira"
- matrix: 01_matriz_competencias.json, /competencias/5/descricao: "Posicionar-se de forma ética e responsável nas decisões de gestão, considerando impactos sociais e ambientais."
- ementa: 02_ementa_gestao_financeira.txt, linhas 18â€“18: "diversificação. Ética e transparência na informação financeira."
Liberado para prova: **nÃ£o**.

### ITM-30008 â€” ANALISADO (replay)

Origem: 04_itens_legado.csv:61, linhas 62â€“62. Motivo: recorded_response_replayed.
Estado semÃ¢ntico: abstained
Assunto: Formula do ponto de equilibrio contabil.
Tarefa exigida: Reconhecer a expressao de calculo entre alternativas; nao realizar calculo numerico.
Objeto (outside_provided_scope): nenhum sustentado. Nao existe OC especifico de custo-volume-lucro/ponto de equilibrio na matriz fornecida. Reconhecer formula e uma operacao identificavel, nao um veto por facilidade. OC-GF-04 trata demonstracoes e indicadores, e COMP-03 trata instrumentos de matematica financeira; mera divisao nao estabelece esses aspectos.
CompetÃªncia (not_established): Nao existe OC especifico de custo-volume-lucro/ponto de equilibrio na matriz fornecida. Reconhecer formula e uma operacao identificavel, nao um veto por facilidade. OC-GF-04 trata demonstracoes e indicadores, e COMP-03 trata instrumentos de matematica financeira; mera divisao nao estabelece esses aspectos. Escopo: Reconhecimento da formula sem OC especifico sustentado.
VÃ­nculos: nenhum
Problemas de uso: Precisao editorial da unidade de ponto de equilibrio deve ser revisada; nao completar o enunciado.
Regra provisÃ³ria de nÃ³s (separada): 0 nÃ³s identificados; 0 pares; estado not_applicable. Nenhum vÃ­nculo truncado.
Resposta bruta: [raw_responses/061.json](raw_responses/061.json)
EvidÃªncias:
- item: 04_itens_legado.csv:61, enunciado: "No calculo do ponto de equilibrio contabil, considera-se:"
- item: 04_itens_legado.csv:61, alternativa_a: "Custos fixos divididos pela margem de contribuicao unitaria"
- matrix: 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/3/nome: "Análise de demonstrações financeiras por indicadores"
- matrix: 01_matriz_competencias.json, /competencias/0/descricao: "Diagnosticar a situação econômico-financeira de uma organização a partir de suas demonstrações contábeis e indicadores."
- ementa: 02_ementa_gestao_financeira.txt, linhas 15â€“16: "do capital de giro. Análise das demonstrações financeiras por indicadores de\nliquidez, endividamento e rentabilidade. Custo de capital e custo médio"
Liberado para prova: **nÃ£o**.

### ITM-30009 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:62, linhas 63â€“63. Motivo: fixture_missing.
PendÃªncias estruturais: MISSING_FIELD (disciplina_informada): "Campo vazio na fonte; não imputado."; MISSING_FIELD (origem_banco): "Campo vazio na fonte; não imputado."
Liberado para prova: **nÃ£o**.

### ITM-30010 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:63, linhas 64â€“64. Motivo: prospective_holdout_excluded.
PendÃªncias estruturais: MISSING_FIELD (ano_aplicacao): "Campo vazio na fonte; não imputado."
Liberado para prova: **nÃ£o**.

### ITM-10073 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:64, linhas 65â€“65. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20042 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:65, linhas 66â€“66. Motivo: fixture_missing.
PendÃªncias estruturais: DUPLICATE_ALTERNATIVES (alternativas): [["alternativa_c", "alternativa_d"]]
Liberado para prova: **nÃ£o**.

### ITM-10074 â€” PENDENTE â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:66, linhas 67â€“67. Motivo: fixture_missing.
Liberado para prova: **nÃ£o**.

### ITM-20043 â€” ANALISADO (replay)

Origem: 04_itens_legado.csv:67, linhas 68â€“68. Motivo: recorded_response_replayed.
Estado semÃ¢ntico: abstained
Assunto: Teorias do comportamento; objeto especifico indeterminavel sem texto-base.
Tarefa exigida: Demanda pretendida: relacionar comportamento do gestor a teoria. Operacao executavel indeterminada: texto acima ausente.
Objeto (indeterminate): nenhum sustentado. Incompletude impede observar comportamento necessario para sustentar OC e competencia. Alternativas e gabarito nao reconstituem texto-base.
CompetÃªncia (not_established): Incompletude impede observar comportamento necessario para sustentar OC e competencia. Alternativas e gabarito nao reconstituem texto-base. Escopo: Sem inferencia curricular positiva.
VÃ­nculos: nenhum
Problemas de uso: Recuperar texto-base na origem antes de reapreciar.
Regra provisÃ³ria de nÃ³s (separada): 0 nÃ³s identificados; 0 pares; estado not_applicable. Nenhum vÃ­nculo truncado.
Resposta bruta: [raw_responses/067.json](raw_responses/067.json)
EvidÃªncias:
- item: 04_itens_legado.csv:67, enunciado: "Com base no texto acima, qual teoria explica o comportamento do gestor descrito?"
- item: 04_itens_legado.csv:67, alternativa_b: "Teoria Y"
Liberado para prova: **nÃ£o**.

### ITM-20044 â€” RESERVADO â€” sem anÃ¡lise

Origem: 04_itens_legado.csv:68, linhas 69â€“69. Motivo: prospective_holdout_excluded.
PendÃªncias estruturais: MISSING_FIELD (alternativa_d): "Campo vazio na fonte; não imputado."; MISSING_FIELD (alternativa_e): "Campo vazio na fonte; não imputado."; MISSING_FIELD (gabarito): "Campo vazio na fonte; não imputado."; MISSING_FIELD (origem_banco): "Campo vazio na fonte; não imputado."
Liberado para prova: **nÃ£o**.
