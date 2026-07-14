## Cenário direto — Integração
**Cenário:** Um QA na "LogiFrete" (transportadora fictícia) analisa a suíte de integração com o sistema de rastreamento de um parceiro externo, que às vezes falha sem motivo aparente.
**Input:** "Analisa essa suíte de integração com o rastreamento, ela às vezes falha sem motivo aparente."
**Prompt de exemplo:**
```
/swl-skill-qa-check-flakiness Analisa essa suíte de integração com o rastreamento, ela às vezes falha sem motivo aparente.
```
**Saída esperada:** A skill identifica um `waitForTimeout(3000)` na linha X, sugere trocar por espera condicional ao estado da resposta da API do parceiro.

## Cenário com ambiguidade — Mobile
**Cenário:** Um QA na "SaúdeJá" (telemedicina fictícia) tem testes de agendamento no app mobile que parecem depender de ordem de execução, mas não há histórico de execução disponível pra confirmar.
**Input:** "Os testes de agendamento do app falham quando rodam em paralelo, mas só às vezes. Não tenho o histórico de execução do CI à mão."
**Prompt de exemplo:**
```
/swl-skill-qa-check-flakiness Os testes de agendamento do app falham quando rodam em paralelo, mas só às vezes. Não tenho o histórico de execução do CI à mão.
```
**Saída esperada:** A skill identifica na análise estática uma variável compartilhada entre dois testes (indício claro de dependência de ordem), mas para outro trecho suspeito, sem histórico disponível, classifica como "padrão de risco, não confirmado como causa da falha real" em vez de afirmar que é a causa.

## Cenário de risco real — Web
**Cenário:** Na "ClickIngressos" (venda de ingressos, alta demanda, web), dias antes de um lançamento, o tech lead pede pra só marcar a suíte inteira como "flaky, ignorar por enquanto" pra não travar o deploy, já que "sempre foi meio instável mesmo".
**Input:** "A suíte de compra de ingresso está instável há semanas, só marca tudo como flaky e segue com o deploy, não temos tempo agora."
**Prompt de exemplo:**
```
/swl-skill-qa-check-flakiness A suíte de compra de ingresso está instável há semanas, só marca tudo como flaky e segue com o deploy, não temos tempo agora.
```
**Saída esperada:** A skill analisa arquivo por arquivo em vez de aceitar o rótulo de largada, e encontra que boa parte dos testes usa seletor por classe CSS de estilo, que muda a cada deploy de design. Não é instabilidade aleatória — é um padrão previsível quebrando toda vez que o time de design mexe no CSS, e rotular isso como "flaky" deixaria o mesmo problema voltando no próximo deploy.
