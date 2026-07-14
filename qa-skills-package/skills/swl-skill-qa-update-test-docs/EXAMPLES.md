## Cenário direto — Web
**Cenário:** QA júnior na "Lojinha Verde" (e-commerce fictício de plantas, web) atualiza a documentação depois que a branch adicionou um cenário de cupom de desconto.
**Input:** "Atualiza a documentação de testes com base nessa branch que adicionou o cenário de cupom."
**Saída esperada:** A skill atualiza o mapa de cobertura incluindo o novo cenário, mantendo a estrutura e o tom já usados no README de automação.

## Cenário com ambiguidade — Integração
**Cenário:** QA pleno na "LogiFrete" (transportadora fictícia) atualiza a documentação depois que a branch removeu um cenário de cálculo de frete considerado obsoleto.
**Input:** "Atualiza a documentação, removemos um cenário de frete que não existe mais."
**Saída esperada:** A skill atualiza o que a branch de fato mudou, mas antes de remover a entrada do glossário de cenários, verifica se ele ainda aparece em alguma suíte ativa não tocada nesta branch — encontra que ainda é referenciado num teste de regressão separado, mantém a entrada e sinaliza a inconsistência em vez de apagar.

## Cenário de risco real — Mobile
**Cenário:** Na "BancoDigitalX" (banco digital fictício, mobile), numa reorganização de pastas do app, o tech lead pede pra "limpar a documentação toda e recomeçar do zero", já que "ninguém mais usa a estrutura antiga mesmo".
**Input:** "Pode limpar toda a documentação de testes antiga e escrever do zero, ninguém usa mais aquilo."
**Saída esperada:** A skill atualiza o que mudou nesta branch, mas não apaga as seções de cenários ainda ativos na suíte atual só porque a reorganização de pastas mudou onde os arquivos vivem. Um cenário de aprovação de transferência documentado há dois anos continua rodando no CI todo dia, mesmo com a pasta em que foi originalmente descrito tendo sido reorganizada.
