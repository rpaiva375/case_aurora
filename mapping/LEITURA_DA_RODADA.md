# Leitura da primeira rodada, após crítica

Este documento é a síntese do manager para revisão do usuário. Não altera `suggestions_v1.json`, não decide em nome do usuário e não constitui validação pedagógica especializada. Consulte em conjunto `amostra_v1.md` e `review/critica_v1.md`.

## Duas sugestões, quatro abstenções — estados provisórios

- **ITM-10041:** sugestão OC-GF-01 → COMP-03 sustentada pelas evidências disponíveis. O aluno precisa aplicar juros simples e obter R$ 13.680,00; HAB-03.1 e a fórmula da ementa dão suporte. Evidência parcial de competência, não domínio integral. Revisão do usuário e especialista não realizadas.
- **ITM-20018:** sugestão OC-CO-02 → COMP-04 **com ressalva de validade da resposta**. O aluno precisa interpretar ausência de reconhecimento/crescimento à luz de Herzberg; isso sustenta o aspecto de HAB-04.1. Contudo, B atribui “insatisfação” à ausência de motivadores, distinção contestada pela ementa; salário adequado também não assegura adequação de todos os fatores higiênicos. A formulação da v1 “para escolher B” não deve ser lida como confirmação de correção. Preservamos B como dado, sem endossá-la. Não usar o acerto do item como prova de competência validada.
- **ITM-20025:** **abstenção contestada**. O autor considerou reconhecimento de base de poder insuficiente para COMP-04. O revisor apontou possível exigência excessiva de HAB-04.3 integral, enquanto outros itens foram aceitos por evidência parcial. OC-CO-04 é candidato diretamente sustentado pela situação, mas a suficiência do par com COMP-04 e a ambiguidade referência/especialista seguem para discussão. Não adicionamos o vínculo por votação entre IAs.
- **ITM-20043:** abstenção por contexto ausente. Não inferir texto-base a partir de Teoria Y/gabarito B. Recuperar o estímulo antes de propor vínculo efetivamente avaliado.
- **ITM-30007:** abstenção por falta de suporte no recorte dos dois componentes. Requisitos jurídicos não serão equiparados automaticamente a ética. Isso não declara o item inválido em outra matriz.
- **ITM-30008:** abstenção por escopo/demanda. Reconhecer fórmula de ponto de equilíbrio não demonstra diagnóstico financeiro; a matriz não oferece OC específico de custo-volume-lucro. Mantém-se a possibilidade de revisão curricular, sem forçar enquadramento.

Contagens acima descrevem decisões desta amostra intencional. Não são taxa de acerto, produtividade, precisão ou estimativa para o acervo.

## Regra provisória

Sugestões e limite de nós estão separados. Com a interpretação provisória OC+COMP distintos, cada uma das duas sugestões tem 2 nós; nas abstenções, a regra é não aplicável. Nada foi cortado para passar. O teste acima de 3 nós usa fixture artificial e demonstra só retenção técnica. O limite é alterável na função independente `check_rules`, ainda sem configuração externa; não exige refazer a inferência.

## O que a revisão humana pode decidir agora

- A justificativa de cada par está apoiada na operação exigida do aluno, em vez de apenas compartilhar assunto?
- O limiar de evidência parcial precisa ser ajustado de modo consistente, especialmente no ITM-20025?
- A apresentação separa claramente vínculo plausível de questão apta para aplicação, especialmente no ITM-20018?

Essas são perguntas para revisão de coerência pelo usuário. A confirmação pedagógica especializada continua pendente e terá registro próprio.

## Evidência de execução e limites

As sugestões foram autoradas por IA nesta sessão; não são mock, mas também não são resultado de um cliente de API integrado ao projeto. O materializador `build_sample_v1.py` contém a resposta literal para preservar/reproduzir o artefato; reexecutá-lo não executa IA. Validação de citações não mede pertinência semântica. O revisor checou pertinência como outra IA, não como especialista humano.

A v1 informa `started_at=18:51:00Z` como aproximado, mas esse valor não foi capturado pelo relógio de execução do agente e antecede sua delegação. **Não deve ser usado como timestamp verificado nem para calcular esforço.** Mantivemos a resposta original e registramos aqui a ressalva de metadado; o fim foi registrado na materialização. O controle de esforço usa o início observado pelo manager e provisões explícitas, não esse início estimado.

Os oito reservados não foram fornecidos aos agentes de mapeamento/crítica. A exposição prévia do acervo no diagnóstico limita qualquer alegação de cegamento; ver `../docs/protocolo_amostra.md`.
