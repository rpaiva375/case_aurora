# Parte visual — conversa do case

https://chatgpt.com/s/cx_6ad125fab20c8191ba99476c4f714d07 essa é a conversa que tive para resolver esse case, analise. Paramos na parte visual.

Não consegui abrir o link compartilhado. O ChatGPT devolve só a página de verificação do Cloudflare, então a leitura abaixo vem do que o projeto já registrou, não do texto turno a turno da conversa.

O trabalho parou no lugar certo para o case: o raciocínio e o fluxo local estão fechados; a tela da analista existe no código, mas ainda não é a história da entrega.

## O que a conversa resolveu

O recorte foi curadoria do acervo, não geração de questões novas. A ordem que o repositório documenta é esta:

1. **Integridade da entrada.** Os sete arquivos entram sem limpeza manual. Gabarito numérico sem convenção não vira letra. Desempenho e histórico de aplicação ficam separados para não inflar contagem.
2. **Vínculo só com evidência.** O critério passou a separar objeto, tarefa exigida e problema de uso. Sugestão parcial, abstenção e pendência são resultados diferentes. Concordância entre agentes não conta como validação pedagógica.
3. **Replay, não API.** O comando local reproduz seis respostas gravadas, deixa 54 sem análise e oito reservados, e marca `ready_for_exam=false` em todos. Alterar a entrada invalida a resposta gravada.
4. **Pessoa no fim.** Encaminhamento é um evento à parte do legado. Você conferiu de fato só 20034 e 10069. A demo dos três caminhos (10041, 30007, 10048) é exemplo de agente, não decisão sua.
5. **Fechamento do case.** Roteiro de cerca de 3min30, piloto de 30 dias e o índice dos quatro momentos de IA. Faltam o vídeo, o transcript original e o envio.

O controle de esforço em `docs/esforco.md` para na etapa 8, com saldo de planejamento de cerca de 2h25 de 8h. Até ali a instrução explícita era não acrescentar tela.

## Onde a parte visual ficou

Há uma fila local em `queue_app.py` e `queue_ui.html`: lista com prioridade, detalhe da questão, evidências, formulário de encaminhamento e histórico. Os atalhos já apontam para os três itens do vídeo (10048, 10041, 30007). A tela repete os limites que o case exige: replay, sem inferência nova, sem liberação para prova, demo separada de decisão real.

Isso ainda não está integrado à entrega escrita. O README ainda diz que não há interface. O roteiro manda mostrar `report.md` e os documentos, não a fila. O controle de horas não registra essa tela.

Para o vídeo, o buraco é de apresentação, não de regra de negócio. A analista ainda lê um relatório denso em vez de percorrer os três caminhos numa tela só. A interface também está num único arquivo, com pouco hierarquia visual para caber em três minutos e meio.

Se quiser continuar daqui, o próximo passo útil é fazer a fila ser o que o roteiro mostra nos três casos, e alinhar README e roteiro a isso. Posso fazer isso em seguida.

## Terminar a entrega visual primeiro

A fila local está pronta para a gravação. Abra http://127.0.0.1:8765: o servidor já está no ar com `python -B queue_app.py --demo`.

A tela abre nos três caminhos do roteiro, com os encaminhamentos demonstrativos já gravados:

- **ITM-10041** — sugestão parcial de HAB-03.1, com o limite da habilidade.
- **ITM-30007** — abstenção, sem componente jurídico na matriz.
- **ITM-10048** — gabarito bruto 2 e padronizado não confirmado.

O resumo mostra 68 questões, 6 analisadas por replay, 54 sem análise, 8 reservadas e 0 erros. Nenhum item aparece como liberado para prova. Com `--demo`, um registro novo sai como `agente_demo`.

O README, o roteiro e o checklist de entrega apontam para essa tela. Os 17 testes da fila passaram. Confirmei pelo servidor local os números, os três encaminhamentos e a referência atual de cada um. Não havia navegador disponível aqui, então a aparência em si ainda não foi vista numa janela.
