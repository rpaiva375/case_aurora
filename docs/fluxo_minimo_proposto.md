# Proposta mínima: executar o fluxo de mapeamento

**Estado: proposta de implementação, não um comando já disponível.** A ingestão e os validadores existentes rodam localmente. As sugestões v1/v2 foram autoradas pelos agentes da sessão. Ainda não existe cliente de inferência integrado ao projeto. Nesta rodada o usuário pediu a proposta e a revisão dos seis casos; nenhuma API paga está autorizada.

## Um programa local, dois provedores intercambiáveis

Reaproveitar `ingest.py` e o contrato v2. Acrescentar um único comando Python que:

1. Leia os sete arquivos sem preparação manual, execute a ingestão e confira hashes/contagens. Desempenho e aplicações continuam separados e não decidem competência.
2. Selecione explicitamente os seis IDs de desenvolvimento; não envie os oito reservados. Monte, por item, um pedido com enunciado/alternativas e matriz/ementas, mais rubrica v2 e formato de resposta. Conteúdo do acervo é dado, nunca instrução para o provedor.
3. Chame `provider.suggest(request)` e salve o retorno bruto com origem, modelo, versão da rubrica, hashes do item/referências e identificador de execução.
4. Confira estrutura, IDs, referências literais e proveniência; rode a regra de nós separadamente, sem apagar sugestões. Respostas inválidas viram pendência técnica, não abstenção pedagógica fictícia.
5. Exporte JSON e um relatório Markdown legível, um registro por item. Mostrar separadamente assunto/OC, tarefa exigida, vínculo de competência ou pendência e problemas de uso. Nunca emitir “pronto para prova” porque há vínculo.

Sem UI, banco novo, embeddings, busca vetorial, segundo serviço ou segundo agente obrigatório em toda chamada. Uma crítica adicional de IA pode ser experimento posterior, mas não substitui revisão humana e não é necessária para demonstrar a primeira execução completa.

## Modo sem gasto: mock/replay explícito

- Adaptador local retorna respostas gravadas dos seis casos, identificadas como `provider_mode=mock`, `response_origin=session_agent_recording`, `new_inference=false`. Não apresenta as respostas gravadas como produto de uma nova chamada de IA.
- Resposta gravada só vale para o mesmo hash do item, currículo, rubrica e contrato. Mudou qualquer entrada ou surgiu item novo: retornar `fixture_missing_or_stale`; não inventar sugestão nem fazer fallback para rede.
- Fixtures adicionais simulam recusa, timeout, JSON inválido, referência inexistente e limite de nós excedido. Ficam fora da base entregue e não contam como qualidade real.
- Demonstra execução ponta a ponta, persistência, tratamento de falhas, rastreabilidade e relatórios. **Não demonstra geração nova, generalização, qualidade do modelo proposto, latência ou custo de inferência.**

## Modo real: mesma interface, ainda não executado

- Adaptador OpenAI Responses API com modelo explicitamente configurado, formato estruturado e captura da resposta efetiva e uso faturado. Não simular sucesso se houver erro de autenticação, indisponibilidade ou recusa.
- Nenhum gasto até autorização do usuário. O futuro programa deverá iniciar em mock por padrão; modo real exigirá configuração explícita e orçamento positivo autorizado, com reserva por chamada e parada antes de ultrapassar o teto.
- Fazer checagem de disponibilidade para o projeto/conta e de limites antes da inferência; existência no catálogo público não confirma acesso na conta. Não foi feita autenticação nesta rodada.
- Sem ferramentas hospedadas, Fast mode, cache-write solicitado ou contexto longo no orçamento base. Limitar entrada e saída; incluir raciocínio faturado na saída. Repetições só dentro do teto, com limite explícito; nunca fallback silencioso para outro modelo/provedor.
- Em caso de resultado técnico inconclusivo, registrar `not_evaluated_provider_failure`. `semantic_abstention` fica reservado para uma resposta real e válida em que a evidência curricular foi considerada insuficiente.
- Guardar custo calculado com tarifa/versionamento e o uso retornado, sem exibir chaves. Nenhuma credencial deve ser persistida na pasta.

## Contrato de saída mínimo

Por registro: ID e hash da fonte; origem da resposta; assunto; objeto(s) com suporte; tarefa exigida e trechos; aspecto curricular e competência sugerida/pendente; problemas de uso; razões e referências; pendências técnicas; checagem estrutural separada; revisões humanas em campos próprios.

Os três estados não se substituem: um objeto sustentado pode continuar sem competência demonstrada; um vínculo sugerido pode coexistir com gabarito contestado; ausência de problema detectado não autoriza aplicação em prova. `user_coherence_review` e `specialist_pedagogical_review` permanecem distintos e não preenchidos automaticamente.

## Critérios de aceite da implementação proposta

- Um comando, a partir dos arquivos fornecidos, produz seis resultados sem limpeza manual e sem alterar originais, v1/v2 ou reservados.
- Modo mock não acessa rede nem chaves; saída e relatório identificam simulação/replay em destaque. Entrada divergente não recebe resposta gravada incorreta.
- Todo resultado aponta para entrada, rubrica e resposta bruta verificáveis. Falhas não desaparecem da contagem de seis itens.
- Regra estrutural pode ser recalculada sem chamar o provedor; excesso de nós mantém os candidatos.
- Modo real desabilitado sem autorização/configuração; timeout, saída inválida e orçamento exercitados por fixtures antes de qualquer gasto.
- Quando houver autorização, fazer primeiro uma chamada real pequena, conferir uso/custo e limites, depois concluir o recorte autorizado. Acesso confirmado, inferência real e qualidade pedagógica são três verificações diferentes.

## Esforço proposto, ainda não consumido

- Agente de implementação: aproximadamente 60 minutos para CLI, pedido/retorno comum, replay e exportação.
- Agente de implementação: aproximadamente 45 minutos para adaptador real desabilitado por padrão, controles de falha/custo e testes sem rede.
- Outro agente e manager: aproximadamente 30 minutos para verificar execução, rastreabilidade e README.
- Total de planejamento: **2h15**, sujeito à integração. A chamada real e a avaliação especializada não são consideradas concluídas por esse orçamento.

A reserva de oito itens só será usada depois de congelar critério e configuração após revisão do usuário. O modelo de API público proposto é para o pacote fictício; produção Aurora continua condicionada à execução dentro do perímetro institucional.
