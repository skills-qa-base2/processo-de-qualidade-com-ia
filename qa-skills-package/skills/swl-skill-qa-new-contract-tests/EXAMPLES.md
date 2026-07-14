## Jr
**Cenário:** QA júnior na "AgroConecta" (marketplace agro B2B fictício) precisa do teste de contrato do endpoint `GET /produtos/{id}`, com spec OpenAPI já publicada.
**Input:** "Gera o teste de contrato pro endpoint GET /produtos/{id}, o schema tá no nosso arquivo openapi.yaml."
**Saída esperada:** A skill lê o schema real, valida status 200 com os campos definidos (tipos, obrigatoriedade), e gera o teste com a biblioteca de validação de schema do stack detectado.

## Pl
**Cenário:** QA pleno na "LogiFrete" (transportadora fictícia) precisa de testes de contrato entre o serviço de rastreamento e o app do motorista, mas não está confirmado se o time usa Pact ou só validação de schema.
**Input:** "Preciso de testes de contrato entre o serviço de rastreamento e o app do motorista. Temos vários consumidores desse serviço mas não sei se já usamos Pact."
**Saída esperada:** A skill identifica múltiplos consumidores (indício de contrato consumer-driven), mas como não encontra Pact nem Spring Cloud Contract configurado, pergunta se deve introduzir uma ferramenta consumer-driven ou se validação de schema simples já resolve por ora — em vez de decidir sozinha.

## Sr
**Cenário:** Na "PagaFácil" (fintech de pagamentos fictícia), o time quer só "documentar o contrato atual" a partir de uma resposta de exemplo colada no Slack por um dev, sem OpenAPI nem Pact publicado, pra ganhar tempo antes de uma integração com parceiro externo.
**Input:** cola uma resposta JSON de exemplo do endpoint de conciliação e pede pra gerar o teste "baseado nesse exemplo mesmo".
**Saída esperada:** A skill não gera o teste a partir da resposta isolada — um campo que aparece como `null` nesse exemplo específico pode ser opcional ou pode ser obrigatório-mas-vazio-nesse-caso, e a diferença importa pra quem for construir a integração em cima. Pede a especificação real antes de codificar qualquer validação, já que o parceiro externo vai confiar nesse teste como se fosse o contrato oficial.
