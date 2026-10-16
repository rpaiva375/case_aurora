# Exemplo completo — ITM-10048

Executado na nova pasta do projeto. Este é um registro demonstrativo do agente, não decisão do usuário nem parecer pedagógico. Nenhuma mensagem foi enviada a terceiros.

## 1. Encontrar a pendência

Abra `runs/portabilidade/report.md` e procure `ITM-10048` ou `ANSWER_UNRESOLVED`. O item está pendente de análise porque não há resposta gravada; separadamente, a ingestão detectou o gabarito numérico não resolvido. Não confundir essas duas pendências.

Em PowerShell, na pasta do projeto, selecione seu Python. Nesta máquina o comando abaixo usa o interpretador existente porque o alias `python` do Windows não funciona:

```powershell
$pythonAurora = 'C:\Users\rodri\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $pythonAurora -B decisions.py show --results runs/portabilidade/results.json --item ITM-10048
```

## 2. Conferir origem e saída

O comando mostra registro `04_itens_legado.csv:8`, linha física 9, valor bruto `gabarito = "2"` e valor padronizado `gabarito = null`. A ocorrência é `ANSWER_UNRESOLVED`. Não há evidência de que 2 signifique B. A cópia original permanece em `runs/portabilidade/ingestion/originals/04_itens_legado.csv`; o log da transformação fica em `ingestion/audit.json`.

## 3. Registrar um encaminhamento separado

Decisão exemplificada: solicitar ao responsável pela exportação a convenção de gabaritos, mantendo a pendência até confirmação documentada. Responsável sugerido é o detentor da exportação; ninguém foi designado ou contatado automaticamente. Essa ação não resolve o gabarito nem libera o item.

```powershell
& $pythonAurora -B decisions.py record --results runs/portabilidade/results.json --item ITM-10048 --events runs/decision_demo --actor agente_demo --review-kind operational --decision request_source --note 'Demonstracao: confirmar a convencao numerica com a origem; manter 2 bruto e canonico nulo ate evidencia documentada.' --demo
```

Cada execução cria um evento com UUID novo e imprime seu caminho. Não substitui eventos anteriores. O exemplo já executado está em `runs/decision_demo/f49c4a10f29440d7be80eb72989bb11d.json`. Contém autor `agente_demo`, `demo=true`, tipo `operational`, ação `request_source`, justificativa, data, hashes e referência ao item. Não é necessário executar novamente para inspecionar o exemplo entregue.

## 4. Conferir o registro e sua aplicabilidade

```powershell
& $pythonAurora -B decisions.py show --results runs/portabilidade/results.json --item ITM-10048 --event runs/decision_demo/f49c4a10f29440d7be80eb72989bb11d.json
```

Resultado verificado: `event_applicability=current`, bruto `2`, canônico `null`, `ready_for_exam=false`. O arquivo `runs/decision_demo/verification.json` registra comparação de hashes de 86 arquivos protegidos: nenhum foi alterado pela criação do evento.

Para entradas novas, rode a ingestão/replay em outra pasta e confira o evento contra o novo `results.json`. Se a referência mudou, aparece `stale`; a decisão não é aplicada automaticamente. Se a origem interna de uma execução foi alterada, a inspeção é recusada. Alterar arquivos externos sem executar nova ingestão não atualiza uma execução histórica.

## Decisão real e limites

Uma decisão real exige autor identificado, justificativa, tipo de revisão e ausência de `--demo`; não foi registrada nesta entrega. `user_evidence_check` registra conferência das evidências; `specialist_pedagogical` registra a classe declarada de um parecer, mas o programa não autentica qualificação; `operational` registra encaminhamentos. Nenhum tipo preenche automaticamente os outros ou autoriza uso em prova.

O registro é de adição, um arquivo novo por evento, sem edição automática dos anteriores. Não é trilha criptograficamente inviolável nem sistema de autenticação. Para corrigir um encaminhamento, acrescente outro evento citando o anterior na justificativa. Não há fechamento automático da pendência: recebida uma fonte confirmatória, documente-a e planeje uma nova versão da transformação, preservando a versão anterior.

Medição realizada: completude técnica do percurso e preservação de arquivos. Não medimos tempo humano, resolução efetiva da pendência, qualidade pedagógica ou economia operacional. O exemplo teve um encaminhamento demonstrado; zero pendências substantivamente resolvidas.
