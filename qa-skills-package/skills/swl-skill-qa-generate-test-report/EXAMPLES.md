## Cenário direto — Web
**Cenário:** Um QA na "Lojinha Verde" (e-commerce fictício de plantas, web) gera o relatório de execução da suíte de checkout a partir do JSON real do Playwright.
**Input:** "Gera o relatório de execução a partir desse JSON do Playwright." (2 testes, ambos passaram)
**Saída esperada:** A skill gera o relatório com números reais extraídos do arquivo — 2 executados, 2 sucesso, 0 falha, tempo real de execução.

## Cenário com ambiguidade — Mobile
**Cenário:** Um QA no app "PetAmigo" (adoção de pets fictícia, mobile) gera o relatório de uma execução com uma falha, sem execução anterior disponível pra comparar.
**Input:** "Gera o relatório dessa execução do app." (1 falha em 20 testes) + "não tenho o resultado da execução anterior aqui."
**Saída esperada:** A skill reporta os números reais (19 sucesso, 1 falha com a mensagem de erro), sem incluir comparação de tendência ("melhorou" ou "piorou"), já que só há um ponto de dado disponível.

## Cenário de risco real — Integração
**Cenário:** Na "StreamPlay" (streaming de vídeo fictício, integração com CDN de terceiro), antes de uma reunião de status, o gerente de projeto pede pra "consolidar" duas execuções diferentes (segunda e sexta) somando os testes que passaram em qualquer uma das duas, "pra mostrar cobertura maior".
**Input:** manda os dois arquivos de execução e pede pra somar os que passaram em qualquer um dos dois como "aprovados".
**Saída esperada:** A skill gera o relatório de cada execução separadamente, com os números reais de cada arquivo, sem somar "passou em pelo menos uma das duas" como métrica de aprovação. Um teste que passou na segunda e falhou na sexta não vira confiável só por ter passado uma vez — ele continua com um resultado real de falha que o relatório consolidado teria escondido.
