# Verificação do fluxo de decisão e portabilidade — 15/10/2026

O agente de portabilidade executou na nova pasta 23 testes CLI, 11 testes de ingestão e 1568 assertivas da revisão independente. A execução `runs/portabilidade` contém 68 registros: seis replay, 54 pendentes, oito reservados e zero erros. Ajustou o README e o verificador independente para usar a fonte local, sem caminho antigo.

O agente autor de `decisions.py` criou código e oito testes, mas atingiu limite de uso antes da conclusão. O segundo agente também atingiu o limite antes da revisão desse novo código. Portanto, não declarar revisão independente concluída de `decisions.py`. O manager leu código/testes, executou os oito testes com sucesso e concluiu a demonstração/documentação.

Os testes cobrem preservação de entradas e eventos anteriores, mudança de origem/resultados, separação de tipos de revisão, identificação da demonstração, bloqueio de reservados, proibição de gravação dentro da execução e rejeição de decisões inválidas. Demonstração real da CLI/funções: `runs/decision_demo/verification.json`, 86 arquivos protegidos idênticos antes/depois, evento aplicável à execução, gabarito bruto 2 e canônico nulo, sem liberação para prova.

Limites: eventos são arquivos locais, sem autenticação ou assinatura. Classes de revisão declaradas não verificam qualificação. Mudanças externas só entram após uma nova ingestão. A comparação da referência é conservadora: mudança em outra parte do results.json também pode tornar o evento stale. Nenhum encaminhamento foi enviado, nenhuma pendência foi substantivamente resolvida e nenhum ganho humano foi medido.
