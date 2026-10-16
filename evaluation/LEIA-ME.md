# Resultado da rodada única

Comece pelo [caderno de conferência](CONFERENCIA_v2.md): contém os oito enunciados e alternativas, sugestões/abstenções, trechos literais, referências, limitações e uma pergunta de conferência por item. Sua análise das evidências está pendente; não foi registrada aprovação pedagógica.

Resultado formal: oito respostas presentes, cinco sugestões, um objeto com competência pendente e duas abstenções. Quarenta citações localizadas literalmente. Isso não é taxa de acerto pedagógico. Não houve chamada de API, nova tentativa semântica nem ajuste dos julgamentos após a entrega.

## O que a analista consegue encaminhar

- **ITM-10049, 10060, 20028, 20034 e 20037:** conferir o vínculo sugerido e seu escopo parcial com a fonte à vista; aceitar, contestar ou deixar inconclusiva a evidência. Os alertas de uso continuam separados. Esses cinco itens não formam uma seleção de questões prontas para prova.
- **ITM-10069:** preservar o objeto de avaliação de investimentos e manter a competência pendente; solicitar contexto/premissas se houver fonte original mais completa. Não converter reconhecimento qualitativo em aplicação de método automaticamente.
- **ITM-20044:** solicitar fonte completa e convenção/formato de alternativas e gabarito. A abstenção curricular é separada da incompletude: reconhecer a iniciativa do desligamento não foi considerado suficiente para explicar comportamento pelas teorias indicadas.
- **ITM-30010:** encaminhar para confirmação de recorte/componente tributário e referência temporal. Não forçar vínculo com finanças nem afirmar validade normativa do gabarito.

## O que continua dependendo de confirmação

O usuário pode conferir se trechos e justificativas sustentam o raciocínio, inclusive contestar abstenções. Especialista ainda precisa avaliar suficiência pedagógica, ambiguidades, alternativas, nível cognitivo e adequação ao uso. Detentor da origem precisa confirmar dados ausentes e premissas. A unidade de 1–3 nós continua provisória; nenhum vínculo foi cortado para obedecer ao limite.

Nenhuma ação acima foi executada junto a terceiros. São encaminhamentos sugeridos, não decisões do usuário. O registro independente de decisões continua sem revisão independente concluída; a auditoria desta rodada não supre essa lacuna. `decisions.py` e o replay ainda protegem os reservados e não foram alterados para incorporar respostas desta avaliação. Para conferir agora, use as perguntas do caderno e registre sua resposta por ID no chat ou em uma cópia separada; não edite a resposta bruta.

## Rastreabilidade e erro de ferramenta preservado

Rubrica e configuração foram gravadas em `freeze_manifest.json` antes de extrair os itens para `packet.json`. `rubric_diff.patch` mostra a derivação da v2: retiradas decisões dos seis exemplos e adaptado o contrato de entrega; mantido o critério semântico. O modelo é o herdado da sessão, sem identificador independentemente verificado; não é um teste do modelo de API proposto antes.

O agente entregou somente `raw_round1.json`, uma vez. SHA256: `32631bf2d64c05f98d380f5d98d7c6cc5d9aec0cab8f95e8760f84cf8108e67a`. A resposta não foi reescrita.

A apresentação inicial (`present_v1.py`, `verification.json`, `CONFERENCIA.md`) produziu oito erros técnicos porque o verificador exigia encaminhamento textual e campo simples. A rubrica permitia as ações estruturadas e não proibia `raw.enunciado`; 13 citações foram incorretamente marcadas como não localizadas. Corrigimos o leitor, não a inferência. O relatório corrigido é **CONFERENCIA_v2.md**, com **verification_v2.json**. A auditoria independente confirmou 40/40 citações e integridade. Sete testes técnicos passaram, inclusive teste de regressão para essas formas de resposta. Histórico inicial preservado para comparação.

Não houve erros de produção do agente reportados; houve erro técnico do nosso primeiro verificador, corrigido sem nova rodada. Nenhuma resposta ou abstenção foi descartada. Citações literais e integridade não aprovam a pertinência do raciocínio.

## Fechamento e demo, após sua conferência

1. Registrar suas oito conferências e destacar divergências, sem transformar suas respostas em validação pedagógica.
2. Priorizar a revisão independente restante do registro de decisões. Não acrescentar tela, busca ou API para a demo.
3. Demonstrar o percurso: rodar os sete arquivos → conferir 68 estados → abrir sugestão com evidências → abrir pendência/abstenção → registrar encaminhamento separado → alterar entrada em cópia e mostrar bloqueio de reutilização.
4. Encerrar com limites e próximos responsáveis: dados a confirmar, mérito a revisar e regra estrutural provisória.

Oito itens já foram abertos: não reutilizá-los como teste inédito após ajustes. Medimos cobertura técnica e rastreabilidade; tempo humano, aceitação das evidências, resoluções reais e ganho operacional ainda não foram medidos.
