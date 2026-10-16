# Auditoria técnica independente — rodada única dos oito reservados

Auditoria de 15/10/2026, restrita à rubrica congelada, aos dois manifests, ao pacote, ao código de apresentação e ao raw da rodada. Os nove arquivos listados em `source_hashes` foram acessados adicionalmente somente como bytes para recalcular SHA-256. Não houve rede, API, nova inferência, revisão dos julgamentos semânticos ou alteração do raw e das saídas de apresentação por esta auditoria.

## Resultado técnico

Os oito IDs congelados aparecem exatamente uma vez no pacote e exatamente uma vez no raw, sem itens adicionais: ITM-10049, ITM-10060, ITM-10069, ITM-20028, ITM-20034, ITM-20037, ITM-20044 e ITM-30010. Todos os `record_id` correspondem aos registros originais do pacote. A ordem diferente dos dois últimos registros não altera essa correspondência.

Uma conferência própria em memória resolveu os campos `raw.*` dos itens, os pointers JSON da matriz e os intervalos inclusivos de linhas das ementas. Todas as 40 citações foram encontradas literalmente nos locais declarados: respectivamente 5, 5, 6, 4, 4, 6, 5 e 5 citações nos IDs acima. Não houve normalização do texto citado. As três classes de evidência estão presentes nos cinco itens com pares sugeridos e no item com objeto pendente.

Os cinco pares sugeridos usam OCs existentes, competências permitidas por esses OCs e habilidades pertencentes às competências indicadas. Candidatos mencionados nas justificativas não foram contados como vínculos. A contagem separada de nós únicos OC+COMP, excluindo habilidades, confere com o raw: cinco itens com 2 nós e `within_provisional_limit`; ITM-10069 com 1 OC sem par e `incomplete_mapping`; ITM-20044 e ITM-30010 com 0 nós e `not_applicable`. Nenhum excesso ou corte de vínculo foi identificado.

Todos os oito registros têm `ready_for_exam=false`, `user_evidence_check=pending` e `specialist_pedagogical_review=pending`. Os estados declarados são cinco `suggested`, um `object_supported_competency_pending` e dois `abstained`; esta auditoria não os reclassifica semanticamente.

## Incompatibilidades da apresentação inicial

A versão inicialmente lida de `present.py` exigia `analyst_next_action` textual, enquanto o raw usa um objeto com três ações separadas: conferência de evidência, solicitação de informação e revisão especializada. A rubrica congelada exige a distinção desses encaminhamentos, mas não fixa o tipo string. Portanto, a rejeição desse formato não demonstra erro substantivo da resposta.

O mesmo código procurava `evidence.field` diretamente dentro de `item.data`, embora o raw forneça caminhos explícitos como `raw.enunciado` e `raw.alternativa_b`. Esses caminhos existem no pacote e suas citações foram verificadas independentemente. A rejeição inicial não representa citação fabricada ou ausente. A correção de compatibilidade do leitor é distinta de uma nova rodada de inferência. Esta auditoria não editou nem executou `present.main`, nem verificou os artefatos derivados produzidos pelo responsável pela apresentação.

A rubrica desta rodada permite um trecho literal contido no campo ou intervalo. A conferência por substring respeita essa regra previamente congelada; não exige igualdade com todo o campo. Uma regra externa ou posterior denominada “exact v2” não foi aplicada retroativamente nem tomada como motivo de falha.

## Integridade

Todos os nove hashes de `freeze_manifest.source_hashes` coincidiram na leitura binária, inclusive rubrica, entradas, split e código de decisões. Isso verifica integridade dos bytes, não correção do código ou conteúdo. O hash do pacote e o do freeze manifest também coincidiram com `packet_manifest.json`; o total declarado de oito coincide com o pacote.

- Rubrica: `4cbcfdd463ce792a4cd03fc14146b8b9902fb88b841995c16078558ec5f99863`.
- Pacote: `93d8eed2d8d3fbc864714366928a929680a7748196a6b45381fa373e7fd2e07c`.
- Freeze manifest: `de2058b141363f68c31f8218f00b7df14e4d20438b5c447cf7e9dd2ac54def64`.
- Raw: `32631bf2d64c05f98d380f5d98d7c6cc5d9aec0cab8f95e8760f84cf8108e67a`, idêntico antes e depois da conferência própria.

O envelope do raw declara autoria `session_agent_new_inference`, rodada 1, zero retries semânticos e ausência de cliente API. Esta auditoria observa esses metadados e preserva o arquivo; o hash observado não prova sozinho todo o histórico anterior à primeira leitura.

## Limites

Localização literal e contagem de citações não medem qualidade pedagógica, pertinência do vínculo, suficiência da operação cognitiva, validade de gabarito ou adequação para prova. Os problemas de uso continuam apontamentos do agente a conferir, não diagnósticos especializados confirmados. Não foram mensuradas precisão pedagógica, concordância humana, economia operacional ou tempo poupado.

A reserva era prospectiva, não retrospectivamente cega, conforme declarado no freeze manifest. Esta auditoria da rodada não substitui a revisão independente de `decisions.py`, que permanece incompleta; recalcular seu hash não equivale a revisar suas decisões. Nenhum item está liberado para aplicação e as duas revisões humanas continuam pendentes.
