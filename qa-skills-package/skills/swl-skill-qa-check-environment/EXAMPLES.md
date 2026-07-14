## Jr
**Cenário:** QA júnior na "ContaCerta" (contabilidade SaaS fictícia) confirma que o ambiente de homologação da API está pronto antes de rodar a suíte de nota fiscal.
**Input:** "Confirma que o ambiente de homologação está pronto antes de eu rodar a suíte de nota fiscal."
**Saída esperada:** A skill faz health check da API e do banco (ambos UP), confirma seed de dados de notas fiscais presente, nenhuma feature flag relevante configurada, e dá veredito AMBIENTE PRONTO.

## Pl
**Cenário:** QA pleno na "AgroConecta" (marketplace B2B fictício) verifica o ambiente antes da suíte de negociação de preço rodar, mas não há documentação de quais feature flags deveriam estar ativas.
**Input:** "Verifica o ambiente de staging antes da suíte de negociação de preço rodar."
**Saída esperada:** A skill confirma serviços UP e seed de dados presente, mas para feature flags, como não há definição registrada de qual estado é esperado, marca "não verificado — estado esperado não documentado" em vez de assumir que está correto.

## Sr
**Cenário:** Na "BancoDigitalX" (banco digital fictício), véspera de um teste de carga importante, o time de infra informa que "o ambiente deve estar ok, sempre está" pra não atrasar o início do teste.
**Input:** "Pode rodar a suíte já, o ambiente de performance sempre tá ok, não precisa checar."
**Saída esperada:** Mesmo com a garantia informal, a skill roda o health check real antes de liberar — e encontra que o serviço de autenticação mockado (WireMock) não estava no ar, o que faria toda a suíte de carga falhar por um motivo que não tem nada a ver com a performance sendo medida. Sem essa checagem, o teste teria produzido um relatório de "sistema não aguenta carga" quando o problema real era um mock fora do ar.
