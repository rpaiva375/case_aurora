# Demo dos três caminhos

**Demonstração do agente: não contém decisões do usuário nem validação pedagógica.**

Reutiliza respostas gravadas. Não gera inferência, não envia mensagens e não faz chamadas de API.

## Sugestão: ITM-10041

Estado semântico: `suggested`.

> Um capital de R$ 12.000,00 foi aplicado a juros simples de 2% ao mes durante 7 meses. Qual o montante ao final do periodo?

Justificativa preservada: Resolver capitalizacao simples e parte textual explicita de HAB-03.1. A operacao e simples, mas executa a habilidade, nao apenas um pre-requisito; nao exige demonstrar capitalizacao composta ou toda COMP-03.

Vínculo sugerido: OC-GF-01 → COMP-03; habilidades: HAB-03.1.

Referência: 01_matriz_competencias.json (/componentes_curriculares/0/objetos_conhecimento/0/nome):

> Valor do dinheiro no tempo: capitalização simples e composta

Referência: 01_matriz_competencias.json (/competencias/2/descricao):

> Aplicar instrumentos de matemática financeira na análise de operações de crédito, investimento e financiamento.

Referência: 01_matriz_competencias.json (/competencias/2/habilidades/0/descricao):

> Resolver problemas de capitalização simples e composta e de equivalência de capitais.

Referência: 02_ementa_gestao_financeira.txt (linhas 38–40):

> 1.1 Capitalização simples e composta
> No regime de juros simples, os juros incidem sempre sobre o capital inicial, de
> modo que o montante cresce linearmente: M = C x (1 + i x n). No regime de juros

Estado observado: `analyzed`. Motivo: `recorded_response_replayed`.

Demonstração: encaminhar a sugestão parcial e suas evidências à revisão especializada; não liberar para prova.

Evento: [f08963ba9e9946318cc27dc43be6b9c4.json](events/f08963ba9e9946318cc27dc43be6b9c4.json). Evidências e origem: [ITM-10041.json](ITM-10041.json).

A pendência permanece aberta; nenhum conteúdo ou vínculo é alterado pelo evento.

## Abstenção: ITM-30007

Estado semântico: `abstained`.

> Sao requisitos de validade do negocio juridico, nos termos do Codigo Civil:

Justificativa preservada: Nao existe OC juridico especifico na matriz fornecida. Reconhecer requisitos legais nao exige reconhecer dilema etico ou avaliar impactos de gestao. Ausencia de escopo nao declara invalidade juridica.

Referência: 01_matriz_competencias.json (/componentes_curriculares/0/objetos_conhecimento/7/nome):

> Ética e transparência na informação financeira

Referência: 01_matriz_competencias.json (/competencias/5/descricao):

> Posicionar-se de forma ética e responsável nas decisões de gestão, considerando impactos sociais e ambientais.

Referência: 02_ementa_gestao_financeira.txt (linhas 18–18):

> diversificação. Ética e transparência na informação financeira.

Estado observado: `analyzed`. Motivo: `recorded_response_replayed`.

Demonstração: encaminhar ao responsável pelo componente jurídico para conferir o recorte curricular; não descartar nem aprovar o item.

Evento: [1ba9d6c160b0470fa33650d8c337fb98.json](events/1ba9d6c160b0470fa33650d8c337fb98.json). Evidências e origem: [ITM-30007.json](ITM-30007.json).

A pendência permanece aberta; nenhum conteúdo ou vínculo é alterado pelo evento.

## Pendência: ITM-10048

Estado semântico: `not_analyzed`.

> O que e capital de giro?

Gabarito bruto: `2`; padronizado: `null`. Regra: `ANSWER_UNRESOLVED`. A convenção numérica precisa de confirmação na origem.

Estado observado: `pending`. Motivo: `fixture_missing`.

Demonstração: solicitar à origem confirmação da convenção do gabarito numérico; preservar 2 bruto e nulo padronizado até evidência documentada.

Evento: [461bd857fcca4896a13557e44ee93e74.json](events/461bd857fcca4896a13557e44ee93e74.json). Evidências e origem: [ITM-10048.json](ITM-10048.json).

A pendência permanece aberta; nenhum conteúdo ou vínculo é alterado pelo evento.

## O que foi demonstrado

Três encaminhamentos demonstrativos; 88 arquivos protegidos comparados; preservação: True.

Zero pendências substantivamente resolvidas. Não medimos tempo humano, qualidade pedagógica ou economia operacional.
