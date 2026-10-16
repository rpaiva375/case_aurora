# Verificação de portabilidade — fechamento

Executada por outro agente em 15/10/2026. Cópia isolada em diretório temporário, excluindo `runs`, caches, `.git`, ambientes e `node_modules`; incluiu fontes em `output/originals`, rubricas e respostas gravadas. Não alterou artefatos congelados.

## Ambiente e comandos

Windows, Python 3.12.14, somente biblioteca padrão. Interpretador disponível nesta máquina: `C:\Users\rodri\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`. Um Python instalado é requisito; o pacote não inclui interpretador. A partir da cópia:

```powershell
python -B run_local.py --source output/originals --output runs/teste_novo
python -B demo.py --results runs/teste_novo/results.json --output runs/demo_nova
```

Os processos executaram com um `sitecustomize` de teste que bloqueia eventos `socket.*` e abertura de arquivos nas pastas originais do projeto, em `financial_care` e em `Downloads`. Esse bloqueio é instrumento desta verificação, não funcionalidade nova do produto. Não houve acesso a API, credenciais ou inferência.

## Evidência observada

Ambos os comandos terminaram com código 0 e stderr vazio. CLI: 68 registros, seis analisados por replay, 54 pendentes, oito reservados, zero erros. Nos seis: duas sugestões, um objeto sustentado com competência pendente e três abstenções. Demo: três eventos, todos `current`, `ready_for_exam=false`; 85 arquivos protegidos idênticos antes/depois. A contagem menor que históricos anteriores decorre da cópia sem caches, não de perda de registros.

Foram conferidos 25 links locais entre README, roteiro, conferência do usuário e guia da avaliação; nenhum destino faltante. Logs estruturados estão em [fechamento_portabilidade.json](fechamento_portabilidade.json). Caminho temporário no log é proveniência do teste, não dependência. A cópia temporária foi removida após retenção da evidência.

## Limites

Verifica execução local em uma cópia Windows com o mesmo interpretador disponível, não instalação em todas as plataformas. O alias `python` desta máquina não substitui a necessidade de Python instalado. Os oito casos têm inferência nova preservada em `evaluation/`, mas a CLI continua reservando-os: não agrega essa rodada aos seis replays. A conferência do usuário permanece complementar e restrita a dois casos. Não houve nova análise semântica, validação pedagógica, liberação para prova nem medição de economia.

A primeira tentativa de criar a cópia falhou por permissão do sandbox antes da execução; a repetição com execução autorizada no Temp concluiu. Nenhum bloqueio funcional foi identificado no percurso testado.
