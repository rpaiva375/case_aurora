# Conferência de modelo e orçamento — 14/10/2026

**Nenhuma autorização de gasto. Nenhuma inferência paga realizada pelo projeto.** Esta conferência usou documentação pública oficial e aritmética local com Decimal; não usou credenciais.

## O que foi confirmado

A documentação oficial lista **gpt-5.6-terra**, endpoint Responses e saída estruturada. O catálogo informa suporte nos níveis pagos apresentados e não no nível Free. Portanto, a oferta pública está documentada; **a disponibilidade na conta/projeto do usuário não foi confirmada**. Não houve teste autenticado nem chamada de inferência. Limites da organização devem ser conferidos na conta antes de executar.

Fontes consultadas:

- [Modelo e preços](https://developers.openai.com/api/docs/models/gpt-5.6-terra).
- [Tabela oficial de preços](https://developers.openai.com/api/docs/pricing).
- [Limites por conta e organização](https://developers.openai.com/api/docs/guides/rate-limits).

Tarifa base consultada: entrada **US$ 2/1 milhão de tokens**, saída **US$ 12/1 milhão**. A estimativa usa requisições de contexto curto e processamento padrão, sem ferramentas cobradas, descontos ou cache-write solicitado. A tarifa e disponibilidade precisam de nova conferência na data da execução.

## Cálculo conferido da estimativa anterior

Hipóteses: 6 itens × 2 passagens = 12 chamadas; 12.000 tokens de entrada e 3.000 tokens de saída faturável por chamada. Saída inclui eventual raciocínio faturado; isso não é contagem medida nem garantia de suficiência.

- Entrada: 12 × 12.000 × 2 / 1.000.000 = **US$ 0,288**.
- Saída: 12 × 3.000 × 12 / 1.000.000 = **US$ 0,432**.
- Total: **US$ 0,720**. A conta anterior está correta sob essas premissas.
- Hipóteses de 10–20 mil tokens de entrada e 2–4 mil de saída: **US$ 0,528–1,056** pelas 12 chamadas.
- Uma repetição integral: **US$ 1,056–2,112** nessa faixa, não US$ 0,72 garantido.

O fluxo mínimo agora proposto precisa apenas de **uma passagem por item**, com revisão humana posterior: 6 chamadas, estimativa central **US$ 0,360**, faixa **US$ 0,264–0,528**. Uma segunda passagem de crítica por IA é opcional e retorna à estimativa anterior. Isso não inclui revisão humana ou comprova qualidade.

O teto de **US$ 3** segue apenas como proposta para piloto e repetições controladas, **não autorização nem controle já implementado**. Tokens efetivos, saída truncada, raciocínio adicional, impostos, câmbio, plano Codex e configurações diferentes podem alterar o gasto. O futuro cliente deve impor limites de entrada/saída e reservar orçamento antes de cada chamada; um teto escrito no documento não o impõe.

## Estado do projeto

- Sugestões dos agentes: reais como análise da sessão, não como execução do cliente API proposto.
- Validações locais: executáveis, mas não geram inferência nova.
- Provedor mock/replay no fluxo ponta a ponta: **proposto, não implementado nesta rodada**.
- Provedor real no fluxo ponta a ponta: **proposto, não implementado nem testado nesta rodada**.
- Disponibilidade autenticada na conta, latência, custo real e qualidade do modelo proposto: **não medidos**.

Produção com enunciados reais da Aurora não está autorizada a usar API pública externa pelo case; a seleção de ambiente interno continua pendente.
