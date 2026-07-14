## Cenário direto — Web
**Cenário:** Um QA na "Lojinha Verde" (e-commerce fictício de plantas, web) encontra um bug claro no botão de checkout.
**Input:** "Encontrei um bug: o botão de finalizar compra não faz nada quando clico duas vezes rápido."
**Saída esperada:** A skill gera relatório estruturado com passos exatos, severidade Alta (bloqueia fluxo principal), resultado esperado vs. obtido claros.

## Cenário com ambiguidade — API
**Cenário:** Um QA na "PagaFácil" (fintech de pagamentos fictícia, API) reporta um bug sem informar o navegador ou dispositivo usado.
**Input:** "A tela de extrato trava às vezes." (sem dizer em qual navegador ou dispositivo)
**Saída esperada:** A skill gera o relatório com os passos que foram informados, mas marca o campo Ambiente como "não informado — confirmar navegador/dispositivo com quem reportou", em vez de deixar em branco ou assumir o mais comum.

## Cenário de risco real — Mobile
**Cenário:** Na "ClickIngressos" (venda de ingressos fictícia, app mobile), dias antes de um lançamento, o suporte pede pra abrir um bug urgente de "ingresso duplicado" mandando só um print da tela de confirmação do app, sem descrever os passos nem confirmar se conseguiu reproduzir de novo.
**Input:** manda um print de uma tela mostrando dois ingressos iguais na conta do usuário, pedindo prioridade máxima, sem mais detalhes.
**Saída esperada:** A skill monta o relatório com o que o print realmente mostra, mas deixa "Passos para reproduzir" e "Resultado esperado" como pendentes de confirmação com quem reportou, em vez de reconstruir uma sequência plausível de toques. Um bug de duplicação tratado como urgente com passos inventados pode levar o time a corrigir a causa errada enquanto o ingresso real continua duplicando.
