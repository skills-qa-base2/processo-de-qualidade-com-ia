## Cenário direto — Mobile
**Cenário:** QA júnior no app mobile "PetAmigo" (adoção de pets fictícia) revisa um teste gerado por IA de cadastro de pet pra adoção.
**Input:** "Revisa esse teste de cadastro de pet que a IA gerou."
**Saída esperada:** O nome do teste descreve o comportamento, os asserts validam o campo relevante, sem redundância — recomendação: manter.

## Cenário com ambiguidade — Web
**Cenário:** QA pleno na "AgroConecta" (marketplace B2B fictício, web) revisa um teste de listagem de fornecedores com nome genérico.
**Input:** "Revisa esse teste chamado 'test_listagem_2'."
**Saída esperada:** A skill sinaliza que o nome não descreve comportamento (deveria dizer o que está sendo validado), recomendação: ajustar o nome, mantendo o restante.

## Cenário de risco real — API
**Cenário:** Na "PagaFácil" (fintech de pagamentos fictícia, API), o QA sênior recebe 8 testes gerados por IA pro fluxo de estorno, já marcados como `generated-by-ai: reviewed`, com o tech lead pedindo "só confirma que tá tudo certo, é rotina".
**Input:** "Revisa esses 8 testes de estorno, já estão marcados como reviewed, é só formalidade."
**Saída esperada:** A skill revisa os 8 normalmente e aponta 2 com asserts fracos (só verificam que não lançou exceção, não que o valor do estorno está correto) — sem validar o marcador `reviewed` já presente. Nesses dois casos o marcador foi colocado antes de alguém checar se os asserts realmente provam o que o nome do teste promete, que é a mesma verificação que essa chamada acabou de fazer.
