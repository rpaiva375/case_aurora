# Amostra v1 — sugestões para revisão

Apenas seis itens e matriz/duas ementas incorporadas. Amostra não representativa. Sem holdout, fontes externas, métricas de acurácia, confiança calibrada ou validação humana.

Autoria: session_agent_authored. Integração API não executada. Revisão humana pendente.

## ITM-10041 — suggested

Um capital de R$ 12.000,00 foi aplicado a juros simples de 2% ao mes durante 7 meses. Qual o montante ao final do periodo?

- A: R$ 13.680,00
- B: R$ 13.440,00
- C: R$ 12.840,00
- D: R$ 14.000,00
- E: R$ 13.200,00

Gabarito preservado: A

Calcular 12000 × (1 + 0,02 × 7) = 13680 e selecionar A.
Aplicar capitalização simples para obter montante é evidência direta do aspecto de matemática financeira de COMP-03.
Mede resolução de um problema simples (HAB-03.1), não comparação de financiamentos, equivalência de capitais ou domínio integral de COMP-03.

Sugerido: OC-GF-01 → COMP-03. 

- 04_itens_legado.csv:1, enunciado: «Um capital de R$ 12.000,00 foi aplicado a juros simples de 2% ao mes durante 7 meses. Qual o montante ao final do periodo?»
- 04_itens_legado.csv:1, alternativa_a: «R$ 13.680,00»
- 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/0/nome: «Valor do dinheiro no tempo: capitalização simples e composta»
- 01_matriz_competencias.json, /competencias/2/descricao: «Aplicar instrumentos de matemática financeira na análise de operações de crédito, investimento e financiamento.»
- 01_matriz_competencias.json, /competencias/2/habilidades/0/descricao: «Resolver problemas de capitalização simples e composta e de equivalência de capitais.»
- 02_ementa_gestao_financeira.txt, linhas 38–40: «1.1 Capitalização simples e composta
No regime de juros simples, os juros incidem sempre sobre o capital inicial, de
modo que o montante cresce linearmente: M = C x (1 + i x n). No regime de juros»


## ITM-20018 — suggested

Uma equipe de suporte tecnico apresenta alta rotatividade. A pesquisa interna aponta salarios compativeis com o mercado, mas ausencia de reconhecimento e de perspectiva de crescimento. A luz da teoria dos dois fatores de Herzberg, qual interpretacao e correta?

- A: Os fatores higienicos estao insatisfatorios e causam a rotatividade
- B: Os fatores motivacionais estao ausentes, o que explica a insatisfacao apesar da remuneracao adequada
- C: A remuneracao e o unico fator motivacional relevante
- D: A teoria nao se aplica a equipes tecnicas
- E: A rotatividade decorre exclusivamente de fatores externos

Gabarito preservado: B

Distinguir fatores higiênicos de motivacionais e aplicar a distinção à situação para escolher B.
Interpretar remuneração adequada e ausência de reconhecimento/crescimento por Herzberg exige explicar comportamento no trabalho por teoria motivacional, aspecto explícito de COMP-04/HAB-04.1.
Interpretação localizada; não demonstra decisão de gestão, diagnóstico completo de clima ou toda COMP-04.

Sugerido: OC-CO-02 → COMP-04. 

- 04_itens_legado.csv:36, enunciado: «Uma equipe de suporte tecnico apresenta alta rotatividade. A pesquisa interna aponta salarios compativeis com o mercado, mas ausencia de reconhecimento e de perspectiva de crescimento. A luz da teoria dos dois fatores de Herzberg, qual interpretacao e correta?»
- 04_itens_legado.csv:36, alternativa_b: «Os fatores motivacionais estao ausentes, o que explica a insatisfacao apesar da remuneracao adequada»
- 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/1/nome: «Motivação no trabalho: teorias de conteúdo e de processo»
- 01_matriz_competencias.json, /competencias/3/descricao: «Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas.»
- 01_matriz_competencias.json, /competencias/3/habilidades/0/descricao: «Explicar comportamentos no trabalho a partir de teorias de motivação, percepção e atitudes.»
- 03_ementa_comportamento_organizacional.txt, linhas 69–75: «razoavelmente atendido. A teoria dos dois fatores, de Herzberg, distingue fatores
higiênicos — salário, condições de trabalho, políticas da empresa, supervisão —,
cuja ausência gera insatisfação mas cuja presença não motiva, dos fatores
motivacionais — reconhecimento, responsabilidade, conteúdo do trabalho,
crescimento —, que atuam sobre a satisfação e o esforço. A consequência prática é
que corrigir apenas fatores higiênicos remove insatisfação sem produzir
engajamento.»

Rejeitado: OC-CO-07 → COMP-04. A pesquisa interna é contexto; não exige diagnóstico de cultura ou clima.

- 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/6/nome: «Cultura e clima organizacional»

Pendência: A alternativa B usa insatisfacao para ausência de motivadores; a ementa distingue ausência de satisfação de insatisfação por fatores higiênicos. Revisar precisão teórica e validade do gabarito, que foi preservado.

## ITM-20025 — abstained

Um gerente recem-promovido obtem adesao da equipe principalmente porque os colaboradores admiram sua trajetoria tecnica e desejam ser associados a ele. Qual base de poder predomina?

- A: Poder legitimo
- B: Poder de referencia
- C: Poder de recompensa
- D: Poder coercitivo
- E: Poder de especialista

Gabarito preservado: B

Reconhecer admiração/identificação como poder de referência (B), distinguindo conhecimento técnico (E).
A demanda é reconhecer uma base de poder; não avaliar efeitos de estilos de liderança ou sustentar decisões. Correspondência temática com OC-CO-04 não basta para COMP-04 ou COMP-05.
Pode evidenciar compreensão do conceito do OC, mas a rubrica não converte automaticamente isso em par com competência ampla.

Rejeitado: OC-CO-04 → COMP-04. Não exige avaliar efeito da liderança nos resultados ou engajamento.

- 04_itens_legado.csv:43, enunciado: «Um gerente recem-promovido obtem adesao da equipe principalmente porque os colaboradores admiram sua trajetoria tecnica e desejam ser associados a ele. Qual base de poder predomina?»
- 04_itens_legado.csv:43, alternativa_b: «Poder de referencia»
- 04_itens_legado.csv:43, alternativa_e: «Poder de especialista»
- 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/3/nome: «Liderança e poder nas organizações»
- 01_matriz_competencias.json, /competencias/3/descricao: «Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas.»
- 01_matriz_competencias.json, /competencias/3/habilidades/2/descricao: «Avaliar o efeito de estilos de liderança sobre resultados e sobre o engajamento da equipe.»
- 03_ementa_comportamento_organizacional.txt, linhas 118–124: «3.2 Bases de poder
Poder é a capacidade de influenciar o comportamento de outra pessoa. As bases
formais incluem o poder legítimo, decorrente do cargo, o poder de recompensa e o
poder coercitivo. As bases pessoais incluem o poder de competência, derivado de
conhecimento técnico reconhecido, e o poder de referência, derivado de admiração
e identificação. Bases pessoais tendem a produzir comprometimento; bases
coercitivas tendem a produzir apenas obediência.»

Rejeitado: OC-CO-04 → COMP-05. Não exige conduzir comunicação, negociação ou mediação.

- 01_matriz_competencias.json, /competencias/4/descricao: «Conduzir processos de comunicação, negociação e mediação de conflitos em equipes de trabalho.»

Pendência: Trajetoria tecnica também evoca poder de especialista; identificação favorece B. Revisão humana deve decidir se a classificação localizada é evidência suficiente de COMP-04.

## ITM-20043 — abstained

Com base no texto acima, qual teoria explica o comportamento do gestor descrito?

- A: Teoria X
- B: Teoria Y
- C: Teoria dos dois fatores
- D: Teoria da expectancia
- E: Teoria da equidade

Gabarito preservado: B

Pretende relacionar comportamento de gestor a uma teoria; estímulo necessário ausente.
O texto acima não está no item fornecido. Sem comportamento descrito, não é possível determinar a operação interpretativa nem justificar o vínculo.
O gabarito B não permite reconstruir o estímulo ou aferir competência.

Rejeitado: OC-CO-02 → COMP-04. Alternativas citam teorias, mas falta o caso para sustentar aplicação.

- 04_itens_legado.csv:67, enunciado: «Com base no texto acima, qual teoria explica o comportamento do gestor descrito?»
- 04_itens_legado.csv:67, alternativa_b: «Teoria Y»
- 01_matriz_competencias.json, /componentes_curriculares/1/objetos_conhecimento/1/nome: «Motivação no trabalho: teorias de conteúdo e de processo»
- 01_matriz_competencias.json, /competencias/3/descricao: «Analisar o comportamento de indivíduos e grupos no contexto organizacional para sustentar decisões de gestão de pessoas.»
- 03_ementa_comportamento_organizacional.txt, linhas 65–75: «2.1 Teorias de conteúdo
As teorias de conteúdo tratam do que motiva. A hierarquia de necessidades de
Maslow organiza necessidades em cinco níveis, dos fisiológicos à autorrealização,
sob a premissa de que um nível se torna relevante quando o anterior está
razoavelmente atendido. A teoria dos dois fatores, de Herzberg, distingue fatores
higiênicos — salário, condições de trabalho, políticas da empresa, supervisão —,
cuja ausência gera insatisfação mas cuja presença não motiva, dos fatores
motivacionais — reconhecimento, responsabilidade, conteúdo do trabalho,
crescimento —, que atuam sobre a satisfação e o esforço. A consequência prática é
que corrigir apenas fatores higiênicos remove insatisfação sem produzir
engajamento.»

Pendência: Recuperar texto-base na origem antes de reapreciar.

## ITM-30007 — abstained

Sao requisitos de validade do negocio juridico, nos termos do Codigo Civil:

- A: Agente capaz, objeto licito e forma prescrita ou nao defesa em lei
- B: Apenas agente capaz
- C: Apenas objeto licito
- D: Registro em cartorio em qualquer hipotese
- E: Anuencia do Ministerio Publico

Gabarito preservado: A

Selecionar a lista de requisitos legais indicada em A; não aplicar a um caso de gestão.
Reconhecer requisitos legais de validade de negócio jurídico não encontra OC jurídico na matriz fornecida; não implica decisão ética de gestão.
Não houve consulta jurídica externa nem validação da completude legal da alternativa. Escopo limitado às duas ementas e à matriz do packet.

Rejeitado: OC-GF-08 → COMP-06. Legalidade de negócio jurídico não é evidência de ética/transparência financeira.

- 04_itens_legado.csv:60, enunciado: «Sao requisitos de validade do negocio juridico, nos termos do Codigo Civil:»
- 04_itens_legado.csv:60, alternativa_a: «Agente capaz, objeto licito e forma prescrita ou nao defesa em lei»
- 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/7/nome: «Ética e transparência na informação financeira»
- 01_matriz_competencias.json, /competencias/5/descricao: «Posicionar-se de forma ética e responsável nas decisões de gestão, considerando impactos sociais e ambientais.»
- 02_ementa_gestao_financeira.txt, linhas 18–18: «diversificação. Ética e transparência na informação financeira.»


## ITM-30008 — abstained

No calculo do ponto de equilibrio contabil, considera-se:

- A: Custos fixos divididos pela margem de contribuicao unitaria
- B: Receita total menos custo variavel total
- C: Lucro operacional dividido pelo ativo total
- D: Custos variaveis divididos pelo preco de venda
- E: Margem bruta menos despesas administrativas

Gabarito preservado: A

Reconhecer custos fixos divididos pela margem de contribuição unitária (A), sem cálculo numérico ou diagnóstico.
Reconhecer fórmula de ponto de equilíbrio não exige diagnosticar demonstrações/indicadores, e não há OC de custo-volume-lucro na matriz.
Proximidade com finanças não transforma recordação de fórmula em diagnóstico econômico-financeiro.

Rejeitado: OC-GF-04 → COMP-01. Não requer interpretar demonstrações nem comparar indicadores financeiros.

- 04_itens_legado.csv:61, enunciado: «No calculo do ponto de equilibrio contabil, considera-se:»
- 04_itens_legado.csv:61, alternativa_a: «Custos fixos divididos pela margem de contribuicao unitaria»
- 01_matriz_competencias.json, /componentes_curriculares/0/objetos_conhecimento/3/nome: «Análise de demonstrações financeiras por indicadores»
- 01_matriz_competencias.json, /competencias/0/descricao: «Diagnosticar a situação econômico-financeira de uma organização a partir de suas demonstrações contábeis e indicadores.»
- 02_ementa_gestao_financeira.txt, linhas 15–16: «do capital de giro. Análise das demonstrações financeiras por indicadores de
liquidez, endividamento e rentabilidade. Custo de capital e custo médio»

