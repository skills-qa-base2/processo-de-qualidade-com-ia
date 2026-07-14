# Auditoria geral do projeto — Processo de Qualidade com IA

Auditoria evidence-based cobrindo scripts de build, conteúdo das 25 skills, documentação de governança e site gerado. Nenhuma correção foi aplicada nesta etapa — este é um relatório para revisão, não uma implementação. Todo achado abaixo tem localização exata (arquivo + linha) ou comportamento observado (comando executado / build rodado). Onde não foi possível confirmar com certeza, o achado está rotulado como "hipótese, sem confirmação".

Metodologia: leitura integral dos 5 scripts de build, dos 25 `SKILL.md` e 25 `EXAMPLES.md`, dos 6 documentos de governança, e inspeção direta do site gerado (os 5 scripts foram executados e o HTML resultante foi analisado, não apenas o código-fonte).

---

## Parte 1 — Scripts de build

### 1.1 Bug real confirmado — navegação "anterior/próxima" idêntica e errada em todas as 25 páginas

**Localização:** `scripts/build_skill_pages.py`, função `build_skill_page(s, idx)`:
- Linha 197: `def build_skill_page(s, idx):` — `idx` recebe a posição real da skill na lista `SKILLS` (passado como `i` no loop da linha 291: `for i, s in enumerate(SKILLS): build_skill_page(s, i)`).
- Linha 216: `for idx, ex in enumerate(s["examples"], start=1):` — este loop **reatribui a variável `idx`**, sobrescrevendo o parâmetro da função. Como todas as 25 skills têm exatamente 3 exemplos, ao final deste loop `idx` vale sempre `3`, independentemente da posição real da página.
- Linha 285: `prev_next=prev_next_block(base, idx)` — usa o `idx` já corrompido (sempre `3`) em vez da posição real da página.

**Confirmado por execução real**: rodei os 5 scripts e depois busquei `class="page-nav"` nas 25 páginas geradas em `skills\*.html`. Resultado: **as 25 páginas, sem exceção, mostram o mesmo bloco de navegação** — "anterior" sempre aponta para `swl-skill-qa-new-automation.html` e "próxima" sempre para `swl-skill-qa-new-test-cases.html` (posições 2 e 4 na lista ordenada `SKILLS`, consistente com `prev_next_block(base, 3)`). Isso inclui o caso patológico de a própria página `swl-skill-qa-new-automation.html` linkar "anterior" para si mesma, e `swl-skill-qa-new-test-cases.html` linkar "próxima" para si mesma.

**Severidade:** bug real, alto impacto de UX (navegação sequencial nunca funcionou desde que os exemplos foram adicionados), causa raiz simples (shadowing de variável), correção de baixo risco (renomear a variável do loop interno, ex. `ex_idx`).

### 1.2 Redundância real confirmada — build_skill_pages.py reconstrói as 25 páginas a cada import

**Localização:** `scripts/build_skill_pages.py`, linhas 291-294 (código de nível de módulo, fora de qualquer função/guard `if __name__ == "__main__"`):
```python
for i, s in enumerate(SKILLS):
    build_skill_page(s, i)

print(f"Built {len(SKILLS)} skill pages")
```
`build_home.py` e `build_instalacao.py` fazem `from build_skill_pages import (...)` (linha 3-5 e 3-4 respectivamente). Um `import` em Python executa todo o código de nível de módulo do arquivo importado.

**Confirmado por execução real**: ao rodar `python scripts/build_data.py && python scripts/build_skill_pages.py && python scripts/build_home.py && python scripts/build_instalacao.py && python scripts/build_downloads.py` em sequência, a mensagem `Built 25 skill pages` apareceu **3 vezes** no console (uma pela execução direta de `build_skill_pages.py`, e mais uma a cada import feito por `build_home.py` e `build_instalacao.py`). Isso significa 75 escritas de arquivo para 25 arquivos únicos — sem impacto de correção (saída final é idêntica e idempotente), mas com custo de I/O redundante e log confuso (parece que algo rodou 3x quando a intenção era rodar 1x por script).

**Severidade:** redundância real, confirmada por execução — não é um bug de corretude, mas é desperdício real e mensurável.

### 1.3 Duplicação real, porém marginal — `CATEGORY_ORDER` definida em dois arquivos

**Localização:** `scripts/build_data.py` linha 7 e `scripts/build_skill_pages.py` linha 11 — ambas definem, de forma independente (não importada), a lista idêntica:
```python
CATEGORY_ORDER = ["Planejamento", "Geração", "Verificação", "Diagnóstico", "Entrega"]
```
`build_home.py` e `build_instalacao.py` corretamente importam `CATEGORY_ORDER` de `build_skill_pages` (não redefinem) — a duplicação real está limitada a esses 2 arquivos.

Aplicando o mesmo critério de quantificação já usado na análise de consolidação das 4 skills de automação (quantificar antes de recomendar extração): isto é 1 linha duplicada em 2 arquivos — volume desprezível, não justificaria uma extração só por tamanho. O risco não é de volume, é de **dessincronia silenciosa**: se uma categoria for renomeada em um arquivo e não no outro, nada quebra em tempo de execução (a categoria só deixaria de bater com o `CATEGORY_MAP`), o que tornaria o bug difícil de perceber.

**Severidade:** duplicação real, volume marginal — não justifica extração pela regra de tamanho, mas o risco de dessincronia é uma razão independente e válida para `build_skill_pages.py` importar `CATEGORY_ORDER` de `build_data.py` em vez de redefinir.

### 1.4 Código morto confirmado — imports não usados em `build_home.py`

**Localização:** `scripts/build_home.py` linha 1: `import json, sys, os` e linha 3-5 (import de `render_md` junto com os demais nomes de `build_skill_pages`).

Confirmado por grep (`grep -n "json" build_home.py build_instalacao.py` e busca por `render_md(` em `build_home.py`):
- `json` é importado na linha 1 mas **nunca usado** em nenhum lugar do arquivo (apenas `sys` e `os` dessa mesma linha são usados).
- `render_md` é importado de `build_skill_pages` (linha 3-5) mas **nunca chamado** em `build_home.py` — o texto de `intro_text` e dos parágrafos do corpo é inserido como string literal já formatada em HTML, sem passar por `render_md()`.

**Severidade:** código morto confirmado, sem impacto funcional — sobra de uma versão anterior do arquivo.

### 1.5 Tratamento de erro — consistente, mas com uma assimetria documentável

- `parse_examples()` em `build_data.py` (linhas 66-69) verifica `os.path.exists()` antes de ler `EXAMPLES.md` e retorna `None` silenciosamente se não existir — mas isso é comunicado depois, de forma alto-falante, via `print(f"AVISO: ...")` em `main()` (linhas 134-136). Não é uma falha silenciosa real: há aviso no console.
- `parse_skill()` (linhas 95-98) **não** verifica se `SKILL.md` existe antes de abrir — se estivesse ausente, o script quebraria com `FileNotFoundError` não tratado. Isso é consistente com a filosofia geral do projeto (falhar alto, não mascarar), mas é uma assimetria de estilo entre duas funções irmãs no mesmo arquivo: uma faz checagem defensiva com aviso, a outra deixa estourar exceção nativa. Nenhuma das duas é "errada" — mas o padrão não é uniforme.
- `front["metadata"]["validated"]` (build_data.py linha 103) não tem valor padrão — quebra alto se ausente (isto é intencional, conforme pedido em rodada anterior desta mesma sessão). Já `version` (linha 102) usa `.get(..., "1.0.0")` — um fallback silencioso. Ou seja, dentro do mesmo bloco de frontmatter, um campo falha alto e o campo vizinho falha silenciosamente com valor default. **Hipótese, sem confirmação de que isso seja indesejado** — pode ser intencional (nem toda skill precisa ter versão explícita), mas vale registrar a assimetria para decisão consciente.
- Nenhum dos 5 scripts tem tratamento de erro para os arquivos de asset (`assets/style.css`, `assets/app.js`, `assets/banner_base2.png`, `scripts/skills_data.json`) — todos falham alto (`FileNotFoundError` nativo) se ausentes. Consistente entre os 5 scripts.

**Severidade:** inconsistência de estilo interna (não um bug), documentada para decisão consciente do time.

### 1.6 URL placeholder desatualizada

**Localização:** `scripts/build_instalacao.py` linha 8:
```python
GITHUB_REPO_URL = "https://github.com/SEU-USUARIO/processo-qualidade-ia"
```
Comentário na linha 7 já sinaliza isso como pendência: `# TODO: depois de criar o repositório no GitHub, troque esta URL pela real.`

Confirmado via `git remote -v`: o remote real é `https://github.com/skills-qa-base2/processo-de-qualidade-com-ia.git` — diferente da URL hardcoded. Isso significa que o botão "↗ Ver no GitHub" na página de instalação (`instalacao.html`, gerado a partir de `download_html` nas linhas 15-31 de `build_instalacao.py`) atualmente aponta para uma URL de exemplo genérica, não para o repositório real.

**Severidade:** bug real confirmado (o link do site aponta para o lugar errado), já sinalizado no próprio código como TODO — não é uma descoberta nova de causa, mas confirma que a pendência já documentada continua não resolvida.

---

## Parte 2 — Conteúdo das skills e exemplos

Leitura integral dos 25 `SKILL.md` + 25 `EXAMPLES.md` (50 arquivos) e do `MANIFEST.md`.

### 2.1 Inconsistência de documentação confirmada — 7 versões desatualizadas no `MANIFEST.md`

O `SKILL.md` de 7 skills foi corrigido para `1.0.1` durante a rodada de eficiência de tokens (registrada em `EFICIENCIA-TOKENS.md`), mas `MANIFEST.md` nunca foi atualizado — tanto a tabela quanto o "Histórico de versões" ainda mostram `1.0.0`, sem nenhuma entrada de patch:

| Skill | `SKILL.md` (frontmatter) | `MANIFEST.md` tabela | `MANIFEST.md` histórico |
|---|---|---|---|
| `swl-skill-qa-new-test-cases` | `1.0.1` | linha 12: `1.0.0` | linhas 68-69: só `1.0.0` |
| `swl-skill-qa-new-mobile-automation` | `1.0.1` | linha 15: `1.0.0` | linhas 78-79: só `1.0.0` |
| `swl-skill-qa-new-contract-tests` | `1.0.1` | linha 16: `1.0.0` | linhas 81-82: só `1.0.0` |
| `swl-skill-qa-new-performance-test` | `1.0.1` | linha 17: `1.0.0` | linhas 84-85: só `1.0.0` |
| `swl-skill-qa-check-security` | `1.0.1` | linha 24: `1.0.0` | linhas 105-106: só `1.0.0` |
| `swl-skill-qa-check-accessibility` | `1.0.1` | linha 25: `1.0.0` | linhas 108-109: só `1.0.0` |
| `swl-skill-qa-check-environment` | `1.0.1` | linha 26: `1.0.0` | linhas 111-112: só `1.0.0` |

`swl-skill-qa-new-automation` é o único caso que bate: `SKILL.md` diz `1.1.0`, `MANIFEST.md` linha 14 também diz `1.1.0`, e o histórico (linhas 74-76) lista corretamente as entradas `1.1.0`/`1.0.0`.

`metadata.validated`: sem mismatch — as 3 skills com `validated: false` (`check-accessibility`, `check-environment`, `check-security`) batem exatamente com a nota do `MANIFEST.md` linha 53. Contagem geral (18 originais + 4 adicionadas depois + 3 pendentes = 25) confere.

**Severidade:** inconsistência de documentação, confirmada — drift real de versionamento, sem impacto funcional no site (a versão exibida na página de cada skill vem do `SKILL.md` real, via `skills_data.json`, não do `MANIFEST.md`).

### 2.2 Confirmação das correções anteriores — todas passaram

Re-verificado, não assumido:

- **Resíduo de "júnior/pleno/sênior"**: `grep -rniE "júnior|junior|pleno|sênior|senior|\bjr\b|\bpl\b|\bsr\b"` nos 50 arquivos → **zero ocorrências**. PASSOU.
- **Distribuição de tipo de projeto**: todas as 22 skills fora da lista de exceções usam 3 tipos de projeto distintos nos 3 exemplos. As 3 exceções documentadas se confirmam exatamente: `new-mobile-automation` (Mobile×3, com nota de exceção documentada na própria linha 28 do arquivo), `new-contract-tests` (API×3, variando técnica — schema OpenAPI / Pact / recusa por falta de spec), `check-accessibility` (Web/Mobile/Mobile). Nenhuma outra skill repete tipo de projeto. PASSOU.
- **Campo "Prompt de exemplo"**: contagem exata — 73 blocos `**Prompt de exemplo:**` + 2 notas `**Prompt de exemplo (nota):**` = 75, batendo com as 75 (`## Cenário`) esperadas. Os 2 casos de nota (`new-contract-tests` e `new-test-data`, ambos no cenário "risco real") são os já conhecidos e continuam justificados no próprio texto (dado real colado pelo usuário, não reproduzido em prompt copiável). PASSOU.

### 2.3 Hipóteses sem confirmação (achados de baixa confiança, não bugs)

- **`swl-skill-qa-check-coverage/SKILL.md` linha 28** — o guardrail distingue explicitamente "cobertura de cenário" de "execução com sucesso" ("cobertura completa de cenários não significa que os testes foram executados com sucesso"). Nenhum dos 3 exemplos em `EXAMPLES.md` ilustra especificamente essa distinção (os 3 giram em torno de "não inflar números de cobertura"). Pode ser que a cláusula seja apenas complementar e não precise de exemplo dedicado — não é possível confirmar se isso é uma lacuna real sem um julgamento de produto.
- **`swl-skill-qa-new-automation/SKILL.md` linha 15** ("se o cenário for mobile, use `swl-skill-qa-new-mobile-automation` em vez desta skill") **vs.** `EXAMPLES.md` linhas 1-8 ("Cenário direto — Mobile", app "híbrido" testado via Playwright, sem menção ao redirecionamento indicado no próprio passo 1 da skill). É defensável (app híbrido pode ser tecnicamente WebView/web), mas, diferente de `new-mobile-automation` e `check-accessibility`, que documentam explicitamente por que fogem do padrão de 3 tipos distintos, `new-automation` não tem nenhuma nota explicando por que seu exemplo rotulado "Mobile" não segue a própria regra de roteamento que a skill define. Consistência de redação, não um bug de comportamento.

Nenhuma referência cruzada quebrada entre skills foi encontrada (todas as 25 skills se referenciam sempre pelo nome completo `swl-skill-qa-*`, e o build não gera hyperlinks a partir desse texto — é renderizado como texto/`<code>` estático, então mesmo um nome incorreto não geraria link quebrado, apenas citação textual errada; nenhum caso desse tipo foi encontrado).

---

## Parte 3 — Documentação de governança

Comparação de `README.md` (raiz), `qa-skills-package/README.md`, `MANIFEST.md`, `AGENTS.md`, `AUDITORIA-COBERTURA.md` e `EFICIENCIA-TOKENS.md` contra o estado real do repositório (25 pastas, `CATEGORY_MAP` de `build_data.py`, contagem real de exemplos, versões reais de frontmatter, `git log`, `git remote -v`).

### 3.1 Contagens de categoria e total de skills — sem mismatch

`README.md` (raiz, linhas 33-66), `qa-skills-package/README.md` (linhas 88-116) e `MANIFEST.md` (linhas 9-33) concordam entre si e com o `CATEGORY_MAP` real (Planejamento=2, Geração=7, Verificação=9, Diagnóstico=3, Entrega=4, total 25). Nenhuma correção necessária aqui.

### 3.2 Inconsistência de documentação confirmada — `AUDITORIA-COBERTURA.md` com contagem de palavras desatualizada

**Localização:** `AUDITORIA-COBERTURA.md`, Parte 2, linhas 43-47 — tabela de contagem de palavras das 4 skills de automação, escrita **antes** da rodada de eficiência de tokens:

| Skill | Doc diz | Real hoje (recontado) |
|---|---|---|
| `qa-new-automation` | 288 | ~290 (não editada nesta skill — diferença é ruído de contagem) |
| `qa-new-mobile-automation` | 315 | ~298 (caiu — `EFICIENCIA-TOKENS.md` linha 63 registra "317 → 298") |
| `qa-new-contract-tests` | 277 | ~264 (caiu — `EFICIENCIA-TOKENS.md` linha 73 registra "279 → 264") |
| `qa-new-performance-test` | 292 | ~278 (caiu — `EFICIENCIA-TOKENS.md` linha 69 registra "294 → 278") |
| **Total** | **1172** | **~1130** |

Causa confirmada via `git log`: `AUDITORIA-COBERTURA.md` foi escrito no commit `c80b9ec` (adição das 3 skills de verificação), e a rodada de eficiência de tokens (commit `c6d76ca`, que criou `EFICIENCIA-TOKENS.md`) veio depois e nunca retroalimentou este documento.

**Hipótese, sem confirmação:** a conclusão da linha 54 ("~2,9x a 3,3x mais caro por chamada" ao fundir as 4 skills em uma só) provavelmente continua válida ou fica ainda mais forte contra a fusão (palavras por chamada individual caíram, o que tende a aumentar o múltiplo relativo de uma skill fundida) — mas o cenário fundido não foi recalculado nesta auditoria, então isso é uma direção provável, não um fato confirmado.

### 3.3 Lacuna de documentação confirmada — nenhum doc de governança menciona `EXAMPLES.md`/"Prompt de exemplo"

`grep -rn "Prompt de exemplo|EXAMPLES.md"` nos 6 documentos → zero ocorrências. Coerente com a ordem cronológica real (`git log` confirma que esses 6 docs são todos anteriores aos commits que criaram `EXAMPLES.md` e o campo "Prompt de exemplo"), mas isso deixa lacunas práticas hoje:

- **`README.md` (raiz), seção "Adicionando uma skill nova" (linhas 146-150)**: instrui criar `SKILL.md` com frontmatter/`## Passos`/`## Guardrail` e registrar em `CATEGORY_MAP`/`TITLE_MAP` — **não menciona criar `EXAMPLES.md`**, apesar de ser uma convenção seguida por 25/25 skills hoje, e do próprio `build_data.py` (linhas 134-136) emitir aviso se faltar. Seguindo só o README ao pé da letra, uma skill nova sairia sem exemplos.
- **`AGENTS.md`, seção "Estrutura esperada" (linhas 13-16)**: mesma lacuna — não cita `EXAMPLES.md` como parte do formato esperado.

**Severidade:** inconsistência de documentação / lacuna de instrução, confirmada — não é uma contradição direta (não diz algo falso), é uma omissão que pode levar a uma skill nova inconsistente com o padrão real do projeto.

### 3.4 URL do repositório — sem mismatch nos documentos de governança

Busquei "SEU-USUARIO" e qualquer placeholder de URL nos 6 documentos: zero ocorrências. `README.md` (raiz) linha 6 já cita a URL real e correta. **A única URL placeholder desatualizada é a de `scripts/build_instalacao.py` linha 8 (já reportada em 1.6) — os documentos de governança em si estão corretos neste ponto.**

### Ranking de desatualização (mais → menos)

1. **`MANIFEST.md`** — 7 versões erradas (tabela + histórico) + lacuna de `EXAMPLES.md`.
2. **`AUDITORIA-COBERTURA.md`** — contagem de palavras stale nas 4 skills de automação + mesma lacuna.
3. **`README.md` (raiz)`, `qa-skills-package/README.md`, `AGENTS.md`** — contagens corretas, mas com a lacuna de instrução sobre `EXAMPLES.md`/"Prompt de exemplo".
4. **`EFICIENCIA-TOKENS.md`** — é a própria fonte da verdade para os bumps de versão e cortes de palavras; nenhum número incorreto encontrado.

---

## Parte 4 — Site gerado

Site gerado a partir de uma execução real dos 5 scripts (não apenas análise de código-fonte).

### 4.1 Links internos — sem links quebrados

Todos os `href` relativos extraídos de `index.html`, `instalacao.html` e das 25 páginas `skills\*.html` resolvem para arquivos que existem em disco. `instalacao.html → downloads/qa-skills-package.zip` também resolve (arquivo de 72 KB confirmado após build).

**Observação de higiene (não bloqueante):** `assets/style.css`, `assets/app.js` e `assets/banner_base2.png` existem no repositório mas **não são referenciados por nenhum `href`/`src` em nenhuma das 27 páginas geradas** — o CSS/JS/imagem são embutidos inline (`<style>`/`<script>`/base64) diretamente no HTML pelos scripts de build. A pasta `assets/` é a fonte usada pelo build, não um artefato consumido pelo site publicado — não é um bug, mas vale registrar para não confundir alguém procurando por que a pasta parece "não usada" ao inspecionar o HTML final.

### 4.2 Sidebar / busca / accordion — checagem nas 25 páginas, não amostra

| Checagem | Resultado |
|---|---|
| `<aside class="sidebar">` presente | 25/25 |
| `window.SKILLS_SEARCH_INDEX` embutido | 25/25 |
| Exatamente 3 `<details class="examples-accordion examples-accordion--N">` (N=1,2,3) | 25/25 |

Nenhuma página fora do padrão.

### 4.3 Bug real confirmado — 7 regras de CSS com `--green` como texto reprovam WCAG AA

Todas as combinações de cor já revisadas em rodadas anteriores (`.callout code`, badges azul/roxo/coral, `.guardrail-box`/`.g-label`, `.examples-accordion--1/2/3`, `.example-note`) **não** foram reavaliadas aqui (permanecem válidas). O que não tinha sido revisado ainda: `--green` (`#00964f`) usado diretamente como cor de texto, ou como fundo com texto branco, em 7 seletores — nenhum deles tem uma variante de texto mais escura calculada (diferente do sistema `--blue-text`/`--purple-text`/`--coral-text` já existente).

Recalculei manualmente a razão de contraste (fórmula WCAG de luminância relativa) para cada par — confirmei por conta própria (não apenas aceitei o número reportado) os dois casos mais citados: `#00964f` sobre `#f6faf8` = **3,64:1**, e branco sobre `#00964f` = **3,84:1** — ambos abaixo do mínimo de 4,5:1 para texto normal, e nenhum dos 7 seletores usa tamanho/peso que qualificasse para o limiar de "texto grande" (3:1) — todos estão entre 11px e 14px:

| Seletor | Linha (style.css) | Par de cor | Contraste | Tema afetado |
|---|---|---|---|---|
| `.eyebrow` | 229 | `#00964f` texto / `#f6faf8` fundo | 3,64:1 | claro (escuro usa `--lime`, ok) |
| `.theme-toggle:hover` | 112 | `#00964f` texto/borda / `#fff` ou `#101f1a` | 3,84:1 / 4,44:1 | ambos |
| `.nav-group li a:hover` | 199 | `#00964f` texto / `--bg` | 3,64:1 | claro (escuro passa, 4,84:1) |
| `.download-option-label` | 463 | `#00964f` texto / `#fff` | 3,84:1 | claro (escuro usa `--lime`, ok) |
| `.skill-card .sc-go` | 523 | `#00964f` texto / `#fff` ou `#101f1a` | 3,84:1 / 4,44:1 | ambos (sem override dark) |
| `.eyebrow .cat-pill` (dark) | 243 | branco / `#00964f` fundo | 3,84:1 | escuro (claro usa `--dark-green`, 9,86:1, ok) |
| `.download-btn:hover` | 478 | branco / `#00964f` fundo | 3,84:1 | ambos |

Como o CSS é embutido de forma idêntica nas 27 páginas, cada uma dessas 7 regras se repete 27 vezes no site publicado.

**Regras novas checadas e aprovadas** (calculadas, não só observadas): `.content code`, `.usage-block .usage-cmd`, `.content th`, `.nav-group li a.active`, `.callout .callout-label`/`.callout strong`, `.eyebrow .cat-pill` no tema claro — todas entre 5,98:1 e 10,14:1, com margem confortável.

**Severidade:** bug real, confirmado por cálculo — dado que este é um pacote de skills de QA que inclui uma skill dedicada de auditoria de acessibilidade (`swl-skill-qa-check-accessibility`), a falha de AA no próprio site é uma inconsistência notável entre o que o produto prega e o que pratica.

---

## Parte 5 — Adições genuinamente efetivas

Aplicando o filtro pedido ("já está coberto? há evidência real de necessidade?") às Partes 1-4: **nenhuma delas revelou uma lacuna de cobertura no catálogo de skills** (isso já foi objeto de uma auditoria de ciclo de vida anterior, que resultou nas 3 skills de verificação já adicionadas). Os achados desta auditoria são inteiramente de dívida de implementação/documentação — um bug de navegação, contraste de cor, drift de versão entre documentos, uma redundância de build e uma lacuna de instrução — não de funcionalidade ausente.

Não estou propondo nenhuma skill nova, nenhum campo novo de exemplo, nem nenhuma seção nova de documentação além das correções pontuais já listadas nas Partes 1-4 (ex.: adicionar `EXAMPLES.md` à lista de "Adicionando uma skill nova" do README é uma correção de lacuna existente, não uma adição especulativa).

**Hipótese, sem demanda confirmada:** os dois pontos da seção 2.3 (exemplo de cobertura vs. execução em `check-coverage`, e a falta de nota de exceção no exemplo Mobile de `new-automation`) são polimentos de consistência de redação que só valem a pena se o time achar que a falta de exemplo/nota realmente confunde um leitor — não há evidência de que isso tenha causado confusão real até agora.

---

## Lista priorizada de resolução

1. **Corrigir o shadowing de `idx` em `build_skill_pages.py` (linha 216)** — bug real de maior impacto ao usuário (navegação sequencial nunca funcionou), causa raiz simples, correção de baixíssimo risco (renomear variável do loop).
2. **Corrigir as 7 regras de contraste de `--green` como texto (Parte 4.3)** — bug real de acessibilidade, mesmo padrão de correção já aplicado ao sistema de badges (variante de texto mais escura + revisão por tema escuro); prioridade alta dado que o produto inclui uma skill de auditoria de acessibilidade.
3. **Corrigir `GITHUB_REPO_URL` em `build_instalacao.py` linha 8** — bug real e já autoassinalado como TODO; o link "Ver no GitHub" do site aponta para lugar errado.
4. **Sincronizar as 7 versões desatualizadas no `MANIFEST.md`** (Parte 2.1) — mecânico, baixo risco, resolve drift de documentação já confirmado.
5. **Atualizar a tabela de contagem de palavras em `AUDITORIA-COBERTURA.md`** (Parte 3.2) — mecânico, mas vale recalcular também o cenário "fundido" antes de reescrever a conclusão, já que a direção do múltiplo pode ter mudado.
6. **Adicionar menção a `EXAMPLES.md`/"Prompt de exemplo" no README (raiz) e no `AGENTS.md`** (Parte 3.3) — fecha uma lacuna real de instrução para quem for criar uma skill nova.
7. **Corrigir a redundância de build (execução tripla de `build_skill_pages.py` via import)** — não afeta corretude, mas resolve desperdício de I/O e log confuso; pode ser feito isolando o loop de geração de página dentro de um `if __name__ == "__main__":` ou de uma função explícita.
8. **Deduplicar `CATEGORY_ORDER`** (importar de `build_data.py` em `build_skill_pages.py`) — baixo custo, elimina risco de dessincronia futura.
9. **Remover imports mortos em `build_home.py`** (`json`, `render_md`) — limpeza trivial.
10. **(Opcional, baixa prioridade) Polimento de redação** — considerar um exemplo/nota para a distinção cobertura×execução em `check-coverage`, e uma nota de exceção no exemplo Mobile de `new-automation` — só se o time concordar que vale o esforço; não há evidência de confusão real reportada.

Nenhum item desta lista foi implementado nesta etapa — aguardando decisão sobre o que vira prompt de implementação.
