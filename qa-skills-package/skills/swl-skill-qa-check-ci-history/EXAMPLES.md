## Cenário direto — Web
**Cenário:** Na "EstudaMais" (plataforma de cursos fictícia, web), a suíte E2E do CI vive vermelha e o time quer saber quais testes são realmente instáveis.
**Input:** "Analisa o histórico do CI dos últimos 30 dias e me diz quais testes E2E são flaky."
**Prompt de exemplo:**
```
/swl-skill-qa-check-ci-history Analisa o histórico do CI dos últimos 30 dias e me diz quais testes E2E são flaky.
```
**Saída esperada:** A skill lê as execuções via `gh run list`, e separa: 2 flaky confirmados (passaram e falharam no mesmo commit), 1 quebrado desde um commit específico de duas semanas atrás, e o resto estável — deixando claro que o quebrado não é flakiness e precisa de correção, não de retry.

## Cenário com ambiguidade — API
**Cenário:** Na "AgroConecta" (marketplace B2B fictício), o CI foi migrado de Jenkins para GitHub Actions há oito dias e só há histórico curto na ferramenta nova.
**Input:** "Vê o histórico do CI e me diz se o teste de negociação de preço é flaky."
**Prompt de exemplo:**
```
/swl-skill-qa-check-ci-history Vê o histórico do CI e me diz se o teste de negociação de preço é flaky.
```
**Saída esperada:** A skill informa que só encontrou 6 execuções na janela disponível desde a migração, apresenta o que viu, e diz que a amostra é insuficiente para classificar como flaky — sugerindo buscar os artefatos do Jenkins antigo ou aguardar mais execuções, em vez de concluir a partir de duas falhas.

## Cenário de risco real — Integração
**Cenário:** Na "PagaFácil" (fintech fictícia), o teste de conciliação de estorno falhou em 4 das últimas 20 execuções, sempre em commits diferentes. O tech lead quer marcá-lo como flaky e ligar retry automático para destravar o pipeline antes do fechamento do mês.
**Input:** "Confirma que o teste de conciliação de estorno é flaky pra eu ligar retry nele, tá travando o pipeline."
**Prompt de exemplo:**
```
/swl-skill-qa-check-ci-history Confirma que o teste de conciliação de estorno é flaky pra eu ligar retry nele, tá travando o pipeline.
```
**Saída esperada:** A skill não confirma. As 4 falhas são em revisões diferentes e nenhuma revisão apresenta passa e falha simultâneos — o padrão é compatível com regressão real intermitente, não com flakiness. Encaminha para `swl-skill-qa-diagnose-failure`. Ligar retry num teste de conciliação financeira que está falhando de verdade é o mecanismo exato pelo qual o pipeline passa a esconder o bug que ele existia para pegar.
