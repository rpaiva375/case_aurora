# Piloto em 30 dias — proposta para decisão

## Onde rodaria

Processamento e inferência dentro do perímetro aprovado pela Aurora, com conta de leitura/exportação do SQL Server e saída em repositório separado. Sem escrita no legado nos primeiros 90 dias. Itens e currículo são suficientes para o recorte; não importar dados pessoais de alunos ou docentes. Desempenho e aplicação, quando incluídos, permanecem separados.

A Célula mantém código, contratos, regras de proveniência, testes e versões reutilizáveis na plataforma compartilhada. Primeiro confirmar se ela pode executar no perímetro exigido. Caso contrário, solicitar aprovação da liderança da Célula para exceção de execução interna, com operação e suporte combinados com TI. Não presumir essa capacidade existente. Enunciados, respostas, prompts e logs com conteúdo ficam internos; somente artefatos sem conteúdo sensível e métricas agregadas aprovadas podem ser compartilhados.

O protótipo atual é CLI local de replay. Não possui inferência integrada, autenticação de atores, armazenamento inviolável, serviço de produção ou integração SQL. A análise nova foi feita pelos agentes da sessão sobre dados fictícios. API pública externa não é solução aprovada para o acervo real.

## Decisões a liberar

- **TI Aurora:** homologação interna, acesso de leitura/exportação de recorte acordado, responsável técnico e regras de acesso, retenção, logs e cópias. Sem escrita no legado.
- **TI e liderança da Célula:** local de execução compatível com perímetro, responsabilidades operacionais e eventual exceção à plataforma compartilhada.
- **TI e patrocinador:** modelo executável no ambiente aprovado, capacidade/licença/orçamento e limites. Nenhum gasto autorizado nesta entrega. Sem liberação do modelo, piloto limitado à ingestão e triagem por regras; não apresentar como teste de IA integrada.
- **Coordenação de Avaliação:** recorte e volume inicial, analista, agenda de especialista e definição da unidade de 1–3 nós. Confirmar convenções de gabaritos com a origem.
- **Patrocinador e operação:** métricas e critérios de continuidade acordados antes da rodada, fila de exceções e responsáveis pelas respostas.

## Sequência proposta

- **Dias 1–5:** liberar os pontos acima, fixar recorte/referências, registrar pendências e medir pequena linha de base manual.
- **Dias 6–12:** ingestão somente leitura e integridade; adaptar inferência ao modelo interno autorizado e testar falhas sem publicar itens.
- **Dias 13–22:** lote limitado com analista, conferência de evidências e revisão especializada separadas; guardar erros, abstenções e versões. Usar novos itens para avaliar após ajustes, pois os oito do case já foram vistos.
- **Dias 23–30:** comparar tempo ativo, retrabalho, pendências resolvidas e julgamentos especializados; decidir ampliar, corrigir ou interromper. Não extrapolar desempenho em 240 mil itens a partir dos 68 fictícios.

## Medição e limites para ampliar

Medir completude, associações incorretas, citações verificáveis, sugestões/abstenções/erros, tempo ativo, retrabalho e pendências efetivamente resolvidas. Comparar tempo com linha de base e casos comparáveis; aceite de evidências pelo usuário não é acurácia pedagógica.

Não ampliar com perda de registros, reutilização após mudança de entrada, referência inventada aceita silenciosamente ou confusão entre mapeamento e liberação de prova. Critérios pedagógicos e decisão de aplicação pertencem à área acadêmica/especialista. Aprovar piloto não autoriza prova.
