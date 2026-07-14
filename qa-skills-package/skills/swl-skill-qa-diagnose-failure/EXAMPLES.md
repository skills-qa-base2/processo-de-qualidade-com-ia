## Cenário direto — Web
**Cenário:** Um QA na "Lojinha Verde" (e-commerce fictício de plantas, web) vê um teste de checkout falhar no CI com uma mensagem de assert clara.
**Input:** cola o log — o teste esperava "Pedido confirmado!" e recebeu "Pedido confirmado com sucesso!", porque a aplicação mudou o texto da mensagem.
**Prompt de exemplo:**
```
/swl-skill-qa-diagnose-failure O teste de checkout falhou no CI. Esperava "Pedido confirmado!" e recebeu "Pedido confirmado com sucesso!".
```
**Saída esperada:** A skill classifica como "teste mal escrito" (expectativa desatualizada), aponta a linha exata do assert, e sugere corrigir o texto esperado no teste.

## Cenário com ambiguidade — Integração
**Cenário:** Um QA na "PagaFácil" (fintech de pagamentos fictícia) tem um teste de integração com o serviço de notificação que falha 1 a cada 5 execuções no CI, sem mudança de código recente.
**Input:** cola o log de timeout na chamada ao serviço de notificação, mencionando que "já viu isso antes" mas sem dados de histórico completo.
**Prompt de exemplo:**
```
/swl-skill-qa-diagnose-failure O teste de integração com o serviço de notificação deu timeout de novo no CI. Já vi isso antes, mas não tenho um histórico completo das vezes anteriores.
```
**Saída esperada:** A skill nota o padrão intermitente, mas como o histórico de execução não foi fornecido de forma completa, marca como "possível flakiness, rastreamento incompleto" e recomenda coletar o histórico real via `swl-skill-qa-check-flakiness` antes de classificar definitivamente.

## Cenário de risco real — API
**Cenário:** Na "PagaFácil" (fintech de pagamentos fictícia, API), a equipe de infraestrutura explica que uma falha recorrente no fechamento de fatura em produção é "só instabilidade de rede", pedindo apenas retry no teste pra ele passar.
**Input:** descreve a pressão para classificar como "ambiente" e colar retry, mas mostra um log onde o valor da fatura calculado já vem errado (arredondamento) antes do timeout aparecer.
**Prompt de exemplo:**
```
/swl-skill-qa-diagnose-failure A infra disse que essa falha recorrente no fechamento de fatura é só instabilidade de rede e pediu pra só colocar retry no teste. Mas o log mostra o valor da fatura já calculado errado (parece arredondamento) antes do timeout aparecer — pode confirmar se é isso mesmo ou se é rede?
```
**Saída esperada:** A skill recusa classificar como ambiente/flaky só para o teste passar — aponta que o log mostra um valor de fatura incorreto antes do timeout, indicando bug real de arredondamento, não instabilidade de rede. Recomenda investigar a lógica de cálculo em vez de mascarar com retry: o timeout foi só o sintoma que apareceu primeiro no log, o valor da fatura já tinha saído errado duas linhas antes dele.
