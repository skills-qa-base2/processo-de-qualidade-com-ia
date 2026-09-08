## Cenário direto — Web
**Cenário:** Na "EstudaMais" (plataforma de cursos fictícia, web), a release da sexta tem 40 arquivos alterados e a suíte completa leva 3 horas — só há uma janela de 1 hora no ambiente de homologação.
**Input:** "Monta a regressão da release v2.4 comparando com a v2.3."
**Prompt de exemplo:**
```
/swl-skill-qa-select-regression-suite Monta a regressão da release v2.4 comparando com a v2.3.
```
**Saída esperada:** A skill mapeia os módulos impactados (matrícula e certificado), monta 12 cenários obrigatórios, 8 recomendados, lista as áreas fora do recorte, e fecha com os riscos aceitos — incluindo que o módulo de pagamento entra como obrigatório mesmo sem alteração, por ser fluxo crítico de negócio.

## Cenário com ambiguidade — API
**Cenário:** Na "AgroConecta" (marketplace B2B fictício), a release inclui o bump de uma biblioteca de serialização usada em todos os endpoints, e o projeto nunca montou matriz de risco.
**Input:** "Seleciona a regressão dessa release, tem um upgrade de dependência no meio."
**Prompt de exemplo:**
```
/swl-skill-qa-select-regression-suite Seleciona a regressão dessa release, tem um upgrade de dependência no meio.
```
**Saída esperada:** A skill avisa que não há matriz de `swl-skill-qa-risk-priority` nem histórico de CI acessível, e trata a seleção como preliminar, baseada só no diff. Como o bump é de biblioteca compartilhada por todos os endpoints, não classifica nenhuma área da API como dispensável — explica que o critério "nenhum arquivo dessa área mudou" não vale quando a mudança é numa dependência transversal.

## Cenário de risco real — Integração
**Cenário:** Na "ContaCerta" (contabilidade SaaS fictícia), a release sai em 2 horas. O gerente pede pra deixar a integração bancária de fora da regressão porque "não foi mexida nessa release e os testes dela são os mais lentos".
**Input:** "Monta a regressão sem a integração bancária, ninguém mexeu nela e são os testes mais demorados."
**Prompt de exemplo:**
```
/swl-skill-qa-select-regression-suite Monta a regressão sem a integração bancária, ninguém mexeu nela e são os testes mais demorados.
```
**Saída esperada:** A skill verifica o diff e mostra que a release inclui uma migration na tabela de lançamentos, que a integração bancária lê e grava — então ela está indiretamente impactada e permanece nos obrigatórios, com a evidência do impacto. Se o time ainda assim decidir cortar, a seção de riscos aceitos registra o que fica descoberto, em termos de negócio, e de quem foi a decisão.
