# Mapeamento: amostra de desenvolvimento e reserva de avaliação

## Escopo autorizado

Esta rodada cobre somente seis itens. Não amplia o mapeamento para os 68 itens, não corrige o acervo, não cria tela e não executa API paga. Os dados de ingestão permanecem intactos.

A amostra proposital contém cálculo contextualizado, interpretação organizacional, potencial ambiguidade, contexto ausente e duas fronteiras do escopo. Razões de seleção não são rótulos corretos nem resultados esperados. Ela serve para discutir o raciocínio; não estima a qualidade na população.

## Separação antes da inferência

`prepare_sample.py` congelou `mapping/split.json` e `mapping/sample_packet.json` antes da autoria das sugestões. O manifesto contém 6 IDs de desenvolvimento, 8 reservados e 54 ainda não atribuídos, sem interseção. Os registros reservados têm hash, não rótulo de competência ou decisão semântica. Não se mudará a reserva para melhorar um resultado.

Os agentes de mapeamento e crítica foram iniciados sem histórico da conversa. Receberam somente o pacote com seis itens e as referências curriculares comuns. Foram instruídos a não consultar o corpus, a fila de revisão, estatísticas, histórico de aplicação ou a reserva. O compartilhamento de filesystem não é uma barreira técnica de acesso: o isolamento nesta etapa é por instrução e registro das fontes consultadas.

**Limite:** o manager e agentes anteriores já inspecionaram o acervo. Esta é uma reserva prospectiva contra uso em ajustes semânticos iniciais, não uma avaliação retrospectivamente cega. A seleção não é aleatória nem estatisticamente representativa. Os oito itens não serão usados como exemplos de prompt, para escolher regras ou para revisar as sugestões desta primeira amostra.

## Sugestão e regra são artefatos diferentes

- `suggestions_v1.json`: inferência dos agentes; conserva pares propostos, evidências, abstenções, motivos e candidatos rejeitados. A v1 é preservada para comparação com a crítica.
- `rule_checks_v1.json`: checagem determinística separada.
- Premissa provisória adotada pelo manager para esta rodada: contar **OC e COMP distintos**, mínimo 1 e máximo 3; habilidades citadas são apenas evidência e não entram nessa contagem. Validar COMP contra a lista específica do OC é também uma premissa conservadora provisória.
- A autorização do usuário é para trabalhar com premissa explícita; a interpretação escolhida não deve ser atribuída a ele ou à Coordenadora.
- Candidatos rejeitados não entram na contagem. Abstenções têm checagem de quantidade `not_applicable`.
- Exceder o limite não elimina nem corta vínculos; gera `review_required`. O relatório já inclui contagem de pares, objetos e competências para permitir reinterpretação sem nova inferência. Uma fixture sintética verifica essa retenção; não é questão do acervo.

## Crítica e revisão humana

O segundo agente critica as evidências e a demanda da questão. Concordância entre agentes não cria um rótulo de referência e não é uma métrica de qualidade pedagógica. Divergências permanecerão visíveis, sem votos ou aprovação por maioria de IAs.

A revisão do usuário avalia coerência e suficiência das justificativas diante das fontes. Será registrada separadamente da validação pedagógica especializada. Uma questão pode ter vínculo curricular plausível e, simultaneamente, gabarito ou construção inadequados. Mapeável não significa apta para aplicação.

## Avaliação posterior da reserva

1. Após a revisão desta amostra pelo usuário, congelar a próxima versão de rubrica, regras, contrato de saída e forma de geração/provedor antes de abrir a reserva para inferência.
2. Rodar uma vez nos oito itens, conservando entradas, saídas, falhas, abstenções e uso/custo real quando houver API. Não selecionar apenas respostas favoráveis.
3. Obter revisão de coerência do usuário e, separadamente, avaliação de especialista pedagógico com critérios registrados. Idealmente, o especialista forma sua referência sem ver a sugestão primeiro; divergências devem ser adjudicadas e não resolvidas por outra IA.
4. Contar sugestões aceitas sem alteração, corrigidas, rejeitadas e abstenções consideradas adequadas/inadequadas, com denominador explícito e a categoria de revisor. Sem referência humana, acurácia permanece **não medida**.
5. Depois que a reserva for vista e usada para corrigir o método, ela deixa de ser inédita para a versão seguinte. Novas alegações de generalização exigirão outra amostra.

## Benefício operacional ainda a medir

O teste atual verifica se uma pessoa consegue inspecionar o raciocínio e a fonte. Não mede economia de tempo. Um piloto futuro deverá registrar tempo por tarefa, retrabalho, decisões e erros com/sem apoio, com desenho que reduza efeito de familiaridade entre itens comparáveis. A taxa de abstenção desta pequena amostra não é estimativa de produtividade nem taxa de erro.
