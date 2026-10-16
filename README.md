# Case Aurora — base conferida e amostra de mapeamento

## Entrega final: começar aqui

- [Roteiro de 3min30](docs/ROTEIRO_FINAL.md), com margem até o teto de quatro minutos.
- [Proposta de piloto em 30 dias](docs/PILOTO_30_DIAS.md): ambiente Aurora, reuso na
  Célula e decisões a liberar; não é implantação já realizada.
- [Quatro momentos do trabalho com IA](docs/MOMENTOS_IA.md). O transcript original
  completo e o vídeo ainda precisam ser anexados; este índice não os substitui.
- [Teste de execução isolada](review/fechamento_portabilidade.md): cópia fora da pasta
  original, sem rede nem leitura de caminhos antigos; ingestão/replay e demo passaram.
- [Fechamento e itens para submissão](docs/ENTREGA.md): vídeo e histórico original
  ainda precisam ser anexados; não confundir código pronto com envio concluído.

Requer **Python 3.10+ instalado**; somente biblioteca padrão, sem instalação de
pacotes, serviço online, chaves ou credenciais. Abra o terminal na raiz desta pasta:

```powershell
python -B run_local.py --source output/originals --output runs/entrega_01
python -B demo.py --results runs/entrega_01/results.json --output runs/entrega_demo_01
python -B queue_app.py --demo
```

O terceiro comando abre a fila em `http://127.0.0.1:8765`: 68 questões, os três caminhos
(sugestão 10041, abstenção 30007, pendência 10048) e os encaminhamentos demonstrativos
já gravados em `runs/fila_visual`. `--demo` impede registrar uma decisão como se fosse
de uma pessoa. A tela não gera inferência nem libera item para prova.

Abra `runs/entrega_01/report.md` e `runs/entrega_demo_01/report.md`. Os destinos devem
ser novos; para repetir mude o sufixo. Os sete arquivos fonte já estão incluídos.
Se `python` for apenas o alias da Microsoft Store, use um Python instalado; a
alternativa testada nesta máquina está na seção de execução abaixo.

**Três origens distintas:** a CLI faz replay de seis respostas gravadas; as oito
análises novas foram geradas por agentes da sessão e estão em `evaluation/`, fora
da inferência da CLI; o usuário conferiu somente 20034 e 10069, em registro separado.
Não há inferência nova ao executar esses comandos. Nenhum desses resultados é
qualidade pedagógica validada ou economia operacional comprovada.

## Entrega atual: conferência e demo

- [Conferência real do usuário](evaluation/CONFERENCIA_USUARIO.md): somente 20034
  (sugestão parcial com ressalva e revisão especializada) e 10069 (objeto mantido,
  competência pendente). Os outros seis continuam pendentes. Nenhuma validação
  pedagógica ou liberação para prova.
- [Demo dos três caminhos](docs/DEMO.md): sugestão 10041, abstenção 30007 e pendência
  10048, com encaminhamentos demonstrativos separados do legado e das decisões reais.
- [Revisão independente concluída](review/revisao_decisoes_final.md): 15 testes do
  registro passaram, sem alteração necessária em decisions.py. A limitação de revisão
  incompleta nos documentos anteriores é histórica; limites de autenticação e parecer
  especializado permanecem. A revisão cobre o módulo, não o registro complementar dos
  dois casos, que foi conferido pelo manager contra sua instrução e os hashes.

O caderno da rodada permanece como retrato anterior à conferência; consulte o registro
complementar acima para o estado atual. Não houve repetição de inferência.

## Avaliação dos oito reservados — conferir agora

Abra o [caderno dos oito itens](evaluation/CONFERENCIA_v2.md), com enunciados,
alternativas, justificativas, trechos e referências. A rodada única de inferência
nova da sessão produziu cinco sugestões, um objeto com competência pendente e duas
abstenções; sem API paga. Sua conferência está registrada somente para 20034 e
10069; os outros seis continuam pendentes. O caderno preserva o estado da rodada.
O [guia de decisões e fechamento](evaluation/LEIA-ME.md) explica o que a analista
pode encaminhar, o que depende de confirmação e o erro do primeiro verificador,
preservado e corrigido sem repetir inferência. Nenhuma aprovação pedagógica.

## Conferir uma pendência e registrar a decisão

O [exemplo completo do ITM-10048](docs/exemplo_pendencia.md) mostra como localizar
a pendência, conferir valor bruto e padronizado, registrar um encaminhamento em
arquivo separado e verificar se a decisão ainda corresponde à mesma entrada.
O exemplo entregue é demonstrativo, atribuído ao agente, sem alteração do legado.
`decisions.py` nunca libera itens para prova e bloqueia os reservados.

A [proposta de avaliação dos oito reservados](docs/avaliacao_reservados.md)
separa sugestões novas, conferência das evidências pelo usuário e avaliação
pedagógica especializada. A proposta histórica foi executada em uma rodada separada
dos oito; não houve chamada paga. Consulte a atualização no início do documento.

Teste do registro: `python -B -m unittest test_decisions -v`.

## Fluxo local atual — 68 registros, sem API

Requer Python 3.10+; não instalar pacotes nem configurar credenciais. Abra PowerShell
na pasta do projeto e execute (ajuste o `cd` se o projeto for movido novamente):

```powershell
cd 'C:\Users\rodri\Documents\projects\case_aurora'
python -B run_local.py --source 'output\originals' --output 'runs\minha_execucao_01'
```

A pasta de saída deve ser **nova**, fora da árvore da fonte. Para repetir, use
`runs\minha_execucao_02`. O comando recusa sobrescrever uma execução existente.
A fonte `output\originals` contém as sete cópias preservadas byte a byte; o
comando não depende da pasta antiga nem de Downloads. Também aceita uma nova
pasta do pacote original pelo argumento `--source`.

Confira `python --version` antes de executar. É necessário um interpretador real
Python 3.10+ no PATH; o alias da Microsoft Store não basta. Se disponível, substitua
`python` por `py -3`. Nesta máquina o alias `python` falhou e `py` não foi
encontrado; a verificação foi feita com um interpretador já disponível no ambiente.
O projeto não exige esse interpretador específico nem pacotes adicionais.

Alternativa já executada nesta máquina, usando o interpretador existente (opcional,
não é dependência do projeto; substitua pelo seu Python em outra máquina):

```powershell
& 'C:\Users\rodri\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B run_local.py --source 'output\originals' --output 'runs\minha_execucao_02'
```

Abra primeiro `report.md` na pasta gerada; ele lista todas as questões, estados,
pendências estruturais e as evidências das seis respostas disponíveis.
`results.json` contém os mesmos resultados estruturados. Na entrada original:

- 68 registros, sem exclusão: seis analisados **por replay**, 54 pendentes por
  `fixture_missing`, oito reservados, zero erros técnicos.
- Os seis são: duas sugestões de vínculo, um objeto sustentado com competência
  pendente e três abstenções. “Analisado” não significa vínculo, aprovação ou acerto.
- Os oito reservados recebem apenas estado de reserva e proveniência; não há pedido,
  resposta semântica ou texto de enunciado deles no relatório. A ingestão mecânica
  mantém todos os registros, inclusive reservados, nos arquivos da base.
- `ready_for_exam=false` em todos. Revisão de coerência pelo usuário e validação
  pedagógica especializada são campos separados, ambos pendentes.

Arquivos auxiliares: `ingestion/` preserva os originais, auditoria e tabelas
separadas; `context.json` e `prompt.md` registram currículo e rubrica;
`requests/` registra entrada e fingerprint dos pedidos elegíveis;
`raw_responses/` preserva bytes das respostas lidas, inclusive inválidas.
Não há cruzamento de desempenho com aplicações para contar questões.

O único provedor disponível é **mock/replay**: seis respostas da sessão anterior,
congeladas em `replay_fixtures/`, com manifesto de fingerprints e hashes das respostas.
O programa não gera fixtures, não acessa rede, não lê chaves e não implementa API
real. `new_inference=false` deixa explícito que não houve inferência nova.
Isso testa o fluxo técnico; não mede qualidade semântica, ganho operacional ou
capacidade de analisar as outras 62 questões.

O fingerprint cobre o registro inteiro (`raw`, `data` e proveniência), matriz,
ementas, resolução das fontes, rubrica e versão/hash do validador. Alteração mesmo
no bruto que normalize para o mesmo valor bloqueia replay (`fixture_stale`).
Alteração curricular/rubrica bloqueia os seis. Reordenar linhas também pode bloquear
respostas por mudança de proveniência: opção conservadora. Não edite manifesto para
“fazer passar” entradas novas; é preciso uma nova análise explicitamente versionada.
Alterações apenas em desempenho/aplicações não invalidam a sugestão semântica,
pois essas tabelas não são entradas da análise e continuam auditadas na ingestão.

JSON inválido, estrutura ausente, citação incorreta ou resposta alterada geram
`processing_status=error` e `semantic_status=null` no registro; não se convertem em
abstenção pedagógica. Os demais itens continuam processados. Ausência de fixture
ou fixture obsoleta é pendência, não erro. Reserva tem prioridade sobre fixtures.

Códigos de saída: `0` = fluxo concluído sem erro técnico (pode conter pendências e
reservas); `2` = relatório completo com erro técnico por item; `1` = falha global,
por exemplo fonte ilegível/CSV inválido ou destino existente. Uma falha global não
permite prometer 68 resultados: quando a pasta foi criada, `run_error.json` registra
a interrupção; corrija a fonte e execute em outra pasta. `$LASTEXITCODE` mostra o
código no PowerShell.

Testes locais, sem API:

```powershell
python -B -m unittest test_run_local -v
python -B -m unittest review.test_cli_independent -v
python -B test_ingest.py --source output/originals -v
```

A mudança de pasta foi conferida em `runs/portabilidade/report.md`: 68 registros,
seis replays, 54 pendentes, oito reservados e zero erros técnicos. Passaram os 23
testes de CLI e 11 de ingestão. A conferência independente da base registrou
1.568 assertivas em `runs/portabilidade/independent_verification.json`. Para
repeti-la sem sobrescrever o relatório histórico, informe um destino de relatório
cuja pasta já exista:

```powershell
python -B review/verify_independent.py --source output/originals --report runs/minha_execucao_01/integrity_review.json
```

Os testes usam cópias temporárias no projeto e alterações artificiais; exercitam
entrada bruta alterada, currículo/rubrica diferentes, resposta JSON/estrutura/citação
inválida, aprovação indevida, reserva e não sobrescrita. `--fixtures OUTRA_PASTA`
serve para testar gravações alternativas, nunca para chamar um serviço.

Limite técnico: o adaptador reutiliza o validador v2 congelado, que espera seis
itens, conferindo cada resposta isolada por seis referências internas à mesma
resposta. Essas referências não são exportadas nem contadas como seis análises;
o teste de baseline exige um resultado por registro. Um contrato de validação
nativo por item pode substituir esse adaptador depois. Não há avaliação semântica
automática das justificativas nem liberação pedagógica.

A proposta anterior permanece como histórico: API real, autenticação, medição de
custo/latência e geração de sugestões novas ficaram fora desta implementação,
conforme o escopo autorizado sem gasto. Não há tela ou busca avançada.


## Histórico das etapas anteriores

Ingestão determinística dos sete arquivos sintéticos do case. Os scripts não fazem
chamadas externas, não requerem chaves de API e usam apenas Python 3.10+.
A etapa de ingestão não realiza mapeamento. A amostra semântica posterior contém
sugestões autoradas por agentes de IA da sessão e salvas para revisão; não é um
motor de inferência integrado por API. Não há aprovação pedagógica nem busca
avançada. A fila local descrita no início deste arquivo é a interface de curadoria.
A revisão de coerência do usuário não equivale à validação pedagógica
especializada; ganho operacional ainda não foi medido.

## Executar

Na pasta `case_aurora`, com Python instalado:

```powershell
python ingest.py --source 'output\originals' --output 'runs\ingestao_nova'
python test_ingest.py --source 'output\originals' -v
```

`--source` aceita a pasta do pacote ou `data_pack`. `--output` deve estar fora da
árvore da fonte. Reexecutar com a mesma entrada gera bytes idênticos. Para uma nova
versão dos arquivos, use outra pasta de saída: cópias originais diferentes causam
erro. A saída entregue está em `output/`.

## O que consultar

- `originals/`: sete arquivos copiados byte a byte. `manifest.json` registra SHA256
  antes/depois da fonte e da cópia e tamanho. Os originais externos não são escritos.
- `itens.json`: 68 registros; `desempenho.json`: 69 observações; `aplicacoes.json`:
  142 aplicações. As tabelas permanecem separadas. Nenhuma linha é deduplicada.
- Cada linha possui `record_id` da fonte + número do registro, `source` com arquivo
  e linhas físicas, `raw` integral e `data` padronizado. `item_record_id` só aponta
  para um registro único do cadastro; `link_status` expõe órfãos e ambiguidades.
- `audit.json`: cada campo alterado, valor anterior/posterior, regra e justificativa.
  `rules.json`: catálogo das regras. Tipagem numérica também é auditada.
- `pendencias.json`: ocorrências estruturais abertas com fonte, registro, campo e
  motivo. Contagens são ocorrências, não quantidades de itens distintos.
- `matriz.json`: JSON sem mudanças, com proveniência; `ementas_manifest.json`:
  duas resoluções explícitas de nomes, auditadas separadamente, sem reescrever a matriz.
- `textos.json`: ementas e fila integrais, com arquivo/intervalo de linhas; sem
  categorização semântica dos relatos da fila. Os originais preservam também os bytes.
- `integrity.json`: contagens, vínculos, grupos com grão repetido, verificações e
  limites da evidência. Falha de parsing ou hash encerra a CLI com erro.

## Regras e granularidade

IDs `ITM` + dígitos recebem hífen. Antes de vincular, o índice de itens verifica
todos os destinos canônicos: mais de um registro bloqueia o vínculo de todos os
afetados. O candidato canônico permanece visível, sem consolidar registros.
Possíveis duplicatas de item, item/semestre de desempenho e item/prova/semestre de
aplicação são sinalizadas e mantidas. Esse grão é uma regra técnica de detecção,
não uma autorização de exclusão.

Gabaritos `a` e `Alternativa B` tornam-se `A` e `B`. `1` e `2` ficam com canônico
null e pendência; não existe hipótese aplicada de equivalência número/letra.
Vazios viram null e pendência, sem imputação. Letras precisam ser A–E; o campo da
alternativa indicada é conferido. Alternativas preenchidas literalmente iguais
geram pendência. Alternativa ausente não torna automaticamente o item inválido:
não foi definida uma obrigação de cinco alternativas.

Textos e disciplinas permanecem como informados. Não corrigimos grafia, não
consolidamos nomes ambíguos e não inferimos texto-base ou pertencimento curricular.
Anos/contagens viram inteiros; métricas decimais viram números, sem mudar a escala
de percentual_acerto (fração). Semestres permanecem texto. Estatística ausente
permanece null. Não impomos limiares pedagógicos ou de qualidade psicométrica.

Nunca cruze desempenho diretamente com aplicações para somar medidas: existem
múltiplas observações de ambos os lados. Agregue cada tabela separadamente ao grão
necessário antes de combinar resultados. Para contagens de acervo use itens;
para respostas por período use desempenho e o semestre; para exposição use
aplicações e prova/semestre. `ITM-10066` mantém 2024.1 e 2025.1 separados.

## Verificações e limites

Testes comparam todas as linhas e campos brutos ao CSV, reconstrução pelo log de
auditoria, contagens, órfãos, gabaritos, semestres, textos/JSON, hashes e reexecução.
Fixtures sintéticas adicionais exercitam colisão de IDs, duplicação no mesmo
semestre e campo multilinha. Elas são exclusivamente testes de software, não
evidência de qualidade real ou pedagógica. Nenhum fixture é anexado à base entregue.

Não há interpretação de “1–3 nós”, análise semântica dos itens ou classificação
dos relatos. Lacunas semânticas (por exemplo texto-base referenciado e ausente) e
suspeitas de similaridade precisam da próxima etapa; não se apresentam como
detectadas automaticamente por este pipeline. A fila textual fica integralmente
consultável. A implementação lê a amostra em memória; desempenho em 240 mil itens
não foi testado. O manifesto detecta mudança da fonte durante a execução, mas
esta ferramenta local não oferece transação de diretório nem armazenamento imutável.

## Revisão independente e decisões abertas

Um segundo agente comparou a saída diretamente com as fontes e não identificou
defeito material ou bloqueante. O método, comandos e limites estão em
[review/revisao.md](review/revisao.md), com verificação reproduzível em
`review/verify_independent.py` e evidências em `review/verification.json`.
São 358 alterações de campos em `audit.json`, mais duas resoluções de nomes no
manifesto das ementas. Os 11 testes do autor passaram.

Consulte [decisões da etapa](docs/decisoes_etapa_1.md) para a distinção entre revisão
de coerência do usuário e validação pedagógica especializada, exemplos da regra
“1–3 nós” e a pergunta preparada (não enviada) à Coordenadora de Avaliação.
As [pendências de decisão](docs/pendencias_de_decisao.md) distinguem problemas
estruturais de dúvidas ainda não resolvidas. O [controle de esforço](docs/esforco.md)
separa intervalos medidos de provisões de orçamento.

## Etapa 2 — seis itens, antes de ampliar

Comece pelos [três casos de rastreabilidade](docs/rastreabilidade_casos.md), pela
[leitura da rodada após crítica](mapping/LEITURA_DA_RODADA.md) e pela
[amostra com evidências](mapping/amostra_v1.md). Consulte a
[crítica de outro agente](mapping/review/critica_v1.md) junto das sugestões: uma
concordância entre IAs não é validação pedagógica. A v1 permanece preservada.

O [protocolo](docs/protocolo_amostra.md) descreve a seleção de seis itens, a reserva
prospectiva de oito, a exposição prévia no diagnóstico e a separação entre
inferência semântica e regra provisória de nós. `mapping/split.json` registra a
partição e hashes; `mapping/sample_packet.json` é o único pacote de dados fornecido
aos dois novos agentes. Os outros 54 itens não foram mapeados nesta rodada.

`mapping/suggestions_v1.json` contém sugestões e abstenções;
`mapping/rule_checks_v1.json` contém a checagem separada de quantidade e permissão.
Exceder o limite não remove vínculos. As [condições de provedor e custo](docs/provedor_e_custo.md)
distinguem inferência nesta sessão, validação determinística e futuro piloto de API
ainda não executado. Naquela rodada não havia mock respondendo pelo provedor nem medição real do
modelo proposto para API. O replay local está descrito no início deste README.

Para reproduzir as verificações, a partir desta pasta:

```powershell
python trace_examples.py
python verify_sample_boundary.py
python mapping/validate_mapping.py
python -m unittest discover -s mapping -p test_validate_mapping.py -v
```

Esses comandos verificam artefatos existentes; não geram novas sugestões de IA.
`prepare_sample.py` recompõe o mesmo recorte e recusa sobrescrever uma versão
congelada diferente. O script `mapping/build_sample_v1.py` materializa a resposta
autorada nesta sessão; suas decisões literais não são uma implementação de IA.
Os testes que usam fixtures artificiais validam software, não acurácia semântica.

## Revisão do critério — v2

O usuário definiu separar assunto/objeto, tarefa realmente exigida e problemas de
uso. Evidência de uma parte explícita da competência pode sustentar sugestão;
coincidência temática não basta e simplicidade cognitiva não é veto. Os julgamentos
por questão continuam sendo dos agentes, não decisões pedagógicas do usuário.

Leia a [amostra v2](mapping/amostra_v2.md), o
[comparativo por item](mapping/changes_v1_v2.md) e a
[crítica v2](mapping/review/critica_v2.md). A v1 permanece preservada. No ITM-20025,
o objeto pode estar sustentado enquanto a competência continua pendente. No
ITM-20018, vínculo sugerido e validade da alternativa B são estados separados.
Nenhum item foi declarado pronto para prova ou validado pedagogicamente.

Verificação formal v2, a partir desta pasta:

```powershell
python mapping/validate_v2.py
python -m unittest discover -s mapping -p test_validate_v2.py -v
```

Isso confere respostas salvas e regras; **não executa uma nova inferência de IA**.
O [fluxo mínimo reproduzível](docs/fluxo_minimo_proposto.md) é uma proposta concreta
para implementar a CLI com mock/replay e provedor real intercambiáveis. Foi proposto naquela rodada; o modo replay agora está implementado, conforme
a seção de fluxo local no início. O adaptador real continua não implementado. A [conferência de API](docs/confirmacao_api_2026-10-14.md)
separa oferta pública confirmada de acesso na conta não testado e apresenta a
aritmética revisada. Nenhum gasto de API foi autorizado ou realizado.


