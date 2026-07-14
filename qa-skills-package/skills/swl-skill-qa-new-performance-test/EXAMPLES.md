## Cenário direto — Web
**Cenário:** QA júnior na "ClickIngressos" (venda de ingressos online fictícia, web) quer um smoke test simples do endpoint de listagem de eventos, com k6 já configurado.
**Input:** "Preciso de um teste de performance smoke pro endpoint GET /eventos, já usamos k6."
**Saída esperada:** A skill detecta k6, confirma que é smoke test (poucos usuários virtuais, só validar que o script roda), gera o script parametrizado e salva em `tests/performance/`.

## Cenário com ambiguidade — Integração
**Cenário:** QA pleno na "StreamPlay" (streaming de vídeo fictício, com integração a um CDN de terceiro) quer testar a API de início de reprodução, mas só definiu o tipo de teste (load), sem os thresholds.
**Input:** "Quero um teste de carga (load) pro endpoint de iniciar reprodução, mas ainda não sei os números de threshold."
**Saída esperada:** A skill gera o script como load test conforme pedido, mas para os thresholds (p95, taxa de erro, RPS) marca "a confirmar com o responsável pelo SLA" em vez de preencher com números de exemplo.

## Cenário de risco real — Mobile
**Cenário:** Na "BancoDigitalX" (banco digital fictício, mobile), o time de infra pede um teste de stress pro endpoint de autenticação do app antes de um evento de marketing com pico esperado de acessos, mas ninguém do time de negócio respondeu quais números de SLA valem, e o prazo é hoje.
**Input:** "Precisamos rodar um teste de stress hoje mesmo pro pico do evento, mas ninguém me respondeu ainda o SLA. Pode estimar um número razoável pra gente não atrasar?"
**Saída esperada:** Mesmo com o prazo apertado e o pedido direto de estimar, a skill gera o script de stress funcional, mas deixa os thresholds marcados como pendentes — um teste "aprovado" contra um número inventado pela própria skill não prova nada sobre o sistema aguentar o pico real do evento, só prova que ele aguenta o número que foi chutado.
