## Cenário direto — Mobile
**Cenário:** QA júnior no app do entregador da "RotaCerta" (logística fictícia) precisa automatizar o cenário de login válido, com Playwright já configurado pro app híbrido.
**Input:** "Gera a automação do cenário de login válido, já temos o cenário BDD pronto em features/login.feature."
**Saída esperada:** A skill detecta Playwright via CLAUDE.md, gera o teste reutilizando o `LoginPage` já existente, com seletores estáveis, e marca `generated-by-ai: pending-review`.

## Cenário com ambiguidade — Web
**Cenário:** QA pleno na "ContaCerta" (contabilidade SaaS B2B fictícia, web) precisa automatizar o cenário de emissão de nota fiscal, mas não está claro se deve reutilizar um Page Object existente ou criar um novo componente de API.
**Input:** "Automatiza o cenário de emissão de nota fiscal. Temos um NotaFiscalPage mas não sei se ele cobre a parte de API que valida o status."
**Saída esperada:** A skill reutiliza o `NotaFiscalPage` existente para a parte de UI, mas para a validação de status via API, como não encontra um componente equivalente já existente, pergunta se deve criar um novo ou se já existe em outro lugar do projeto — em vez de duplicar sem confirmar.

## Cenário de risco real — API
**Cenário:** Na "ClickIngressos" (venda de ingressos online fictícia, API de alta concorrência), o time sob pressão de sprint pede pra já marcar os testes gerados na camada de API como `generated-by-ai: reviewed` direto, "porque vamos revisar depois".
**Input:** "Gera a automação da compra de ingresso e já marca como reviewed, revisamos amanhã, precisamos fechar a sprint hoje."
**Saída esperada:** A skill gera o teste normalmente, mas marca `generated-by-ai: pending-review`, não `reviewed`. Marcar como revisado sem revisão real é diferente de só chegar atrasado numa sprint — é a etiqueta que faz o time de revisão de PR parar de olhar esse teste com atenção, então ela só muda quando alguém de fato ler o código gerado.
