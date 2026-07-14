# Eficiência de tokens — auditoria e cortes aplicados

Objetivo: reduzir custo de token por chamada de cada skill, sem mudar comportamento nem
diluir nenhuma condição de guardrail. Metodologia: releitura frase por frase das 25
skills, buscando (a) a mesma instrução dita de duas formas na mesma skill, (b)
verbosidade sem ganho de precisão, (c) boilerplate já coberto em AGENTS.md/README.

**Achado sobre a categoria (c)**: não encontrei nenhum caso real. `AGENTS.md` e o
`README.md` do pacote são documentação de governança/instalação para quem mantém o
repositório — não são lidos em tempo de execução quando uma skill é invocada (só o
`SKILL.md` correspondente carrega). Nenhuma skill repete conteúdo desses arquivos; todo
corte aplicado foi por redundância **dentro do próprio arquivo** (categoria a) ou
verbosidade (categoria b).

**Regra seguida à risca**: nenhum corte foi aplicado a uma frase dentro de `## Guardrail`.
Todo corte de categoria (a) que envolvia sobreposição com o Guardrail foi resolvido
removendo a repetição do lado de fora do Guardrail (nos Passos), nunca do Guardrail em si.

---

## Passo 1 — Baseline (antes, ordem decrescente)

| Skill | Palavras (antes) |
|---|---|
| swl-skill-qa-check-security | 389 |
| swl-skill-qa-check-environment | 355 |
| swl-skill-qa-new-mobile-automation | 317 |
| swl-skill-qa-check-accessibility | 300 |
| swl-skill-qa-new-performance-test | 294 |
| swl-skill-qa-new-automation | 290 |
| swl-skill-qa-new-contract-tests | 279 |
| swl-skill-qa-plan-strategy | 274 |
| swl-skill-qa-safe-test-commit | 247 |
| swl-skill-qa-check-performance-results | 241 |
| swl-skill-qa-new-test-cases | 217 |
| swl-skill-qa-generate-rules | 213 |
| swl-skill-qa-risk-priority | 212 |
| swl-skill-qa-diagnose-failure | 203 |
| swl-skill-qa-check-coverage | 196 |
| swl-skill-qa-new-test-data | 194 |
| swl-skill-qa-generate-test-report | 194 |
| swl-skill-qa-new-bdd-scenarios | 191 |
| swl-skill-qa-check-data-quality | 185 |
| swl-skill-qa-exploratory-session | 181 |
| swl-skill-qa-report-bug | 180 |
| swl-skill-qa-check-flakiness | 180 |
| swl-skill-qa-review-tests | 178 |
| swl-skill-qa-describe-test-pr | 175 |
| swl-skill-qa-update-test-docs | 150 |
| **Total (25 skills)** | **5835** |

---

## Passos 2-4 — Skills editadas (categoria "sem mudança de significado")

### swl-skill-qa-check-security — 389 → 359 palavras (-30, -7,7%) — v1.0.0 → v1.0.1
- **Passo 1**: cortado "(Node, Python, Java, mobile, etc.)" e "que já cobre esse caso em profundidade" — ambos já ditos na `description` do frontmatter, carregada junto no mesmo contexto.
- **Passo 3**: cortado "com a evidência real observada (request/response, não suposição)" — mesma exigência já coberta, com mais precisão, no `## Guardrail` ("Todo achado reportado precisa ter uma evidência real de execução...").

### swl-skill-qa-check-environment — 355 → 344 palavras (-11, -3,1%) — v1.0.0 → v1.0.1
- **Passo 1**: cortado "— nunca assuma um critério de 'ambiente pronto' genérico sem confirmação" — mesma regra já coberta pela primeira frase do `## Guardrail` ("Nunca assuma que um ambiente está pronto sem checar de fato").

### swl-skill-qa-new-mobile-automation — 317 → 298 palavras (-19, -6,0%) — v1.0.0 → v1.0.1
- **Passo 4**: cortado "Nunca declare cobertura de uma matriz mais ampla (ex: 'testado em iOS e Android') do que a efetivamente exercitada" — coberto pelo `## Guardrail` ("Nunca afirme que um cenário foi validado em um dispositivo ou versão de OS sem execução real registrada").

### swl-skill-qa-check-accessibility — 300 → 288 palavras (-12, -4,0%) — v1.0.0 → v1.0.1
- **Passo 3**: cortado "— a auditoria só vale para o que foi de fato executado" — mesma ideia já coberta em profundidade pelo `## Guardrail`.

### swl-skill-qa-new-performance-test — 294 → 278 palavras (-16, -5,4%) — v1.0.0 → v1.0.1
- **Passo 2**: cortado "— nunca assuma 'load' por padrão sem essa definição" — coberto pelo `## Guardrail` ("Nunca defina o tipo de teste... por conta própria").
- **Passo 3**: cortado "Nunca invente um SLA/threshold não informado —" (mantendo a instrução operacional de marcar "a confirmar com o responsável pelo SLA", que não está no Guardrail e por isso não podia ser cortada).

### swl-skill-qa-new-contract-tests — 279 → 264 palavras (-15, -5,4%) — v1.0.0 → v1.0.1
- **Passo 1**: cortado "— nunca infira campos, tipos ou obrigatoriedade a partir de uma única resposta de exemplo" — coberto pelo `## Guardrail` ("pergunte antes de inventar campos, tipos ou estrutura").

### swl-skill-qa-new-test-cases — 217 → 206 palavras (-11, -5,1%) — v1.0.0 → v1.0.1
- **Passo 1**: cortado "— nunca preencha lacunas de regra de negócio por conta própria" — coberto pelo `## Guardrail`, que além disso especifica o marcador exato (`[REGRA A CONFIRMAR COM PO]`) que os Passos não tinham.

**Teste aplicado a cada corte acima** (Passo 3 do prompt): reli só a versão nova de cada
trecho, sem a antiga, e cheguei à mesma decisão operacional e à mesma condição de
guardrail em todos os 7 casos — por isso foram aplicados como "sem mudança de
significado".

---

## Skills sem corte aplicado (18)

Revisei frase por frase e não encontrei redundância interna segura de cortar em:
`swl-skill-qa-new-automation`, `swl-skill-qa-plan-strategy`, `swl-skill-qa-safe-test-commit`,
`swl-skill-qa-check-performance-results`, `swl-skill-qa-generate-rules`,
`swl-skill-qa-risk-priority`, `swl-skill-qa-diagnose-failure`, `swl-skill-qa-check-coverage`,
`swl-skill-qa-new-test-data`, `swl-skill-qa-generate-test-report`,
`swl-skill-qa-new-bdd-scenarios`, `swl-skill-qa-check-data-quality`,
`swl-skill-qa-exploratory-session`, `swl-skill-qa-report-bug`, `swl-skill-qa-check-flakiness`,
`swl-skill-qa-review-tests`, `swl-skill-qa-describe-test-pr`, `swl-skill-qa-update-test-docs`.

Não forcei corte artificial nessas 18 — a maioria já era enxuta desde a criação, e o texto
que parecia "cortável" à primeira vista, ao aplicar o teste do Passo 3, não passava com
100% de certeza.

---

## Pendências — "mudança de significado", não aplicadas (decisão manual)

Nestes 4 pontos, considerei um corte mas não tive certeza absoluta de que o significado
se mantém idêntico — não apliquei nada, arquivos intocados nesses trechos:

1. **`swl-skill-qa-check-accessibility` — `## Guardrail`**: a frase repete a mesma ideia
   três vezes ("nunca declare conformidade sem execução real" → analogia com
   `qa-new-mobile-automation` → exemplo concreto "conforme WCAG AA só pode significar...").
   Poderia ser mais curta, mas não tenho certeza de que cortar a analogia ou o exemplo não
   perde nuance que um executor menos experiente precisaria. **Não tocado.**

2. **`swl-skill-qa-check-environment` — `## Guardrail`**: a analogia longa
   ("mesma classe de erro que os guardrails de 'nunca inferir' já usados nas demais
   skills...") pode ser proposital, para reforçar o padrão do pacote — ou pode ser cortável
   sem perda. Não tenho certeza suficiente. **Não tocado.**

3. **`swl-skill-qa-new-automation` — `## Guardrail`**: a frase final ("Testes sem esse
   comentário não devem ser aceitos em PR — não adicione o comentário antes da revisão
   real acontecer") reafirma o mesmo ponto da frase anterior de um ângulo diferente
   (quando marcar vs. o que rejeitar em PR). Pode ser puramente redacional ou pode ter
   as duas metades com peso operacional distinto. **Não tocado.**

4. **`swl-skill-qa-check-performance-results` e `swl-skill-qa-generate-test-report`**: a
   frase do Passo 1 ("nunca gere o relatório a partir de estimativa ou memória de
   execuções anteriores") e a do Guardrail ("não preencha as métricas/números faltantes
   com estimativa") podem ser a mesma regra aplicada a dois cenários (arquivo ausente vs.
   arquivo incompleto) ou duas regras distintas. Não tenho certeza suficiente para tratar
   como redundância pura. **Não tocado**, nas duas skills.

Nenhuma dessas 4 pendências envolve edição real — são só observações registradas para
você decidir manualmente, se quiser.

## Decisão sobre as 4 pendências (revisado manualmente)

Nenhuma das 4 foi cortada. Em todos os casos, a aparente redundância escondia uma
distinção operacional real:
- check-accessibility: o exemplo concreto e a analogia tornam a regra aplicável na
  prática, não são enfeite
- check-environment: a analogia é proposital, reforça o padrão do pacote
- new-automation: as duas frases do Guardrail instruem dois momentos diferentes do
  fluxo (quem escreve o teste vs. quem aprova o PR)
- check-performance-results / generate-test-report: cobrem duas falhas diferentes
  (arquivo ausente vs. arquivo incompleto), não a mesma regra repetida

Nenhum arquivo de skill foi alterado por esta decisão.

---

## Confirmação sobre `metadata.validated`

Nenhuma das 7 skills editadas teve frase do `## Guardrail` reescrita — todos os cortes
ficaram fora do Guardrail (confirmado via `git diff` filtrando pela linha `## Guardrail`
antes deste relatório). Por isso, **nenhuma skill precisa ser marcada como candidata a
reconfirmação de validação** — o campo `validated` de todas permanece exatamente como
estava antes desta rodada.

---

## Passo 5 — Versionamento aplicado

| Skill | Versão antes | Versão depois |
|---|---|---|
| swl-skill-qa-check-security | 1.0.0 | 1.0.1 |
| swl-skill-qa-check-environment | 1.0.0 | 1.0.1 |
| swl-skill-qa-check-accessibility | 1.0.0 | 1.0.1 |
| swl-skill-qa-new-mobile-automation | 1.0.0 | 1.0.1 |
| swl-skill-qa-new-contract-tests | 1.0.0 | 1.0.1 |
| swl-skill-qa-new-performance-test | 1.0.0 | 1.0.1 |
| swl-skill-qa-new-test-cases | 1.0.0 | 1.0.1 |

As outras 18 skills não foram editadas, então a versão não muda.

---

## Total agregado

| | Palavras |
|---|---|
| Antes (25 skills) | 5835 |
| Depois (25 skills) | 5721 |
| **Redução total** | **114 palavras (≈2,0%)** |

O ganho é modesto porque as skills já eram redigidas de forma enxuta desde a criação
(confirmado na auditoria anterior, `AUDITORIA-COBERTURA.md`, Parte 2) — a maior parte do
conteúdo de cada arquivo é instrução operacional específica de domínio, não passível de
corte sem perda real. Prefiro reportar 2% real a inflar a % cortando algo sem certeza.
