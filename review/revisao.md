# Revisão técnica independente — etapa 1

Revisor: agente separado do autor da ingestão. Resultado: **nenhum achado bloqueante ou defeito material identificado na base entregue**. A revisão é técnica; não constitui validação pedagógica especializada nem demonstra ganho operacional.

Primeiro marco horário registrado durante a revisão: 14/10/2026 15:36:30 -03:00, após leitura inicial de código e README. Execução independente: 15:37:12 a 15:37:13 -03:00. Testes do autor concluídos até 15:37:21 -03:00. O tempo anterior ao primeiro marco não foi cronometrado e não deve ser inferido como zero. O relatório foi concluído em aproximadamente 15:38 -03:00.

## Método e evidência

Li `ingest.py`, `README.md` e testes. Comparei os arquivos efetivamente entregues em `output/` com as fontes externas, usando leitor CSV posicional e verificações próprias em `review/verify_independent.py`. Não usei a implementação para produzir os valores esperados das comparações da base. A implementação é chamada somente para os ensaios adversariais em memória. `verification.json` contém 1.568 asserções aprovadas e os horários exatos dessa execução. Adicionalmente, os 11 testes do autor passaram.

Comando reproduzível, a partir da raiz do workspace:

```powershell
& 'C:\Users\rodri\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' case_aurora/review/verify_independent.py
& 'C:\Users\rodri\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' case_aurora/test_ingest.py --source 'C:\Users\rodri\Downloads\pacote_candidato\pacote_candidato' -v
```

## O que passou

- Sete originais: hashes das fontes atuais, cópias e manifesto coincidem. As fontes permaneceram iguais entre início e fim do script independente. Isso confirma a igualdade com a captura da ingestão, não uma assinatura histórica externa anterior ao trabalho.
- CSVs: 68 itens, 69 observações de desempenho e 142 aplicações preservados na ordem original, com todos os campos brutos idênticos e esquema de dados correspondente. Nenhum registro foi removido, replicado ou consolidado.
- Auditoria: todos os registros padronizados são reconstruíveis a partir de `raw` pela sequência de eventos; todos os eventos referenciam registros existentes e regras cadastradas. São **358 eventos**: 136 inteiros + 204 decimais = 340 tipagens; 12 vazios para null; 2 hífens; 1 letra maiúscula; 1 remoção do prefixo `Alternativa`; 2 gabaritos não resolvidos. **Além desses eventos**, há 2 resoluções rastreáveis em `ementas_manifest.json`; elas não reescrevem a matriz.
- Valores numéricos: comparação independente com `Decimal` confirma valores e escala, inclusive frações de acerto. Ausências permanecem null. Semestres permanecem texto.
- Vínculos: cada associação existente foi conferida contra destino único no cadastro. Desempenho: 67 registros associados e 2 órfãos preservados (`ITM-10039`, `ITM-20011`). Aplicações: 142 associações. Nenhum vínculo curricular foi criado.
- `ITM-10066`: observações de 2024.1 e 2025.1 continuam separadas após padronizar o hífen. Não há grupos repetidos nas granularidades verificadas da amostra.
- Gabaritos numéricos de `ITM-10048` e `ITM-20021`: bruto preservado, canônico null, pendência explícita; nenhuma equivalência número/letra aplicada.
- Matriz preservada semanticamente; bytes originais também preservados. Ementas e fila mantidas integralmente. As duas referências de ementa resolvem por manifesto explícito para arquivos reais correspondentes.
- Desempenho e aplicações permanecem em arquivos separados. A implementação não faz cruzamento entre essas tabelas nem soma medidas através de junção multiplicativa.
- Exemplo conferido: `ITM-10066` tem 2 observações de desempenho e 2 aplicações. Uma junção direta apenas pelo ID produziria 4 linhas e repetiria cada observação duas vezes. A entrega mantém 2 registros em cada tabela; não foi gerada tabela plana para esta verificação.
- Ensaios adversariais próprios: cadastro adicional com ID vazio fica inválido e sem associação; colisão `ITM10041`/`ITM-10041` mantém linhas e bloqueia todas as associações afetadas; duplicata no mesmo semestre permanece e é sinalizada. São fixtures de software em memória, não evidência de qualidade pedagógica ou operacional.

## Pendências e limites

Há **17 ocorrências estruturais abertas**: 12 campos vazios, 2 gabaritos não resolvidos, 1 conjunto de alternativas iguais e 2 órfãos. Isso não significa 17 questões distintas. As ausências não foram imputadas e os órfãos não foram associados por aproximação.

A fila textual é preservada sem converter suas alegações em defeitos confirmados. Texto-base ausente, similaridade semântica, convenções numéricas e interpretação de “1–3 nós” continuam fora da conclusão técnica desta revisão. Revisão do candidato diante da matriz/evidências deverá ser distinguida de validação pedagógica especializada.

As verificações confirmam a amostra entregue. Não demonstram desempenho em 240 mil itens, governança de produção, imutabilidade de armazenamento ou melhoria operacional. Nenhuma dessas capacidades foi exigida para aceitar esta etapa.

## Achados por severidade

- Bloqueantes/altos: nenhum identificado.
- Médios/baixos com necessidade de correção nesta etapa: nenhum identificado.
- Limites documentados: processamento em memória, saída sem transação de diretório e ausência de avaliação semântica/pedagógica. Coerentes com o recorte; não são defeitos da base conferida.

Recomendação técnica: a base pode alimentar a próxima etapa após a revisão do usuário. Essa recomendação não aprova o mapeamento nem encerra as pendências.
