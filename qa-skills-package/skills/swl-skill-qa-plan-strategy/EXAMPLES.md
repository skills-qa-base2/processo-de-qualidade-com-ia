## Cenário direto — API
**Cenário:** Um QA recém-chegado na "AgroConecta" (marketplace agro B2B fictício, API + integrações com ERPs de fornecedores) percebe que nunca houve uma estratégia de teste formal documentada.
**Input:** "Nunca tivemos uma estratégia de teste formal aqui na AgroConecta. Pode me ajudar a definir uma?"
**Prompt de exemplo:**
```
/swl-skill-qa-plan-strategy Nunca tivemos uma estratégia de teste formal aqui na AgroConecta. Pode me ajudar a definir uma?
```
**Saída esperada:** A skill lê o CLAUDE.md (ainda incompleto) e faz as 5 perguntas estruturadas. O QA responde todas com clareza (monolito com integrações externas, sem QA dedicado ainda, envolvido só na entrega, sistema não é crítico financeiramente, existe ambiente de staging). A skill propõe uma pirâmide balanceada (não 100% E2E) e gera `docs/qa/estrategia-teste.md`.

## Cenário com ambiguidade — Web
**Cenário:** Um QA na "EstudaMais" (plataforma de cursos online fictícia, web) responde às perguntas, mas não tem certeza se existe massa de dados própria de teste.
**Input:** responde as 4 primeiras perguntas com segurança, mas diz "não sei se temos massa de dados própria — às vezes usamos uma cópia de produção mascarada".
**Prompt de exemplo:**
```
/swl-skill-qa-plan-strategy Não sei se temos massa de dados própria — às vezes usamos uma cópia de produção mascarada.
```
**Saída esperada:** A skill registra as 4 respostas normalmente, e para a pergunta 5 marca como "a confirmar" em vez de assumir que existe massa fictícia de verdade — uma cópia de produção mascarada não é necessariamente massa de teste fictícia, e a skill sinaliza isso como risco em aberto em vez de tratar como resposta dada.

## Cenário de risco real — Mobile
**Cenário:** Na "BancoDigitalX" (banco digital fictício, app mobile + API), a diretoria pede uma estratégia de teste pronta pra apresentar amanhã, e o QA, sem tempo de entrevistar o time todo, pede pra skill "preencher com o que é padrão de mercado pra banco digital".
**Input:** "Preciso da estratégia pronta pra reunião de amanhã, pode assumir as respostas típicas de um banco digital?"
**Prompt de exemplo:**
```
/swl-skill-qa-plan-strategy Preciso da estratégia pronta pra reunião de amanhã, pode assumir as respostas típicas de um banco digital?
```
**Saída esperada:** Mesmo com o pedido explícito de assumir respostas, a skill não inventa nenhuma das 5 perguntas — registra cada uma como "a confirmar" e lista como risco em aberto no documento gerado. A reunião de amanhã sai com um documento que mostra exatamente o que ainda não foi levantado, em vez de uma estratégia com aparência de pronta que ninguém no time realmente validou.
