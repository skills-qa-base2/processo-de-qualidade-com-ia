## Cenário direto — Mobile
**Cenário:** QA júnior no app "PetAmigo" (adoção de pets fictícia) faz sua primeira sessão exploratória na tela de busca de pets.
**Input:** "Quero fazer uma sessão exploratória na busca de pets, tenho 1 hora."
**Saída esperada:** A skill define o charter (missão: busca por filtros combinados; escopo: só a tela de busca; tempo-caixa: 60 min), conduz e documenta os achados reais da sessão.

## Cenário com ambiguidade — Web
**Cenário:** QA pleno na "AgroConecta" (marketplace B2B fictício, web) conduz sessão exploratória no checkout, mas é interrompido antes de testar uma parte do fluxo planejado.
**Input:** relata que testou boa parte do fluxo de negociação de preço, mas foi interrompido antes de testar o fluxo de aprovação em duas etapas.
**Saída esperada:** A skill documenta as áreas realmente cobertas (negociação de preço) e registra explicitamente, em "cobertura percebida", que o fluxo de aprovação em duas etapas não foi exercitado por falta de tempo — sem incluir esse fluxo em "áreas cobertas" mesmo fazendo parte do charter original.

## Cenário de risco real — Integração
**Cenário:** Na "RH Fácil" (sistema de RH fictício, com integração ao processador de folha de pagamento externo), o QA sênior conduz uma sessão de 45 minutos na tela de folha de pagamento, e o gerente pede pro relatório dizer que "o módulo de folha inteiro foi testado" pra justificar a liberação do release.
**Input:** "Coloca no relatório que testamos o módulo de folha inteiro, deu pra ver bastante coisa nessa sessão."
**Saída esperada:** O relatório lista como "áreas cobertas" exatamente as três telas exercitadas (cálculo de horas extras, desconto de INSS, geração de holerite) — não o módulo inteiro, que também inclui rescisão e o envio ao processador externo de folha, nenhum dos dois tocados nesses 45 minutos. Um release liberado com base num relatório que diz "módulo inteiro testado" deixa ninguém sabendo que a integração de rescisão ficou sem nenhum teste, até um problema aparecer lá.
