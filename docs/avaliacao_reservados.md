# Proposta de avaliação dos oito reservados — ainda não executada

**Atualização:** proposta histórica abaixo. A rodada foi posteriormente autorizada e executada em 15/10/2026; consulte `../evaluation/LEIA-ME.md` e `../evaluation/CONFERENCIA_v2.md`. A conferência do usuário permanece pendente. Nenhuma chamada de API paga.

Objetivo: descobrir se sugestões novas ajudam a conferir evidências e encaminhar pendências. Não estimar qualidade pedagógica por concordância entre agentes, nem por aprovação de coerência do usuário.

## Antes de abrir os itens

Preparar uma rubrica de avaliação derivada da v2, retirando somente instruções específicas dos seis exemplos e suas decisões literais. Preservar o critério de objeto/tarefa/problemas de uso, evidência parcial e abstenção. Revisar e congelar essa versão antes de abrir os oito; guardar o diff para não ocultar alterações de critério. O prompt v2 atual é específico dos seis e não deve ser aplicado literalmente aos oito.

Congelar hashes dessa rubrica, matriz/ementas, contrato, código e lista reservada. Registrar provedor, modelo quando identificável, data e configuração. Os oito já foram separados prospectivamente; diagnóstico anterior teve contato com o acervo, portanto não são um teste retrospectivamente cego nem uma amostra representativa.

Não usar os oito em ajustes iniciais. Gerar uma única rodada para todos, preservar respostas brutas, falhas e abstenções. Não substituir respostas ruins por novas tentativas silenciosas. Correções posteriores formam uma nova versão; após inspeção esses itens deixam de ser inéditos para ajustes futuros.

## Como obter sugestões novas

O comando atual só faz replay e continuará excluindo os reservados. Não reutilizar suas respostas para apresentar uma avaliação nova.

Opção sem contratação de API: uma rodada futura explicitamente autorizada a agentes da sessão, recebendo somente os oito itens e o currículo/rubrica congelados, sem decisões humanas ou sugestões anteriores. Isso é inferência nova da sessão, não mock, mas continua fora do cliente de inferência do projeto; não demonstra desempenho de um provedor de API nem tem custo/cota Codex medido.

Opção integrada futura: implementar e testar um adaptador real, confirmar acesso/modelo/preço e orçamento e obter autorização antes de chamar. Registrar tokens, latência, falhas e custo efetivos. Nesta etapa nenhuma dessas chamadas está autorizada ou executada. Não é necessário contratar API para avaliar primeiro o método com os agentes da sessão, desde que a procedência fique explícita.

## Conferência pelo usuário, item a item

Mostrar questão e trecho citado, objeto, tarefa exigida, aspecto curricular citado, vínculo parcial ou pendência, problemas de uso e verificação estrutural separada. O usuário registra uma decisão de conferência de evidências, com justificativa:

- Evidência conferível e coerente com a tarefa;
- Evidência insuficiente ou vínculo contestado;
- Não consigo decidir: encaminhar ao especialista ou solicitar fonte.

Conferir também todas as abstenções e objetos sem competência: perguntar se há evidência curricular ignorada e registrar eventual contestação. Isso procura omissões, mas não fornece recall pedagógico sem uma referência especializada.

Registrar o tempo ativo de leitura/conferência por item, excluindo interrupções. Informar experiência do avaliador e se já conhecia o item. Não chamar essa conferência de gabarito de referência pedagógico.

Revisão especializada continua necessária para validade do item e alternativas, suficiência da tarefa como evidência da habilidade, adequação do nível cognitivo ao propósito, ambiguidades e eventual autorização institucional de uso. Um campo aceito na conferência de evidências não preenche esse segundo parecer nem libera prova.

## O que medir com honestidade

1. Cobertura: oito registros presentes, quantos receberam resposta válida, erro técnico, sugestão de vínculo, somente objeto ou abstenção. São categorias diferentes; sempre informar numerador e denominador.
2. Rastreabilidade: citações localizáveis e literais entre as citações apresentadas; exemplos de falhas. É medida técnica, não de pertinência semântica.
3. Resultado da conferência: quantos itens tiveram evidências aceitas, contestadas ou inconclusivas pelo usuário, separados por estado da sugestão. Não chamar aceitação de acurácia.
4. Operação: minutos ativos por item e total; pendências que tiveram próximo responsável/ação definidos; retrabalho necessário. Tempo de execução do programa fica separado do tempo humano.
5. Qualidade pedagógica: não medida enquanto não houver avaliação especializada independente, com critério e referência definidos.

Sem uma linha de base comparável, não afirmar economia de tempo. Se medir ganho for prioritário, antes de revelar sugestões o usuário pode fazer o mesmo registro de evidências manualmente nos oito, cronometrado. A revisão posterior com sugestões terá efeito de aprendizado e ordem; a diferença será exploratória, não causal. Com apenas oito itens, não ampliar alegações para o acervo. Alternativamente medir só tempo assistido agora e planejar comparação controlada com novos itens depois.

## Porta de decisão após a rodada

Bloqueios técnicos: perda de itens, citação fabricada aceita pelo validador, reutilização após mudança de entrada ou decisão confundida com liberação de prova exigem correção antes de ampliar. Falha de inferência deve continuar visível e contada.

Para ampliar, o usuário examina todos os oito e os casos contestados/inconclusivos. Não há percentual de aprovação inventado como critério pedagógico. Decidir explicitamente se as evidências permitem ampliar apenas a triagem, ajustar o método com uma nova reserva futura, ou buscar revisão especializada. Não repetir ajustes nos oito e continuar chamando-os de avaliação final independente.

Nenhum item reservado foi semanticamente avaliado para escrever este plano. Estado atual: proposta, não experimento realizado.
