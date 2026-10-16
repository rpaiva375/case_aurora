# Revisão independente final do registro de decisões

Data: 15/10/2026. Revisor: agente da sessão `/root/revisao_decisoes_final`, distinto do implementador e do manager. Escopo: `decisions.py`, seus testes e armazenamento local de eventos. Não houve API, inferência semântica nem alteração de dados do legado, respostas congeladas ou código de produção.

## Resultado

Revisão independente anteriormente incompleta agora concluída para o módulo de registro. Não encontrei defeito bloqueador nos caminhos examinados. Passaram **15 testes distintos: oito existentes e sete adversariais adicionados pelo revisor**. O código `decisions.py` não precisou ser alterado.

Comando, a partir da raiz atual do projeto:

```powershell
& 'C:\Users\rodri\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B -m unittest test_decisions review.test_decisions_independent -v
```

Saída observada: `Ran 15 tests in 0.253s` e `OK`. Os testes usam execuções temporárias dentro de `runs/`, removidas ao final. A primeira execução da suíte duplicava testes por herança; essa coleta foi corrigida antes da execução final. A contagem de 15 não inclui repetições.

## Evidências verificadas

- Dois eventos sucessivos usam arquivos diferentes, preservam bytes do primeiro e não modificam resultado nem origem.
- Colisão forçada no identificador gera `FileExistsError`; não sobrescreve o evento existente.
- Alteração do resultado torna evento anterior `stale`; alteração da origem bloqueia consulta/registro. Evento com referência de outro item também é `stale`.
- Item duplicado exige `record_id`; origem com `record_id` duplicado é rejeitada.
- Escrita é recusada na origem preservada, fora de `runs/`, na própria raiz `runs/`, dentro da execução consultada e dentro de outra execução identificada por `results.json`.
- Item marcado `reserved` é recusado pelo fluxo operacional. A avaliação separada não transforma esses registros em itens liberados.
- `approve_exam` e classe desconhecida são rejeitados; ator e justificativa vazios não são aceitos.
- Todas as classes mantêm `ready_for_exam=false`, `qualification_verified=false`, sem transformar conferência de evidências em aprovação especializada.
- `accept_evidence` preserva a pendência de gabarito numérico e o valor padronizado nulo; registrar não resolve automaticamente a pendência.
- Demonstração exige conjuntamente `demo=true` e ator `agente_demo`; evento real é marcado `demo=false`. Isso separa a proveniência declarada dos exemplos.

## Limites que permanecem

- A propriedade append-only é garantida pelos comandos da ferramenta; não é um armazenamento inviolável. Quem tem acesso ao disco pode editar/remover arquivos manualmente. Não há assinatura digital, controle de acesso ou autenticação do ator.
- `event_applicability=current` significa coincidência da referência da entrada, não autenticação do conteúdo/autor do evento nem validação pedagógica. Um JSON editado manualmente pode conservar a referência e adulterar outros campos; deve-se consultar eventos produzidos pelo comando e não tratar coincidência como prova de autenticidade.
- Classes de revisão são declarações; a ferramenta não verifica credenciais de especialista. A aceitação de evidências nunca libera uso em prova.
- O hash do resultado completo é conservador: alteração em outro item também invalida a referência anterior, exigindo conferência novamente.
- A revisão cobre o módulo operacional e seus testes, não o mérito das sugestões, a nova conferência do usuário registrada em overlay separado, nem ganho de produtividade.

Não se propõe ampliar o escopo para autenticação ou armazenamento inviolável nesta demo local. Para uso operacional compartilhado essas limitações precisam ser reavaliadas.
