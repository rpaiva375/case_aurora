# Roteiro final — alvo 3min30, limite 4min

Alvo de gravação: **3min30**, com 30 segundos de margem. Os tempos são um plano, não ensaio medido. Prepare as abas e faça um ensaio cronometrado; não leia JSONs nem todas as alternativas. Se atrasar, corte navegação e detalhes, nunca a distinção de proveniência e os limites.

## Preparação fora do vídeo

Abra a raiz do projeto no terminal, este roteiro e `evaluation/CONFERENCIA_USUARIO.md`. Suba a fila antes de gravar: `python -B queue_app.py --demo` e deixe `http://127.0.0.1:8765` na tela. Python 3.10+ real é o único requisito; sem pacotes, credenciais ou rede. Na máquina atual, use o interpretador do README porque o alias Python do Windows não funciona.

Use destinos novos. Para executar ao vivo, altere o sufixo se já existir:

```powershell
python -B run_local.py --source output/originals --output runs/gravacao_01
python -B demo.py --results runs/gravacao_01/results.json --output runs/gravacao_demo_01
```

Abra `runs/gravacao_demo_01/report.md`. O segundo comando cria três eventos demonstrativos; nenhum evento real é atribuído à analista. Não gera inferência nem envia mensagens. O relatório já entregue é alternativa caso a navegação falhe. Não depende da pasta antiga, Downloads ou serviços de IA da sessão.

## 0:00–0:25 — problema escolhido

**Mostrar:** título e relatório.

**Fala:** “Escolhi começar pela curadoria do acervo existente. A hipótese é que precisamos saber o que temos, quais vínculos conseguimos justificar e quais pendências impedem o uso, antes de gerar mais questões. O protótipo organiza essa triagem e registra encaminhamentos, preservando o legado. Ainda não comprovamos ganho operacional.”

## 0:25–0:50 — entrada e saída funcionando

**Mostrar:** executar os dois comandos preparados; resumo e relatório.

**Fala:** “Entram os sete arquivos, sem limpeza manual. Saem as 68 questões: seis com análise gravada, 54 sem análise e oito reservadas neste comando. Desempenho e histórico de aplicação continuam separados. Cada transformação tem origem e regra. A avaliação separada das oito reservadas continua disponível.”

## 0:50–1:20 — sugestão

**Mostrar:** na fila, o cartão Sugestão parcial (ITM-10041), o trecho, HAB-03.1 e o encaminhamento demonstrativo.

**Fala:** “Calcular juros simples sustenta uma sugestão parcial de habilidade. A analista vê o trecho e a referência curricular, pode contestar a evidência e registrar o encaminhamento para revisão especializada. O evento demonstrativo guarda autor, motivo e versão da entrada. Ter vínculo não significa estar pronto para prova.”

## 1:20–1:45 — abstenção

**Mostrar:** na fila, o cartão Abstenção (ITM-30007) e o motivo.

**Fala:** “Esta questão jurídica não encontrou suporte nos dois componentes fornecidos. A ferramenta preserva a abstenção. A analista pode encaminhá-la para confirmação do componente adequado; não precisa inventar um vínculo nem descartar a questão. A decisão depende da referência curricular e de uma pessoa responsável.”

## 1:45–2:15 — pendência

**Mostrar:** na fila, o cartão Pendência de origem (ITM-10048), bruto 2 e padronizado não confirmado.

**Fala:** “O gabarito veio como dois. Sem conhecer a convenção, não assumimos que seja B. Registramos solicitar confirmação à origem, sem mudar o legado. Se a entrada muda, a resposta gravada não é reutilizada. Registrar o pedido não resolve a pendência nem envia uma mensagem automaticamente.”

## 2:15–2:45 — onde houve IA e onde houve pessoa

**Mostrar:** marcação replay; caderno dos oito e conferência, sem percorrer itens.

**Fala:** “O comando reproduz seis respostas gravadas. Separadamente, agentes da sessão produziram uma rodada nova para os oito reservados: cinco sugestões, uma competência pendente e duas abstenções. O usuário conferiu somente 20034 e 10069, mantendo ressalvas e pendências. Isso não é validação pedagógica. Os testes verificam integridade; não provam acurácia ou economia.”

## 2:45–3:30 — Aurora e piloto em 30 dias

**Mostrar:** `docs/PILOTO_30_DIAS.md`, decisões a liberar.

**Fala:** “Na Aurora, proponho processamento e inferência dentro do perímetro institucional, com exportação ou leitura do SQL Server e sem escrita no legado nos primeiros 90 dias. A Célula mantém código e contratos reutilizáveis na plataforma compartilhada. Se ela não operar nesse perímetro, peço exceção formal para execução local; enunciados não saem. Para um piloto em 30 dias, precisamos liberar ambiente, leitura, modelo interno aprovado e responsáveis de curadoria e revisão pedagógica. Começamos com recorte limitado, medimos tempo e retrabalho com linha de base e decidimos se vale ampliar.”

## Encerrar

Parar aos 3min30 planejados; quatro minutos é teto absoluto. O vídeo ainda precisa ser gravado e ter duração conferida. O piloto é proposta, não arquitetura implantada nem autorização recebida. Os três eventos da demo são demonstrações, separados da conferência real dos dois casos.
