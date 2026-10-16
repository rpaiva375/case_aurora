# Case Aurora — decisões e limites da etapa 1

## Autorização do usuário

- Implementar ingestão e padronização dos sete arquivos, preservar originais e identificar cada transformação e sua regra.
- Manter desempenho e histórico de aplicação separados para evitar multiplicação das contagens.
- Gabaritos numéricos continuam pendentes: não assumir `1 = A` ou `2 = B`.
- IDs sem hífen podem ser padronizados após verificar colisões; observações de diferentes semestres devem permanecer separadas.
- Entregar base, pendências e verificações de integridade; solicitar revisão por outro agente.
- Não implementar tela, busca avançada nem mapeamento nesta etapa.

## Tipos de evidência

1. **Verificação técnica:** reconciliação com fontes, hashes, regras, chaves, tipos, preservação e contagens. Não comprova mérito pedagógico.
2. **Revisão do usuário:** conferência de coerência de uma futura sugestão diante da matriz e das evidências. Não deve ser rotulada como validação pedagógica especializada.
3. **Validação pedagógica especializada:** exige pessoa habilitada para julgar conteúdo e adequação avaliativa. Não foi realizada nesta etapa nem será inferida da revisão do usuário.
4. **Fixtures de teste:** dados artificiais criados para testar falhas técnicas. Seus resultados não medem qualidade do acervo ou das sugestões.

## Ambiguidade de “1–3 nós”: exemplo estrutural concreto

Fonte: `01_matriz_competencias.json`, `regras_de_vinculo` e objetos `OC-GF-05` e `OC-GF-06`.

Considere uma futura proposta contendo os objetos **OC-GF-05** (custo de capital) e **OC-GF-06** (VPL, TIR e payback), com as relações permitidas pela matriz:

- OC-GF-05 → COMP-02.
- OC-GF-06 → COMP-02.
- OC-GF-06 → COMP-03.

Este é somente um exemplo de interpretação da regra usando entidades reais. Não é um mapeamento realizado, uma indicação de que qualquer questão avalia esses três vínculos, nem evidência de qualidade.

- **Contar objetos e competências como nós distintos:** 2 objetos + 2 competências = **4 nós**, acima do máximo 3; proposta recusada pelo limite.
- **Contar cada par objeto–competência como uma unidade:** **3 pares**, dentro do máximo; proposta passa nesse critério estrutural.
- **Contar somente objetos, com competências como atributos dos vínculos:** **2 objetos**, dentro do máximo; proposta passa nesse critério estrutural.

Outro caso mostra uma diferença entre as duas últimas interpretações: OC-GF-03 vinculado a COMP-01 e COMP-03, junto com OC-GF-06 vinculado a COMP-02 e COMP-03, dá **4 pares** (excede), **2 objetos** (não excede) e **5 nós distintos** (excede).

Passar no limite estrutural não implica aprovação pedagógica. A ingestão preserva a regra original e não escolhe silenciosamente uma interpretação. Habilidades também não serão contadas nem vinculadas automaticamente.

## Pergunta preparada para a Coordenadora de Avaliação

> Na matriz, o limite de 1 a 3 nós por item conta objetos de conhecimento, o conjunto de objetos e competências distintos, ou cada par objeto–competência? Por exemplo, os vínculos OC-GF-05→COMP-02 e OC-GF-06→COMP-02/COMP-03 resultam em 2 objetos, 4 nós distintos ou 3 pares. Qual contagem devemos aplicar? Habilidades entram nesse limite? E a competência precisa constar na lista do objeto específico ou basta pertencer ao componente curricular? Até sua definição, manteremos essa validação pendente, sem impedir a ingestão.

Pergunta preparada, **não enviada**. Não há autorização para contato externo.

## O que permanece fora das conclusões

- Não há medição de economia de tempo, ganho operacional ou qualidade de sugestões.
- Não há classificação semântica, deduplicação pedagógica, aprovação de questões ou cobertura validada.
- Estatísticas negativas, repetição de aplicação e relatos de revisores são sinais ou observações, não comprovação automática de defeito, vazamento ou causalidade.
- As proporções da amostra sintética não serão extrapoladas para os 240 mil itens do contexto.
