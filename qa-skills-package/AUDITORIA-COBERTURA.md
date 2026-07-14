# Auditoria de cobertura — Skills de QA Base2

Auditoria realizada lendo o conteúdo real de todas as skills do pacote (22 na primeira rodada, depois 25 com as adições da Parte 3) — nenhuma conclusão baseada em suposição sobre o que uma skill "provavelmente" faz.

---

## Parte 1 — Mapa de cobertura do ciclo de vida de QA

| Etapa do ciclo | Skills que cobrem | Situação |
|---|---|---|
| **Planejamento** | `qa-plan-strategy`, `qa-generate-rules` | Coberto |
| **Design de caso** | `qa-new-bdd-scenarios`, `qa-new-test-cases` | Coberto |
| **Geração de dados** | `qa-new-test-data` | Coberto |
| **Ambiente** | nenhuma skill dedicada (antes da Parte 3) | Parcial — `qa-plan-strategy` (pergunta 5) e `qa-generate-rules` (`convencoes-teste.md`) perguntam/documentam, mas nenhuma skill validava, provisionava ou fazia seed de ambiente |
| **Execução manual** | `qa-exploratory-session`, `qa-report-bug` | Coberto |
| **Automação** | `qa-new-automation` (web/API/integração), `qa-new-mobile-automation`, `qa-new-contract-tests`, `qa-new-performance-test` | Coberto |
| **Não-funcional — Performance** | `qa-new-performance-test`, `qa-check-performance-results` | Coberto |
| **Não-funcional — Segurança** | nenhuma nesta coleção (antes da Parte 3) | Existe `swl-skill-check-security` no pacote irmão `org-skills`, mas escopado a .NET Web API (confirmado relendo o `MANIFEST.md`/frontmatter daquele pacote) — não serve outros stacks |
| **Não-funcional — Acessibilidade** | nenhuma (antes da Parte 3) | Zero menção em qualquer skill |
| **Não-funcional — Visual** | nenhuma | Zero menção — deixada de fora por enquanto (ver Parte 3) |
| **Diagnóstico** | `qa-diagnose-failure`, `qa-check-flakiness`, `qa-report-bug` | Coberto |
| **Entrega** | `qa-describe-test-pr`, `qa-update-test-docs`, `qa-safe-test-commit`, `qa-generate-test-report`, `qa-check-performance-results` | Coberto |
| **Manutenção da própria suíte** | `qa-review-tests` + `qa-check-coverage` (flag de teste órfão) + `qa-check-flakiness` | Coberto, distribuído em 3 skills — não é lacuna |

Filtro aplicado antes de propor qualquer skill nova: (a) já coberta por outra skill existente? (b) há evidência real no MANIFEST/histórico de que a necessidade já apareceu? Nenhuma das 4 lacunas abaixo teve confirmação de demanda real — todas tratadas como **hipótese**.

### Propostas priorizadas (máx. 5)
1. `qa-check-security` genérica — maior impacto, já que a única cobertura de segurança do ecossistema Base2 é travada a .NET.
2. `qa-check-accessibility` (WCAG) — pauta comum em contratos enterprise/setor público.
3. `qa-check-environment` — resolve a lacuna parcial de "Ambiente".
4. `qa-check-visual-regression` — impacto mais restrito, times com UI pesada.

Não houve 5ª proposta — "manutenção da suíte" já estava coberta, não force uma proposta artificial.

---

## Parte 2 — Consolidação: as 4 skills de automação deveriam virar 1?

### Números reais (contagem `wc`, arquivo completo incluindo frontmatter = exatamente o custo por chamada)

| Skill | Palavras/chamada | Frontmatter | % genuinamente exclusivo |
|---|---|---|---|
| `qa-new-automation` | 288 | 46 | ≈70% |
| `qa-new-mobile-automation` | 315 | 44 | ≈73% |
| `qa-new-contract-tests` | 277 | 40 | ≈96% |
| `qa-new-performance-test` | 292 | 46 | ≈95% |
| **Total hoje** | **1172** | — | — |

Duplicação real concentrada quase toda entre **automation ↔ mobile** (~85 palavras idênticas/quase-idênticas, confirmado via grep): seção `Origem do cenário`, seção `Registro no pipeline`, bullet de dados via `qa-new-test-data`, núcleo do guardrail `generated-by-ai`. `contract-tests` e `performance-test` não têm nenhuma dessas seções — são as mais distintas das 4.

### Custo por chamada, hoje vs. fundida
- Hoje: 277 a 315 palavras, dependendo de qual é chamada.
- Fundida (eliminando toda duplicação real + adicionando uma etapa nova de "identifique o domínio" que hoje é implícita no nome da skill): ≈900-950 palavras.
- **Resultado: ~2,9x a 3,3x mais caro por chamada, para sempre, em troca de uma redução de armazenamento total de ~20%.**

### Guardrail se perderia?
Sim — risco real de diluição (parágrafo genérico aplicado com menos precisão) e de perda por edição futura (alguém "simplifica" o parágrafo combinado e apaga sem querer a cláusula de outro domínio).

### Conclusão: NÃO FUNDIR — sustentado pelos números, não por preferência estética.

### Extrair o texto duplicado automation↔mobile para um arquivo compartilhado?
Testado com números: **não compensa em custo de token**. Um arquivo `_shared/` exigiria frase-ponteiro + leitura externa via ferramenta, custando igual ou pior que hoje (85 palavras do arquivo compartilhado + ~15 de ponteiro ≈ mesma ordem de grandeza dos 85 originais, mais uma ida a mais de tool call). Vale por manutenção (editar 1x em vez de 2x), não por token. **Decisão: não extrair agora** — 85 palavras é pequeno demais para justificar a complexidade. Rastreamento desse risco de manutenção registrado no `AGENTS.md` (ver Parte 3).

### Outros pares/trios com sobreposição ≥ automation↔mobile?
Par mais próximo: `qa-generate-test-report` ↔ `qa-check-performance-results` — 40 palavras idênticas/quase-idênticas (3 frases via grep), mas isso é 20,8% de 192 e 16,7% de 239 — **abaixo** do par automation↔mobile (27-29,5%). Nenhum outro par/trio atinge ou supera o critério. O resto da coleção compartilha *filosofia* (guardrail anti-invenção), não *texto literal* — isso é intencional (estilo do `AGENTS.md`), não duplicação a extrair.

---

## Parte 3 — Implementado

### Skills novas criadas
Três skills novas em `qa-skills-package/skills/`, na categoria **Verificação**, seguindo o formato exato das 22 existentes (frontmatter `name`/`description`/`argument-hint`/`metadata.version` iniciando em `1.0.0`, seção `## Passos`, seção `## Guardrail`):

- **`swl-skill-qa-check-security`** — verificação de segurança stack-agnóstica (QA funcional/dinâmica: autenticação, injeção, exposição de dados, headers, mobile), para qualquer stack fora de .NET Web API.
- **`swl-skill-qa-check-accessibility`** — auditoria WCAG via ferramenta já presente no projeto (axe-core/pa11y/Lighthouse); guardrail contra declarar conformidade além do efetivamente exercitado.
- **`swl-skill-qa-check-environment`** — valida ambiente pronto antes da execução (health check, seed de dados, feature flags); guardrail contra presumir "pronto" sem checar.

`qa-check-visual-regression` **ficou de fora por enquanto**, conforme escopo desta rodada — segue como hipótese registrada na Parte 1, não descartada.

### Confirmação do escopo real do org-skills/check-security
Reli o `MANIFEST.md` e o frontmatter do `swl-skill-check-security` do pacote `org-skills` antes de escrever a descrição da nova skill. Confirmado: a descrição do arquivo real diz explicitamente *"vulnerabilidades de segurança comuns em APIs .NET"* — o escopo .NET-específico presumido na Parte 1 bateu com a realidade, nenhum ajuste de description/guardrail foi necessário além do já planejado. A description de `swl-skill-qa-check-security` (nova) deixa explícito que complementa, não duplica, essa skill.

### Registro no build_data.py
As 3 skills novas foram adicionadas ao `CATEGORY_MAP` (todas `"Verificação"`) e ao `TITLE_MAP` (`"Verificar segurança (multi-stack)"`, `"Auditar acessibilidade"`, `"Validar ambiente de teste"`) no topo de `scripts/build_data.py`.

### Nota de rastreamento de duplicação no AGENTS.md
Adicionada a seção **"Duplicação intencional entre skills (não extrair)"** ao `qa-skills-package/AGENTS.md`, documentando os 4 trechos compartilhados entre `qa-new-automation` e `qa-new-mobile-automation`, a decisão de não extrair (custo de token igual ou pior) e o lembrete de replicar manualmente qualquer edição nesses trechos entre as duas skills. Não é referenciada por nenhum SKILL.md em runtime — é só um lembrete para quem editar o repositório.

### Pipeline de build
Rodados os 5 scripts, na ordem: `build_data.py` (25 skills parseadas) → `build_downloads.py` (zip de 34 KB) → `build_skill_pages.py` (25 páginas) → `build_home.py` → `build_instalacao.py`. Nenhum erro. As 3 páginas novas renderizam com categoria "Verificação" e título correto; as 22 páginas existentes foram regeradas só por causa do nav prev/next e do índice de busca embutido se ajustarem à lista de 25 skills — não houve mudança de conteúdo nelas.
