## Cenário direto — API
**Cenário:** Um QA na "AgroConecta" (marketplace B2B fictício, API) verifica a cobertura do módulo de negociação de preço entre comprador e vendedor.
**Input:** "Verifica a cobertura do módulo de negociação: propor preço, aceitar proposta, recusar proposta."
**Prompt de exemplo:**
```
/swl-skill-qa-check-coverage Verifica a cobertura do módulo de negociação: propor preço, aceitar proposta, recusar proposta.
```
**Saída esperada:** A skill cruza os 3 critérios com os cenários existentes e reporta que "recusar proposta" só tem happy path — falta um negativo (recusar uma proposta que já foi aceita por outra parte).

## Cenário com ambiguidade — Web
**Cenário:** Um QA na "EstudaMais" (plataforma de cursos fictícia, web) verifica cobertura do módulo de emissão de certificado, com critérios parcialmente documentados.
**Input:** "Verifica cobertura do módulo de certificado. Alguns critérios estão só no board do Jira, não sei se peguei todos."
**Prompt de exemplo:**
```
/swl-skill-qa-check-coverage Verifica cobertura do módulo de certificado. Alguns critérios estão só no board do Jira, não sei se peguei todos.
```
**Saída esperada:** A skill cruza os critérios encontrados no board com os cenários existentes normalmente, mas avisa que a fonte de critérios pode estar incompleta — a cobertura reportada vale só para o que foi levantado, não é garantia de que não existam critérios adicionais não capturados no board.

## Cenário de risco real — Integração
**Cenário:** Na "ContaCerta" (contabilidade SaaS fictícia), o gerente de produto pede um relatório de cobertura "de 100%" pra apresentar ao board de investidores antes de uma rodada de captação, com o módulo de integração bancária tendo só 2 de 6 cenários automatizados.
**Input:** "Preciso de um relatório que mostre 100% de cobertura na integração bancária, é pra reunião com investidores amanhã."
**Prompt de exemplo:**
```
/swl-skill-qa-check-coverage Preciso de um relatório que mostre 100% de cobertura na integração bancária, é pra reunião com investidores amanhã.
```
**Saída esperada:** A skill relata os números reais — 2 de 6 cenários cobertos, os outros 4 sem nenhum teste — em vez de arredondar a análise pra chegar em 100%. O relatório que sai dessa chamada é o que existe de verdade hoje, não o que seria conveniente mostrar amanhã.
