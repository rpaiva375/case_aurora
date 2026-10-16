# Roteiro para gravar

Alvo: **3 minutos e 30 segundos**. Pare antes de 4 minutos.

Antes de apertar gravar, deixe a fila aberta:

```powershell
python -B queue_app.py --demo
```

Abra `http://127.0.0.1:8765`. Não leia JSON. Não abra todas as alternativas. Se atrasar, corte a parte do piloto. Não corte os três exemplos nem a frase de que a analista encaminha e não aprova.

## O que falar

**0:00 — o problema.** Tela da fila.

“Comecei pelo acervo que já existe. Antes de gerar mais questão, precisamos saber o que temos, o que conseguimos vincular com evidência e o que está pendente. Este protótipo faz essa triagem e registra o encaminhamento. Não altera o banco antigo e ainda não mede ganho de tempo.”

**0:25 — o que entra e o que sai.** Mostre o resumo da fila: 68 questões.

“Entram sete arquivos, sem limpeza manual. Saem 68 questões: seis com análise já gravada, 54 sem análise e oito reservadas. Desempenho de aluno fica separado do histórico de aplicação, para não contar a mesma questão duas vezes.”

**0:50 — sugestão.** Abra o cartão ITM-10041.

“Esta questão pede calcular juros simples. A análise sugere um pedaço da habilidade HAB-03.1 e mostra o trecho. A analista confere esse trecho e encaminha para revisão especializada. Ter vínculo não significa que a questão pode ir para prova.”

**1:20 — abstenção.** Abra o cartão ITM-30007.

“Esta questão é jurídica. Os dois componentes que temos não a sustentam. A ferramenta registra a abstenção. A analista encaminha para quem responde pelo componente certo. Não inventa vínculo e não descarta a questão.”

**1:45 — pendência.** Abra o cartão ITM-10048. Aponte o gabarito bruto 2 e o padronizado vazio.

“O gabarito veio como 2. Sem a convenção da origem, não tratamos isso como alternativa B. O pedido de confirmação fica registrado. O arquivo original não muda, e registrar o pedido não envia mensagem nem resolve o dado.”

**2:15 — quem fez o quê.** Volte para a lista. Não percorra os oito itens.

“As seis análises da fila são respostas gravadas: o comando não chama IA de novo. Os oito reservados tiveram uma rodada separada. Eu conferi só dois, o 20034 e o 10069, com ressalva. Isso não é aprovação pedagógica. Os testes checam se o dado não se perdeu. Não provam que a sugestão está certa.”

**2:45 — o que vem depois.** Abra `docs/PILOTO_30_DIAS.md`, só o título.

“Na Aurora, o próximo passo é um piloto de 30 dias, dentro do ambiente da instituição, lendo o banco e sem escrever no legado. Precisamos de ambiente, modelo interno e um revisor pedagógico. Começamos com poucas questões, medimos tempo e retrabalho, e aí decidimos se amplia. Isso é proposta. Ainda não está implantado.”

Pare perto de 3:30.
