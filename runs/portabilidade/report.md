# Case Aurora — execução local de respostas gravadas

**MOCK/REPLAY: nenhuma inferência nova, chamada de API ou validação pedagógica.**

Registros: 68; analisados por replay: 6; pendentes sem análise: 54; reservados: 8; erros técnicos: 0.

Analisados incluem sugestões, objeto com competência pendente e abstenções. Essas classes não medem acurácia.

Nenhum item está liberado para prova. Revisão de coerência e validação pedagógica especializada continuam pendentes.

Desempenho e aplicações permanecem separados em ingestion/. Ocorrências estruturais não são somadas à quantidade de questões.

## Questões

### ITM-10041 — ANALISADO (replay)

Origem: 04_itens_legado.csv:1, linhas 2–2. Motivo: recorded_response_replayed.

Estado semântico: suggested

Assunto: Capitalizacao simples e montante.

Tarefa exigida: Calcular montante em juros simples com capital, taxa e prazo fornecidos: 12000*(1+0.02*7)=13680.

Objeto (supported): OC-GF-01. Resolver capitalizacao simples e parte textual explicita de HAB-03.1. A operacao e simples, mas executa a habilidade, nao apenas um pre-requisito; nao exige demonstrar capitalizacao composta ou toda COMP-03.

Competência (partial_suggestion): Resolver capitalizacao simples e parte textual explicita de HAB-03.1. A operacao e simples, mas executa a habilidade, nao apenas um pre-requisito; nao exige demonstrar capitalizacao composta ou toda COMP-03. Escopo: Somente resolver capitalizacao simples; nao composta, equivalencia ou competencia integral.

Vínculos: OC-GF-01 → COMP-03

Problemas de uso: nenhum adicional registrado; isso não libera uso

Regra provisória de nós (separada): 2 nós identificados; 1 pares; estado within_provisional_limit. Nenhum vínculo truncado.

Resposta bruta: [raw_responses/001.json](raw_responses/001.json)

Evidências:

- item: 04_itens_legado.csv:1, enunciado: "Um capital de R$ 12.000,00 foi aplicado a juros simples de 2% ao mes durante 7 meses. Qual o montante ao final do periodo?"

- item: 04_itens_legado.csv:1, alternativa_a: "R$ 13.680,00"

- matrix: 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/0/nome: "Valor do dinheiro no tempo: capitalização simples e composta"

- matrix: 01_matriz_competencias.json, /competencias/2/descricao: "Aplicar instrumentos de matemática financeira na análise de operações de crédito, investimento e financiamento."

- matrix: 01_matriz_competencias.json, /competencias/2/habilidades/0/descricao: "Resolver problemas de capitalização simples e composta e de equivalência de capitais."

- ementa: 02_ementa_gestao_financeira.txt, linhas 38–40: "1.1 Capitalização simples e composta\nNo regime de juros simples, os juros incidem sempre sobre o capital inicial, de\nmodo que o montante cresce linearmente: M = C x (1 + i x n). No regime de juros"

Liberado para prova: **não**.

### ITM-10042 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:2, linhas 3–3. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10043 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:3, linhas 4–4. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10044 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:4, linhas 5–5. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10045 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:5, linhas 6–6. Motivo: fixture_missing.

Pendências estruturais: MISSING_FIELD (alternativa_e): "Campo vazio na fonte; não imputado."

Liberado para prova: **não**.

### ITM-10046 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:6, linhas 7–7. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10047 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:7, linhas 8–8. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10048 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:8, linhas 9–9. Motivo: fixture_missing.

Pendências estruturais: ANSWER_UNRESOLVED (gabarito): {"raw": "2", "decision": "Confirmar convenção na origem."}

Liberado para prova: **não**.

### ITM-10049 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:9, linhas 10–10. Motivo: prospective_holdout_excluded.

Liberado para prova: **não**.

### ITM-10050 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:10, linhas 11–11. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10051 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:11, linhas 12–12. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10052 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:12, linhas 13–13. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10053 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:13, linhas 14–14. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10054 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:14, linhas 15–15. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10055 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:15, linhas 16–16. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10056 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:16, linhas 17–17. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10057 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:17, linhas 18–18. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10058 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:18, linhas 19–19. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10059 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:19, linhas 20–20. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10060 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:20, linhas 21–21. Motivo: prospective_holdout_excluded.

Liberado para prova: **não**.

### ITM-10061 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:21, linhas 22–22. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10062 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:22, linhas 23–23. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10063 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:23, linhas 24–24. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10064 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:24, linhas 25–25. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10065 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:25, linhas 26–26. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10066 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:26, linhas 27–27. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10067 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:27, linhas 28–28. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10068 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:28, linhas 29–29. Motivo: fixture_missing.

Pendências estruturais: MISSING_FIELD (gabarito): "Campo vazio na fonte; não imputado."

Liberado para prova: **não**.

### ITM-10069 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:29, linhas 30–30. Motivo: prospective_holdout_excluded.

Liberado para prova: **não**.

### ITM-10070 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:30, linhas 31–31. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10071 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:31, linhas 32–32. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-10072 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:32, linhas 33–33. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20015 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:33, linhas 34–34. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20016 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:34, linhas 35–35. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20017 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:35, linhas 36–36. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20018 — ANALISADO (replay)

Origem: 04_itens_legado.csv:36, linhas 37–37. Motivo: recorded_response_replayed.

Estado semântico: suggested

Assunto: Motivacao no trabalho por Herzberg.

Tarefa exigida: Interpretar o cenario de remuneracao, reconhecimento e crescimento usando a distincao de fatores de Herzberg; nao confirmar B como correta.

Objeto (supported): OC-CO-02. Interpretar comportamento no trabalho por teoria motivacional executa aspecto explicito de HAB-04.1. O vinculo tematico e cognitivo subsiste mesmo com validade de B contestada.

Competência (partial_suggestion): Interpretar comportamento no trabalho por teoria motivacional executa aspecto explicito de HAB-04.1. O vinculo tematico e cognitivo subsiste mesmo com validade de B contestada. Escopo: Somente interpretacao motivacional localizada; nao decisao de pessoas nem competencia integral.

Vínculos: OC-CO-02 → COMP-04

Problemas de uso: Validade de B contestada: atribui insatisfacao a ausencia de motivadores, enquanto ementa distingue sua atuacao em satisfacao/esforco de ausencia de fatores higienicos. Remuneracao adequada nao prova adequacao de todos fatores higienicos. Revisar antes de usar acerto como evidencia.

Regra provisória de nós (separada): 2 nós identificados; 1 pares; estado within_provisional_limit. Nenhum vínculo truncado.

Resposta bruta: [raw_responses/036.json](raw_responses/036.json)

Evidências:

- item: 04_itens_legado.csv:36, enunciado: "Uma equipe de suporte tecnico apresenta alta rotatividade. A pesquisa interna aponta salarios compativeis com o mercado, mas ausencia de reconhecimento e de perspectiva de crescimento. A luz da teoria dos dois fatores de Herzberg, qual interpretacao e correta?"

- item: 04_itens_legado.csv:36, alternativa_b: "Os fatores motivacionais estao ausentes, o que explica a insatisfacao apesar da remuneracao adequada"

- matrix: 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/1/nome: "Motivação no trabalho: teorias de conteúdo e de processo"

- matrix: 01_matriz_competencias.json, /competencias/3/descricao: "Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas."

- matrix: 01_matriz_competencias.json, /competencias/3/habilidades/0/descricao: "Explicar comportamentos no trabalho a partir de teorias de motivação, percepção e atitudes."

- ementa: 03_ementa_comportamento_organizacional.txt, linhas 69–75: "razoavelmente atendido. A teoria dos dois fatores, de Herzberg, distingue fatores\nhigiênicos — salário, condições de trabalho, políticas da empresa, supervisão —,\ncuja ausência gera insatisfação mas cuja presença não motiva, dos fatores\nmotivacionais — reconhecimento, responsabilidade, conteúdo do trabalho,\ncrescimento —, que atuam sobre a satisfação e o esforço. A consequência prática é\nque corrigir apenas fatores higiênicos remove insatisfação sem produzir\nengajamento."

- matrix: 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/6/nome: "Cultura e clima organizacional"

Liberado para prova: **não**.

### ITM-20019 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:37, linhas 38–38. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20020 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:38, linhas 39–39. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20021 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:39, linhas 40–40. Motivo: fixture_missing.

Pendências estruturais: ANSWER_UNRESOLVED (gabarito): {"raw": "1", "decision": "Confirmar convenção na origem."}

Liberado para prova: **não**.

### ITM-20022 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:40, linhas 41–41. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20023 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:41, linhas 42–42. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20024 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:42, linhas 43–43. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20025 — ANALISADO (replay)

Origem: 04_itens_legado.csv:43, linhas 44–44. Motivo: recorded_response_replayed.

Estado semântico: object_supported_competency_pending

Assunto: Bases de poder e influencia sobre equipe.

Tarefa exigida: Classificar a base de poder descrita por admiracao/identificacao, distinguindo-a de conhecimento tecnico. O efeito adesao e sua causa ja sao informados.

Objeto (supported): OC-CO-04. OC-CO-04 sustentado por classificacao contextual de bases de poder. COMP-04 permanece pendente: nomear a base cuja causa e adesao ja foram dadas nao demonstra por si analisar seu efeito (objetivo 3) ou avaliar efeito de estilos (HAB-04.3). Nao se exige competencia inteira nem se veta operacao simples; falta correspondencia operacional suficiente com um aspecto explicito.

Competência (pending): OC-CO-04 sustentado por classificacao contextual de bases de poder. COMP-04 permanece pendente: nomear a base cuja causa e adesao ja foram dadas nao demonstra por si analisar seu efeito (objetivo 3) ou avaliar efeito de estilos (HAB-04.3). Nao se exige competencia inteira nem se veta operacao simples; falta correspondencia operacional suficiente com um aspecto explicito. Escopo: Nenhum aspecto de COMP aprovado; classificacao de base e OC sustentado.

Vínculos: nenhum

Problemas de uso: Trajetoria tecnica também evoca poder de especialista; identificação favorece B. Revisão humana deve decidir se a classificação localizada é evidência suficiente de COMP-04.

Regra provisória de nós (separada): 1 nós identificados; 0 pares; estado incomplete_mapping. Nenhum vínculo truncado.

Resposta bruta: [raw_responses/043.json](raw_responses/043.json)

Evidências:

- item: 04_itens_legado.csv:43, enunciado: "Um gerente recem-promovido obtem adesao da equipe principalmente porque os colaboradores admiram sua trajetoria tecnica e desejam ser associados a ele. Qual base de poder predomina?"

- item: 04_itens_legado.csv:43, alternativa_b: "Poder de referencia"

- item: 04_itens_legado.csv:43, alternativa_e: "Poder de especialista"

- matrix: 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/3/nome: "Liderança e poder nas organizações"

- matrix: 01_matriz_competencias.json, /competencias/3/descricao: "Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas."

- matrix: 01_matriz_competencias.json, /competencias/3/habilidades/2/descricao: "Avaliar o efeito de estilos de liderança sobre resultados e sobre o engajamento da equipe."

- ementa: 03_ementa_comportamento_organizacional.txt, linhas 118–124: "3.2 Bases de poder\nPoder é a capacidade de influenciar o comportamento de outra pessoa. As bases\nformais incluem o poder legítimo, decorrente do cargo, o poder de recompensa e o\npoder coercitivo. As bases pessoais incluem o poder de competência, derivado de\nconhecimento técnico reconhecido, e o poder de referência, derivado de admiração\ne identificação. Bases pessoais tendem a produzir comprometimento; bases\ncoercitivas tendem a produzir apenas obediência."

- matrix: 01_matriz_competencias.json, /competencias/4/descricao: "Conduzir processos de comunicação, negociação e mediação de conflitos em equipes de trabalho."

- ementa: 03_ementa_comportamento_organizacional.txt, linhas 30–30: "3. Analisar o efeito de estilos de liderança e de bases de poder sobre a equipe."

Liberado para prova: **não**.

### ITM-20026 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:44, linhas 45–45. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20027 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:45, linhas 46–46. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20028 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:46, linhas 47–47. Motivo: prospective_holdout_excluded.

Liberado para prova: **não**.

### ITM-20029 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:47, linhas 48–48. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20030 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:48, linhas 49–49. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20031 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:49, linhas 50–50. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20032 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:50, linhas 51–51. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20033 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:51, linhas 52–52. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20034 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:52, linhas 53–53. Motivo: prospective_holdout_excluded.

Liberado para prova: **não**.

### ITM-20035 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:53, linhas 54–54. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20036 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:54, linhas 55–55. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20037 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:55, linhas 56–56. Motivo: prospective_holdout_excluded.

Liberado para prova: **não**.

### ITM-20038 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:56, linhas 57–57. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20039 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:57, linhas 58–58. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20040 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:58, linhas 59–59. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20041 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:59, linhas 60–60. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-30007 — ANALISADO (replay)

Origem: 04_itens_legado.csv:60, linhas 61–61. Motivo: recorded_response_replayed.

Estado semântico: abstained

Assunto: Requisitos de validade de negocio juridico.

Tarefa exigida: Reconhecer uma lista de requisitos juridicos entre alternativas; completude normativa nao verificada.

Objeto (outside_provided_scope): nenhum sustentado. Nao existe OC juridico especifico na matriz fornecida. Reconhecer requisitos legais nao exige reconhecer dilema etico ou avaliar impactos de gestao. Ausencia de escopo nao declara invalidade juridica.

Competência (not_established): Nao existe OC juridico especifico na matriz fornecida. Reconhecer requisitos legais nao exige reconhecer dilema etico ou avaliar impactos de gestao. Ausencia de escopo nao declara invalidade juridica. Escopo: Sem inferencia juridica normativa ou aconselhamento.

Vínculos: nenhum

Problemas de uso: Gabarito A preservado como dado; completude legal nao verificada pelas fontes disponiveis.

Regra provisória de nós (separada): 0 nós identificados; 0 pares; estado not_applicable. Nenhum vínculo truncado.

Resposta bruta: [raw_responses/060.json](raw_responses/060.json)

Evidências:

- item: 04_itens_legado.csv:60, enunciado: "Sao requisitos de validade do negocio juridico, nos termos do Codigo Civil:"

- item: 04_itens_legado.csv:60, alternativa_a: "Agente capaz, objeto licito e forma prescrita ou nao defesa em lei"

- matrix: 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/7/nome: "Ética e transparência na informação financeira"

- matrix: 01_matriz_competencias.json, /competencias/5/descricao: "Posicionar-se de forma ética e responsável nas decisões de gestão, considerando impactos sociais e ambientais."

- ementa: 02_ementa_gestao_financeira.txt, linhas 18–18: "diversificação. Ética e transparência na informação financeira."

Liberado para prova: **não**.

### ITM-30008 — ANALISADO (replay)

Origem: 04_itens_legado.csv:61, linhas 62–62. Motivo: recorded_response_replayed.

Estado semântico: abstained

Assunto: Formula do ponto de equilibrio contabil.

Tarefa exigida: Reconhecer a expressao de calculo entre alternativas; nao realizar calculo numerico.

Objeto (outside_provided_scope): nenhum sustentado. Nao existe OC especifico de custo-volume-lucro/ponto de equilibrio na matriz fornecida. Reconhecer formula e uma operacao identificavel, nao um veto por facilidade. OC-GF-04 trata demonstracoes e indicadores, e COMP-03 trata instrumentos de matematica financeira; mera divisao nao estabelece esses aspectos.

Competência (not_established): Nao existe OC especifico de custo-volume-lucro/ponto de equilibrio na matriz fornecida. Reconhecer formula e uma operacao identificavel, nao um veto por facilidade. OC-GF-04 trata demonstracoes e indicadores, e COMP-03 trata instrumentos de matematica financeira; mera divisao nao estabelece esses aspectos. Escopo: Reconhecimento da formula sem OC especifico sustentado.

Vínculos: nenhum

Problemas de uso: Precisao editorial da unidade de ponto de equilibrio deve ser revisada; nao completar o enunciado.

Regra provisória de nós (separada): 0 nós identificados; 0 pares; estado not_applicable. Nenhum vínculo truncado.

Resposta bruta: [raw_responses/061.json](raw_responses/061.json)

Evidências:

- item: 04_itens_legado.csv:61, enunciado: "No calculo do ponto de equilibrio contabil, considera-se:"

- item: 04_itens_legado.csv:61, alternativa_a: "Custos fixos divididos pela margem de contribuicao unitaria"

- matrix: 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/3/nome: "Análise de demonstrações financeiras por indicadores"

- matrix: 01_matriz_competencias.json, /competencias/0/descricao: "Diagnosticar a situação econômico-financeira de uma organização a partir de suas demonstrações contábeis e indicadores."

- ementa: 02_ementa_gestao_financeira.txt, linhas 15–16: "do capital de giro. Análise das demonstrações financeiras por indicadores de\nliquidez, endividamento e rentabilidade. Custo de capital e custo médio"

Liberado para prova: **não**.

### ITM-30009 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:62, linhas 63–63. Motivo: fixture_missing.

Pendências estruturais: MISSING_FIELD (disciplina_informada): "Campo vazio na fonte; não imputado."; MISSING_FIELD (origem_banco): "Campo vazio na fonte; não imputado."

Liberado para prova: **não**.

### ITM-30010 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:63, linhas 64–64. Motivo: prospective_holdout_excluded.

Pendências estruturais: MISSING_FIELD (ano_aplicacao): "Campo vazio na fonte; não imputado."

Liberado para prova: **não**.

### ITM-10073 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:64, linhas 65–65. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20042 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:65, linhas 66–66. Motivo: fixture_missing.

Pendências estruturais: DUPLICATE_ALTERNATIVES (alternativas): [["alternativa_c", "alternativa_d"]]

Liberado para prova: **não**.

### ITM-10074 — PENDENTE — sem análise

Origem: 04_itens_legado.csv:66, linhas 67–67. Motivo: fixture_missing.

Liberado para prova: **não**.

### ITM-20043 — ANALISADO (replay)

Origem: 04_itens_legado.csv:67, linhas 68–68. Motivo: recorded_response_replayed.

Estado semântico: abstained

Assunto: Teorias do comportamento; objeto especifico indeterminavel sem texto-base.

Tarefa exigida: Demanda pretendida: relacionar comportamento do gestor a teoria. Operacao executavel indeterminada: texto acima ausente.

Objeto (indeterminate): nenhum sustentado. Incompletude impede observar comportamento necessario para sustentar OC e competencia. Alternativas e gabarito nao reconstituem texto-base.

Competência (not_established): Incompletude impede observar comportamento necessario para sustentar OC e competencia. Alternativas e gabarito nao reconstituem texto-base. Escopo: Sem inferencia curricular positiva.

Vínculos: nenhum

Problemas de uso: Recuperar texto-base na origem antes de reapreciar.

Regra provisória de nós (separada): 0 nós identificados; 0 pares; estado not_applicable. Nenhum vínculo truncado.

Resposta bruta: [raw_responses/067.json](raw_responses/067.json)

Evidências:

- item: 04_itens_legado.csv:67, enunciado: "Com base no texto acima, qual teoria explica o comportamento do gestor descrito?"

- item: 04_itens_legado.csv:67, alternativa_b: "Teoria Y"

Liberado para prova: **não**.

### ITM-20044 — RESERVADO — sem análise

Origem: 04_itens_legado.csv:68, linhas 69–69. Motivo: prospective_holdout_excluded.

Pendências estruturais: MISSING_FIELD (alternativa_d): "Campo vazio na fonte; não imputado."; MISSING_FIELD (alternativa_e): "Campo vazio na fonte; não imputado."; MISSING_FIELD (gabarito): "Campo vazio na fonte; não imputado."; MISSING_FIELD (origem_banco): "Campo vazio na fonte; não imputado."

Liberado para prova: **não**.