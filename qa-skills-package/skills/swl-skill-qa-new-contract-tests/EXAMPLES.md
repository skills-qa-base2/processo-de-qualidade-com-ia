## Cenário direto — API
**Cenário:** Um QA na "AgroConecta" (marketplace agro B2B fictício, API) precisa do teste de contrato do endpoint `GET /produtos/{id}`, com spec OpenAPI já publicada.
**Input:** "Gera o teste de contrato pro endpoint GET /produtos/{id}, o schema tá no nosso arquivo openapi.yaml."
**Saída esperada:** A skill lê o schema real, valida status 200 com os campos definidos (tipos, obrigatoriedade), e gera o teste com a biblioteca de validação de schema do stack detectado.

## Cenário com ambiguidade — API
**Cenário:** Um QA na "LogiFrete" (transportadora fictícia, API) precisa de testes de contrato entre o serviço de rastreamento e seus múltiplos consumidores (app do motorista, painel do cliente), mas o projeto não tem nenhuma ferramenta de contrato consumer-driven configurada ainda.
**Input:** "Preciso de testes de contrato entre o serviço de rastreamento e seus consumidores. Temos vários consumidores desse serviço mas não sei se já usamos Pact."
**Saída esperada:** A skill identifica múltiplos consumidores — sinal claro de que o cenário pede contrato consumer-driven (Pact) em vez de só validação de schema — mas como não encontra Pact nem Spring Cloud Contract configurado no projeto, pergunta se deve introduzir a ferramenta ou se o time prefere só validação de schema por ora, em vez de decidir sozinha.

## Cenário de risco real — API
**Cenário:** Na "PagaFácil" (fintech de pagamentos fictícia, API), o time quer só "documentar o contrato atual" a partir de uma resposta de exemplo colada no Slack por um dev, sem OpenAPI nem Pact publicado, pra ganhar tempo antes de uma integração com parceiro externo.
**Input:** cola uma resposta JSON de exemplo do endpoint de conciliação e pede pra gerar o teste "baseado nesse exemplo mesmo".
**Saída esperada:** A skill não gera o teste a partir da resposta isolada — um campo que aparece como `null` nesse exemplo específico pode ser opcional ou pode ser obrigatório-mas-vazio-nesse-caso, e a diferença importa pra quem for construir a integração em cima. Pede a especificação real (via schema OpenAPI ou contrato Pact já publicado) antes de codificar qualquer validação, já que o parceiro externo vai confiar nesse teste como se fosse o contrato oficial.
