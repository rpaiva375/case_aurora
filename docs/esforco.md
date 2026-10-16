# Controle do limite de oito horas

## Como interpretar

O limite do case é **8 horas**. Tempo de execução de agentes não equivale a horas de trabalho humano. Os registros abaixo distinguem relógio, soma de execuções e provisão de orçamento. Espera por resposta do usuário entre etapas não será debitada como trabalho.

O diagnóstico da etapa anterior não foi cronometrado. Não há base para afirmar um consumo exato acumulado. Para manter um controle conservador, foi mantida a **provisão de 1 hora para diagnóstico e decisão de escopo** do orçamento proposto anteriormente. Essa hora é uma provisão, não uma medição nem uma aprovação nova do usuário.

## Etapa 1 — ingestão e padronização

- Início registrado: **14/10/2026, 15:31:47 America/Sao_Paulo** (18:31:47 UTC).
- Marco de fechamento técnico: **14/10/2026, 15:38:56 America/Sao_Paulo** (18:38:56 UTC): **7min09s de relógio** desde o início registrado, antes da preparação da resposta final.
- Agente de ingestão: primeiro marco observado às **15:32:41**, conclusão às **15:35:42**: **3min01s**. Esse é um intervalo registrado, não uma medição de trabalho humano.
- Agente revisor: primeiro marco às **15:36:30**, após a leitura inicial; conclusão às **15:38:25**: **1min55s registrados**, mais o início não cronometrado. Para orçamento, reservar **3 minutos** à revisão cobre esse intervalo e a leitura inicial nesta sessão.
- O intervalo do manager inclui coordenação e esperas; a soma com os intervalos dos agentes é apresentada apenas como teto conservador de débito, pois contém sobreposição.

## Saldo conservador no fechamento da etapa 1

- Diagnóstico anterior e decisão de escopo: **1h provisionada**, não cronometrada.
- Etapa 1: **20min debitados conservadoramente**, cobrindo o relógio da coordenação, as execuções dos agentes, início não cronometrado e preparação da entrega. Não significa que foram observados 20 minutos líquidos de trabalho humano.
- Débito orçamentário acumulado: **1h20 de 8h**.
- Saldo de planejamento: **6h40**.

O esforço acumulado real não é conhecido com precisão. Este saldo usa provisões explícitas para não apresentar uma estimativa como medição. Tempo de revisão humana fora desta sessão não está incluído e deve ser acrescentado quando informado.

Não foram medidos nesta etapa o tempo de um analista curando questões ou qualquer ganho operacional.

## Etapa 2 — rastreabilidade e pequena amostra semântica

- Início observado pelo manager: **14/10/2026, 15:50:33 America/Sao_Paulo** (18:50:33 UTC).
- Fechamento técnico observado: **15:59:26** (18:59:26 UTC): **8min53s de relógio**, antes da preparação final da entrega.
- Mapeador: fim registrado às **15:54:58**; início não cronometrado de forma confiável. A estimativa `18:51:00Z` presente na v1 antecede a delegação e não foi usada como medição; ressalva registrada em `mapping/LEITURA_DA_RODADA.md` sem reescrever a resposta original.
- Revisor crítico: intervalo registrado **15:56:13–15:58:04**, aproximadamente **1min51s**, além de leitura preliminar não cronometrada.
- Provisão conservadora debitada para esta rodada: **30min**, incluindo coordenação, execuções de agentes e entrega. Não é medição de esforço humano líquido.
- Novo débito de planejamento acumulado: **1h50 de 8h**; saldo **6h10**. Inclui a provisão de 1h do diagnóstico e 20min da etapa 1.
- API paga do pipeline: nenhuma chamada; custo incremental executado de API US$ 0. Custo/cota da sessão Codex não mensurado. Estimativa de API futura está em `provedor_e_custo.md` e não foi debitada como gasto real.

Nenhum tempo de revisão especializada ou benefício operacional foi medido. O tempo de espera entre mensagens de etapas não foi debitado como trabalho; a mensagem de continuação dentro desta rodada não reiniciou o orçamento.

## Etapa 3 — critério uniforme, revisão v2 e proposta executável

- Início observado: **14/10/2026, 16:14:49 America/Sao_Paulo** (19:14:49 UTC).
- Marco de fechamento técnico: **16:21:11** (19:21:11 UTC), **6min22s de relógio**, antes da entrega final.
- Dois agentes participaram: autoria da v2 e crítica independente. Seus intervalos não foram somados como horas humanas; houve sobreposição com a coordenação.
- Débito conservador de planejamento desta rodada: **30min**, incluindo agentes, verificações, documentação e entrega; é provisão, não medição de esforço humano.
- Acumulado provisionado: **2h20 de 8h**; saldo de planejamento: **5h40**.
- O fluxo integrado foi proposto, não implementado. Sua estimativa de **2h15** ainda não foi debitada.
- Nenhuma chamada de inferência à API do projeto; gasto executado dessa API **US$ 0**. Consulta à documentação pública não testa disponibilidade na conta. Custo/cota Codex não mensurado.
- Dez testes v2 passaram; limites da amostra e preservação de v1/entradas foram conferidos. Não foram medidos acurácia pedagógica ou ganho operacional.

## Etapa 4 — comando local replay e revisão independente

- Data: **15/10/2026**. Início observado **10:49:34 America/Sao_Paulo** (13:49:34 UTC); marco de execução final **10:55:58** (13:55:58 UTC): **6min24s de relógio**, antes do fechamento documental.
- Implementador e revisor trabalharam com sobreposição; não há medição de esforço humano líquido. Debitado conservadoramente **45min** para implementação, revisão, correção de codificação, testes e entrega.
- Acumulado provisionado: **3h05 de 8h**; saldo de planejamento **4h55**. A rodada ficou dentro da reserva de **2h15**; o restante dessa reserva não foi debitado.
- Escopo entregue: execução local sem rede, 68 saídas, seis respostas gravadas, 54 pendências, oito reservados, testes adversariais e README. Nenhuma inferência nova ou chamada paga.
- Adaptador de API real e controles de gasto ficaram fora do escopo desta rodada, conforme autorização exclusiva para replay. Não foram abandonados por estouro de prazo. UI, análise nova das outras questões e validação pedagógica também não foram executadas.
- Dez testes do autor e treze do revisor passaram. O manager identificou depois um defeito de acentos no relatório; autor corrigiu e acrescentou verificação Unicode. Execuções intermediárias identificadas como substituídas; saída final em `runs/replay_final/`.
- Nenhum ganho operacional ou qualidade pedagógica foi medido. Espera entre turnos não entra no débito; custo/cota Codex não mensurado; gasto API do projeto **US$ 0**.

## Etapa 5 — portabilidade e percurso de decisão

- 15/10/2026: início observado 11:27:10 America/Sao_Paulo (14:27:10 UTC); marco técnico 11:33:59 (14:33:59 UTC), intervalo de relógio 6min49s, incluindo coordenação/espera e antes da entrega. Não equivale a esforço humano líquido.
- Débito conservador de planejamento: **45min**. Acumulado **3h50 de 8h**; saldo **4h10**. Não há medição exata de horas humanas.
- Projeto passou a usar `C:\Users\rodri\Documents\projects\case_aurora`. Portabilidade executada com cópias locais dos sete arquivos; testes de ingestão/replay e revisão independente passaram.
- Registro separado de decisões e exemplo ITM-10048 concluídos pelo manager após limite de uso dos agentes. Oito testes passaram e 86 arquivos protegidos não mudaram. A revisão independente do novo registro ficou incompleta; não apresentar revisão do manager como outro agente.
- Proposta de avaliação dos oito reservados escrita, sem abrir semanticamente os oito nem gerar novas sugestões. Nenhuma API paga, tela ou busca acrescentada.
- Uma demonstração de encaminhamento registrada; zero resoluções reais e nenhum tempo humano de conferência ou ganho operacional medido. Cota Codex atingiu limite nos agentes; custo monetário dessa sessão não mensurado.

## Etapa 6 — rodada única dos oito reservados

- 15/10/2026: início observado 11:36:32 America/Sao_Paulo (14:36:32 UTC), fechamento técnico observado 11:45:59 (14:45:59 UTC): 9min27s de relógio, com agentes sobrepostos e antes da resposta final. Não é esforço humano líquido.
- Rubrica congelada às 11:38:18, antes da extração e leitura semântica dos oito nesta rodada. Um agente gerou uma única resposta; outro auditou integridade/citações sem segunda inferência semântica.
- Resultado: oito respostas, cinco sugestões, um objeto com competência pendente e duas abstenções; 40 citações literais conferidas. Sete testes técnicos passaram. Revisões do usuário/especialista: zero realizadas.
- Erro técnico do primeiro verificador preservado: rejeitou campos raw.* e ações estruturadas permitidas pela rubrica. Corrigido apenas leitor/apresentação; raw, julgamentos e abstenções não reescritos. Relatórios inicial e corrigido preservados.
- Débito conservador de planejamento: **45min**. Acumulado **4h35 de 8h**; saldo **3h25**. Provisão, não medição de esforço humano.
- API paga: nenhuma chamada; custo API **US$ 0**. Uso/custo Codex não mensurado. Tempo humano de conferência e ganho operacional continuam não medidos.
- Próxima prioridade: receber conferência das evidências, concluir revisão independente do registro de decisões e fechar demo do fluxo existente. Não acrescentar tela, busca ou API. Os oito não são mais inéditos para ajustes futuros.

## Etapa 7 — duas conferências reais, revisão final e demo

- 15/10/2026. Primeiro marco de relógio desta entrega: 15:35:03 America/Sao_Paulo (18:35:03 UTC), após início da coordenação. Fechamento técnico: 15:36:54 (18:36:54 UTC). Intervalo observado 1min51s, não duração integral nem esforço humano. Espera do usuário entre turnos não foi debitada.
- Débito conservador de planejamento: **30min**, incluindo registro, agentes, testes, demo e entrega. Acumulado **5h05 de 8h**; saldo **2h55**. São provisões, não horas humanas medidas.
- Duas conferências reais registradas por instrução explícita: 20034 com ressalva/revisão especializada e 10069 mantendo competência pendente. Outros seis permanecem pendentes; zero validações pedagógicas e nenhuma inferência repetida.
- Revisão independente do módulo decisions.py concluída: oito testes existentes e sete adversariais distintos passaram. Nenhuma alteração necessária no módulo. O registro complementar dos dois casos foi verificado pelo manager, não incluído nessa revisão de código.
- Demo executada: sugestão 10041, abstenção 30007, pendência 10048; três encaminhamentos demonstrativos, 88 arquivos protegidos preservados, destino existente recusado sem sobrescrita. Nenhuma decisão demonstrativa atribuída ao usuário.
- Zero chamadas API, mensagens externas ou pendências substantivamente resolvidas pela demo. Tempo humano e ganho operacional não medidos. Permanecem limitações de autenticação/qualificação e de armazenamento local; nenhum item liberado para prova.

## Etapa 8 — fechamento e roteiro de até quatro minutos

- 15/10/2026: início observado 15:45:38 America/Sao_Paulo; marco técnico 15:49:12, intervalo observado 3min34s antes do fechamento documental/empacotamento. Não equivale a trabalho humano líquido.
- Provisão de fechamento: **30min**. Acumulado **5h35 de 8h**; saldo **2h25**. Não inclui gravação/envio pelo usuário nem tempo humano não informado.
- Outro agente verificou CLI e demo numa cópia isolada sem rede nem acesso aos caminhos anteriores; 68 saídas e três eventos corretos. README corrigido para estados atuais e execução sem dependência do caminho antigo.
- Roteiro alvo 3min30, 366 palavras de fala, duração estimada e ainda não ensaiada; plano de piloto interno, quatro momentos de IA e checklist de submissão preparados.
- Permanecem externos à entrega executada nesta sessão: gravar vídeo, anexar transcript original completo e disponibilizar os arquivos ao destinatário. Nenhuma chamada paga, nova inferência, aprovação pedagógica ou economia comprovada adicionada.
