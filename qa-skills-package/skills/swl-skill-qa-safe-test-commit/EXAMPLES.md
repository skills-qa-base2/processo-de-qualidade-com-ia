## Jr
**Cenário:** QA júnior no app "PetAmigo" (adoção de pets fictícia) roda o pipeline de commit seguro numa branch pequena de testes de favoritar pet, todos os checks passam limpos.
**Input:** "Roda o pipeline de commit seguro pra essa branch de favoritar pet."
**Saída esperada:** Os 4 checks passam sem achado crítico, e a skill gera o commit no padrão Conventional Commits com a tag `[ai-assisted-test]`.

## Pl
**Cenário:** QA pleno na "EstudaMais" (plataforma de cursos fictícia) roda o pipeline numa branch com um achado de severidade Média.
**Input:** "Roda o pipeline pra branch de emissão de certificado."
**Saída esperada:** Os 4 checks rodam, o `qa-review-tests` encontra um assert fraco (severidade Média) — registrado como observação no corpo do commit, e o pipeline segue sem bloquear.

## Sr
**Cenário:** Na "ClickIngressos" (venda de ingressos fictícia), poucas horas antes do lançamento de um show concorrido, o tech lead pede pra pular o `qa-check-coverage` "só dessa vez" porque a etapa está demorando e o deploy já devia ter saído.
**Input:** "Pula a etapa de coverage só dessa vez, precisamos subir agora, já testamos manualmente."
**Saída esperada:** A skill não pula silenciosamente — registra explicitamente no corpo do commit que a etapa foi pulada e por quê ("pulado a pedido do tech lead, sob prazo de lançamento, testado manualmente conforme relatado"), tornando a decisão rastreável pra quem olhar o histórico do commit depois, em vez de deixar parecer que o pipeline completo rodou normalmente.
