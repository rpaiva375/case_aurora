# Provedor, custo e natureza da demonstração

Atualização da rodada v2: [conferência de disponibilidade e aritmética](confirmacao_api_2026-10-14.md).
A conta central de US$ 0,72 abaixo é de **duas passagens**. O fluxo mínimo proposto
usa uma passagem por item: US$ 0,36 sob as mesmas hipóteses por chamada. Catálogo
público confirmado; acesso na conta não verificado. O usuário **não autorizou gasto**.

## O que foi autorizado e executado nesta rodada

As sugestões da amostra são produzidas por agentes de IA desta sessão do Codex e salvas como `session_agent_authored`. Não são respostas de uma integração API executada pelo projeto. Não se atribui a elas o modelo de API proposto abaixo: o alias/snapshot exato dos agentes não foi registrado pela interface de execução como evidência verificável.

Não houve chamada paga de API do pipeline, leitura de chaves nem instalação de cliente de API. O gasto adicional de API executado pelo projeto é **US$ 0**; o custo ou a cota da própria sessão do usuário não foi medido e não deve ser descrito como gratuito.

Não há mock gerando estas sugestões: há inferência real dos agentes sobre seis itens do pacote fictício. Reexecutar o validador apenas confere respostas salvas; **não é uma nova execução de IA**. Fixtures sintéticas testam somente regras de software, separadas das sugestões do caso.

Ainda não foram testados pelo pipeline: integração com provedor, repetibilidade de inferência, custo real em tokens, latência, limites de API, qualidade em itens reservados, validação pedagógica e ganho operacional.

## Opção proposta para futuro piloto com API — ainda não executada

Provedor: **OpenAI**, modelo **gpt-5.6-terra**, por Responses API, exclusivamente para o pacote sintético do case. É uma opção para experimentar custo/qualidade, não um resultado de benchmark desta tarefa. As páginas dos modelos GPT-4.1 mini e GPT-5 mini consultadas estão marcadas como deprecated; a documentação do GPT-5 mini aponta GPT-5.6 Terra para novos fluxos desse tipo.

Preços consultados em 14/10/2026: **US$ 2 por milhão de tokens de entrada** e **US$ 12 por milhão de tokens de saída**. Fonte oficial: https://developers.openai.com/api/docs/models/gpt-5.6-terra . As requisições planejadas ficariam abaixo do limiar de contexto longo. Não se presume desconto de cache, batch ou promoção.

Estimativa de planejamento, não consumo medido:

- 6 itens × 2 passagens (sugestão e crítica) = 12 chamadas.
- Hipótese central: 12 mil tokens de entrada e 3 mil tokens de saída faturada por chamada, incluindo eventual raciocínio faturável.
- Entrada: 144.000 / 1.000.000 × US$ 2 = **US$ 0,288**.
- Saída: 36.000 / 1.000.000 × US$ 12 = **US$ 0,432**.
- Total central: **US$ 0,72**.
- Faixa com 10–20 mil tokens de entrada e 2–4 mil de saída por chamada: **US$ 0,528–1,056**. Uma repetição integral dobraria essa faixa.
- Proposta de teto para esse piloto: **US$ 3**, sem chamadas automáticas além do teto. Esse controle ainda não está implementado; o valor não constitui autorização de gasto.

O número de tokens é uma premissa, não contagem feita pelo tokenizer do provedor. Custos do plano Codex, câmbio, tributos e revisão humana não estão incluídos. Antes de executar, será necessário confirmar orçamento, disponibilidade do modelo na conta, limites de saída e interrupção de novas chamadas por orçamento.

## Produção Aurora

A restrição do case impede que enunciados reais saiam do perímetro da Aurora. A opção de API pública acima **não é uma proposta aprovada para produção**. O motor de produção terá de executar dentro do perímetro aprovado; provedor, infraestrutura e custo desse ambiente continuam indefinidos. O pacote do case é explicitamente fictício.
