## Cenário direto — Web
**Cenário:** Um QA na "Lojinha Verde" (e-commerce de plantas, web) recebe um critério de aceite simples de busca de produto.
**Input:** "Critério: usuário busca por nome de produto e vê os resultados correspondentes."
**Saída esperada:** A skill gera `Funcionalidade: Busca de produtos` com cenário happy path, um negativo (busca sem resultado) e um edge case (busca com caractere especial).

## Cenário com ambiguidade — Mobile
**Cenário:** Um QA no app mobile da "TarefaCerta" (gestão de tarefas fictícia) recebe um critério de assinatura de plano com regra de desconto pouco clara.
**Input:** "Critério: usuário assina o plano premium e, se for a segunda assinatura do mesmo usuário, recebe desconto." (sem informar o percentual)
**Saída esperada:** A skill gera o cenário happy path da assinatura simples e um Esquema do Cenário pro desconto, mas deixa o percentual como `<percentual_a_confirmar>` nos Exemplos, em vez de inventar um número plausível.

## Cenário de risco real — API
**Cenário:** Na "PagaFácil" (fintech de pagamentos, API), o critério de aceite de estorno descreve três regras diferentes numa frase só (prazo de estorno, taxa de reversão e notificação ao usuário), e o PO pede "um cenário só, pra não ficar grande".
**Input:** critério de aceite denso com 3 regras numa frase, e pedido explícito de resumir em um cenário único.
**Saída esperada:** Mesmo com o pedido de simplificar, a skill gera 3 cenários separados — um `Quando` que testa prazo, taxa e notificação ao mesmo tempo não isola qual das três falhou se o teste quebrar. Resumir do jeito pedido deixaria a falha sem indicar qual regra de negócio especificamente parou de funcionar.
