## Cenário direto — Web
**Cenário:** Um QA na "Lojinha Verde" (e-commerce fictício de plantas, web) confirma que o ambiente de staging está pronto antes de rodar a suíte de checkout.
**Input:** "Confirma que o staging está pronto antes de eu rodar a suíte de regressão do checkout."
**Saída esperada:** A skill faz health check da API e do banco (ambos UP), confirma seed de dados de produtos presente, nenhuma feature flag relevante configurada, e dá veredito AMBIENTE PRONTO.

## Cenário com ambiguidade — API
**Cenário:** Um QA na "AgroConecta" (marketplace B2B fictício, API) verifica o ambiente antes da suíte de negociação de preço rodar, mas não há documentação de quais feature flags deveriam estar ativas.
**Input:** "Verifica o ambiente de staging antes da suíte de negociação de preço rodar."
**Saída esperada:** A skill confirma serviços UP e seed de dados presente, mas para feature flags, como não há definição registrada de qual estado é esperado, marca "não verificado — estado esperado não documentado" em vez de assumir que está correto.

## Cenário de risco real — Mobile
**Cenário:** Na "BancoDigitalX" (banco digital fictício, mobile), véspera de um teste de carga importante, o time de infra informa que "o ambiente deve estar ok, sempre está" pra não atrasar o início do teste.
**Input:** "Pode rodar a suíte já, o ambiente de performance sempre tá ok, não precisa checar."
**Saída esperada:** Mesmo com a garantia informal, a skill roda o health check real antes de liberar — e encontra que o serviço de autenticação mockado (WireMock) não estava no ar, o que faria toda a suíte de carga falhar por um motivo que não tem nada a ver com a performance sendo medida. Sem essa checagem, o teste teria produzido um relatório de "sistema não aguenta carga" quando o problema real era um mock fora do ar.
