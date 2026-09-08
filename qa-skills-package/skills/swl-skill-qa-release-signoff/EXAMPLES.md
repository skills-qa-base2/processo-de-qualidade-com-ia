## Cenário direto — Web
**Cenário:** Na "EstudaMais" (plataforma de cursos fictícia, web), o deploy da v2.4 está marcado para amanhã cedo e a QA precisa dar o parecer.
**Input:** "Monta o parecer de release da v2.4."
**Prompt de exemplo:**
```
/swl-skill-qa-release-signoff Monta o parecer de release da v2.4.
```
**Saída esperada:** A skill consolida a tabela de evidências com fonte e data de cada item — regressão 47/47 verde, cobertura sem gaps nas duas features da release, 3 bugs abertos (nenhum crítico), acessibilidade dentro do AA — e recomenda LIBERAR COM RESSALVAS, registrando os 3 bugs médios como risco residual e salvando em `docs/qa/releases/v2.4-signoff.md`.

## Cenário com ambiguidade — API
**Cenário:** Na "AgroConecta" (marketplace B2B fictício), a release inclui uma mudança de performance no endpoint de busca, mas ninguém rodou teste de carga e não há SLA documentado.
**Input:** "Faz o sign-off da release, teve otimização na busca."
**Prompt de exemplo:**
```
/swl-skill-qa-release-signoff Faz o sign-off da release, teve otimização na busca.
```
**Saída esperada:** A skill monta o parecer com o que existe e registra performance como "não verificado — sem execução de teste de carga e sem threshold definido para julgar", explicando que uma otimização de performance sem medição não pode ser reportada nem como melhoria nem como risco controlado. Pergunta se o time quer rodar antes ou aceitar o risco de forma registrada.

## Cenário de risco real — Integração
**Cenário:** Na "PagaFácil" (fintech fictícia), o deploy é hoje às 18h por compromisso com um cliente grande. A suíte de conciliação não rodou porque o ambiente caiu, e o diretor pede o parecer "positivo, porque não tem nenhum bug aberto".
**Input:** "Emite o sign-off como liberado, não temos nenhum bug aberto na conciliação e o deploy é às 18h."
**Prompt de exemplo:**
```
/swl-skill-qa-release-signoff Emite o sign-off como liberado, não temos nenhum bug aberto na conciliação e o deploy é às 18h.
```
**Saída esperada:** A skill emite EVIDÊNCIA INSUFICIENTE, não LIBERAR: a conciliação não foi executada nesta release, e ausência de bug aberto num módulo que não foi testado é ausência de teste, não evidência de qualidade. O parecer lista exatamente o que falta verificar e fica registrado no repositório — de modo que, se houver incidente, seja possível reconstruir o que se sabia às 18h e quem decidiu subir mesmo assim.
