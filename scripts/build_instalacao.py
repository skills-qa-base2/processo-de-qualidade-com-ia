import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_skill_pages import SKILLS, page_shell, render_md, word_count_and_time, OUT_DIR

base = ""

GITHUB_REPO_URL = "https://github.com/skills-qa-base2/processo-de-qualidade-com-ia"

command_rows = "\n".join(
    f"<tr><td><code>/{s['name']}</code></td><td>{s['description']}</td></tr>"
    for s in SKILLS
)

download_html = f"""
<div class="download-card">
  <div class="download-option">
    <div class="download-option-label">BAIXAR O ZIP</div>
    <p>Contém só as pastas <code>skills/</code> prontas pra copiar para <code>.claude/skills/</code>,
    sem o resto do site.</p>
    <a class="download-btn" href="downloads/qa-skills-package.zip" download>⬇ qa-skills-package.zip</a>
  </div>
  <div class="download-option">
    <div class="download-option-label">CLONAR O REPOSITÓRIO</div>
    <p>Inclui histórico de versões, o código-fonte do site e o pacote de skills, tudo junto.</p>
    <a class="download-btn download-btn-outline" href="{GITHUB_REPO_URL}" target="_blank" rel="noopener">↗ Ver no GitHub</a>
  </div>
</div>
<p style="font-size:13.5px; color:var(--text-muted);">As duas opções vêm da mesma fonte
(<code>qa-skills-package/skills/</code>) — nunca ficam desatualizadas uma em relação à outra.</p>
"""

install_md = """
## Opção 1 — Projeto específico

Copie a pasta de cada skill que deseja usar para `.claude/skills/` dentro do repositório do projeto:

```
seu-projeto/
└── .claude/
    └── skills/
        ├── swl-skill-qa-plan-strategy/
        │   └── SKILL.md
        ├── swl-skill-qa-new-test-cases/
        │   └── SKILL.md
        └── ...
```

As skills ficam disponíveis apenas para quem trabalha naquele repositório.

## Opção 2 — Disponível globalmente (usuário)

Copie as pastas das skills para o diretório global do Claude Code.

**Windows (PowerShell):**

```powershell
Copy-Item -Recurse ".\\skills\\swl-skill-qa-plan-strategy" "$env:USERPROFILE\\.claude\\skills\\"
Copy-Item -Recurse ".\\skills\\swl-skill-qa-new-test-cases" "$env:USERPROFILE\\.claude\\skills\\"
# ... repita para cada skill desejada
```

**macOS / Linux:**

```bash
cp -r ./skills/swl-skill-qa-plan-strategy ~/.claude/skills/
cp -r ./skills/swl-skill-qa-new-test-cases ~/.claude/skills/
# ... repita para cada skill desejada
```

**Instalar todas de uma vez:**

Se preferir disponibilizar as 25 skills globalmente de uma só vez, em vez de copiar pasta por pasta:

**Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\\.claude\\skills" | Out-Null
Copy-Item -Recurse ".\\skills\\*" "$env:USERPROFILE\\.claude\\skills\\"
```

**macOS / Linux:**

```bash
mkdir -p ~/.claude/skills
cp -r ./skills/*/ ~/.claude/skills/
```

As skills ficam disponíveis em todos os projetos do usuário.

## Como usar

Com o Claude Code aberto em qualquer projeto, digite o comando da skill (ex: `/swl-skill-qa-plan-strategy`)
seguido do argumento indicado em cada skill.

## Como personalizar para um projeto

As skills leem o `CLAUDE.md` do projeto (e `.claude/rules/qa/`, quando gerado pela skill
`swl-skill-qa-generate-rules`) para adaptar o comportamento ao contexto específico.
Documente no `CLAUDE.md` do seu projeto:

- Framework de automação e padrão de organização (ex: Page Object Model)
- Ferramenta de gestão de casos de teste em uso
- Convenções de nomenclatura de cenários
- Política de dados de teste

Quanto mais completo o `CLAUDE.md`, mais preciso o resultado das skills.

## Fluxos comuns

Isto é um **guia de referência**, não uma skill nem uma automação nova — a ideia é
colar a versão em markdown (mais abaixo) no `CLAUDE.md` do seu projeto, para que o
Claude Code (ou você mesmo) saiba em que ordem faz sentido chamar as skills quando o
pedido é amplo ("testa esse fluxo do zero", "isso tá pronto pra lançar?"), em vez de
escolher uma skill de cada vez sem critério. Onde a ordem é uma dependência real
(uma skill lê o que a outra gerou), isso está indicado; onde é só uma sugestão de
bom senso, também.

### Fluxo 1 — Funcionalidade nova, testar do zero

**Dispara com:** "preciso testar o fluxo de checkout do zero", "essa feature ainda não tem nenhum teste".

1. `/swl-skill-qa-plan-strategy` — se o projeto ainda não tem uma estratégia de teste registrada. *Ordem sugerida:* evita partir direto pra 100% E2E por padrão.
2. `/swl-skill-qa-new-bdd-scenarios` (ou `/swl-skill-qa-new-test-cases`, conforme o projeto usa Gherkin ou casos estruturados) — a partir da user story/critérios de aceite.
3. `/swl-skill-qa-risk-priority` — prioriza os cenários gerados no passo 2. *Ordem sugerida:* a skill lista "cenários já mapeados via new-test-cases/new-bdd-scenarios" como fonte preferencial.
4. `/swl-skill-qa-new-test-data` — gera a massa fictícia para a entidade/domínio da feature.
5. `/swl-skill-qa-new-automation` (ou `/swl-skill-qa-new-mobile-automation` para mobile, `/swl-skill-qa-new-performance-test` para carga, `/swl-skill-qa-new-contract-tests` para contrato de API) — *dependência real:* o passo "Origem do cenário" dessas skills lê o cenário do passo 2, e consome a massa do passo 4.
6. `/swl-skill-qa-safe-test-commit` — antes de commitar, roda em sequência check-coverage, check-data-quality, check-flakiness e review-tests (pipeline interno da própria skill).

### Fluxo 2 — Verificar se está pronto para lançar (release readiness)

**Dispara com:** "dá pra lançar essa versão?", "preciso de um go/no-go pra release".

1. `/swl-skill-qa-check-environment` — *dependência real:* confirma health check, seed de dados e feature flags antes de qualquer execução; lê `convencoes-teste.md` se ele existir (gerado por `swl-skill-qa-generate-rules`).
2. `/swl-skill-qa-check-coverage` — confirma que os critérios de aceite da release estão de fato cobertos por cenários, antes de aceitar os números da execução.
3. Execute a suíte (fora do escopo das skills) e gere os arquivos de resultado reais.
4. `/swl-skill-qa-generate-test-report` — *dependência real:* lê o arquivo de resultado real gerado no passo 3.
5. `/swl-skill-qa-check-performance-results` — se houver teste de carga no ciclo; *dependência real:* compara com os thresholds definidos em `swl-skill-qa-new-performance-test`, quando existirem.
6. `/swl-skill-qa-check-security` e `/swl-skill-qa-check-accessibility` — verificações funcionais/dinâmicas adicionais contra o ambiente já confirmado no passo 1. *Ordem entre elas é livre.*
7. `/swl-skill-qa-check-data-quality` — audita o relatório final gerado nos passos anteriores antes de circular para stakeholders, garantindo que nenhum número foi inventado.

### Fluxo 3 — Um teste ou suíte está falhando / vermelho no CI

**Dispara com:** "esse teste quebrou no CI e eu não sei por quê", "a suíte ficou vermelha".

1. `/swl-skill-qa-check-environment` — *ordem sugerida, não obrigatória:* descarta primeiro se o CI está vermelho por ambiente não estar pronto, antes de investigar o teste em si.
2. `/swl-skill-qa-diagnose-failure` — classifica a causa raiz: bug de produto / teste mal escrito / ambiente / flakiness.
3. Conforme a classificação do passo 2 — *dependência real, a própria skill encaminha:*
   - Bug de produto → `/swl-skill-qa-report-bug`
   - Flakiness → `/swl-skill-qa-check-flakiness`
   - Teste mal escrito → corrigir o teste diretamente (sem skill dedicada)
   - Ambiente → sinalizar ao responsável por infraestrutura
4. `/swl-skill-qa-safe-test-commit` — antes de subir a correção do teste ou do bug.

### Fluxo 4 — Assumir ou auditar um conjunto de testes já existente

**Dispara com:** "herdei essa suíte e não sei o estado dela", "projeto legado sem processo de QA definido".

1. `/swl-skill-qa-generate-rules` — quando o projeto não tem `.claude/rules/qa/` definido ainda; é o caso de uso explícito da skill para "projetos legados sem processo de teste definido".
2. `/swl-skill-qa-plan-strategy` — *dependência real:* seu primeiro passo lê `.claude/rules/qa/` (se existirem) e o `CLAUDE.md` para levantar o contexto atual.
3. `/swl-skill-qa-check-flakiness` — varre a suíte existente em busca de instabilidade.
4. `/swl-skill-qa-check-coverage` — cruza os critérios de aceite atuais com os cenários já existentes; aponta gaps e possíveis testes órfãos.
5. `/swl-skill-qa-review-tests` — revisa nomenclatura, qualidade de assert e redundância dos testes existentes.
6. `/swl-skill-qa-risk-priority` — com o cenário completo levantado, prioriza o que vale manter/automatizar vs. testar manualmente daqui pra frente.

### Fluxo 5 — Fechar a entrega depois de uma rodada de testes

**Dispara com:** "terminei de rodar os testes desse ciclo, preciso fechar a entrega", "preciso descrever o PR de testes".

1. `/swl-skill-qa-check-coverage` — *dependência real:* seu resultado é referenciado diretamente no template do passo 5.
2. `/swl-skill-qa-generate-test-report` — relatório executivo a partir do resultado real de execução do ciclo.
3. `/swl-skill-qa-check-data-quality` — audita o relatório recém-gerado antes de circular.
4. `/swl-skill-qa-update-test-docs` — atualiza README de automação, glossário de cenários e mapa de cobertura com base no que mudou na branch.
5. `/swl-skill-qa-describe-test-pr` — *dependência real:* o template gerado já embute "resultado do swl-skill-qa-check-coverage mais recente" (passo 1).
6. `/swl-skill-qa-safe-test-commit` — se ainda houver testes dessa rodada não commitados, roda o pipeline de segurança antes do push final.

### Fluxo 6 — Sessão de teste exploratório e o que fazer com os achados

**Dispara com:** "quero explorar essa área e documentar o que encontrar", "vamos rodar uma sessão exploratória no módulo X".

1. `/swl-skill-qa-exploratory-session` — define charter, conduz a sessão e documenta o que foi de fato observado.
2. Para cada bug encontrado — *dependência real, a própria skill encaminha:* `/swl-skill-qa-report-bug`.
3. Dúvidas de regra de negócio levantadas na sessão vão para PO/dev — fora do escopo das skills.
4. `/swl-skill-qa-risk-priority` — *ordem sugerida:* usa as áreas cobertas/não cobertas da sessão para ajudar a decidir o que virar automação vs. teste manual contínuo.
5. Se algum cenário encontrado virar automação, segue a mesma cadeia do Fluxo 1 a partir do passo 2 (`/swl-skill-qa-new-bdd-scenarios` ou `/swl-skill-qa-new-test-cases` → `/swl-skill-qa-new-test-data` → `/swl-skill-qa-new-automation` → `/swl-skill-qa-safe-test-commit`).

**Pronto pra colar no `CLAUDE.md` do projeto:**

```markdown
## Fluxos comuns de QA (ordem sugerida de skills)

### Funcionalidade nova, testar do zero
1. /swl-skill-qa-plan-strategy (se não houver estratégia definida)
2. /swl-skill-qa-new-bdd-scenarios ou /swl-skill-qa-new-test-cases
3. /swl-skill-qa-risk-priority
4. /swl-skill-qa-new-test-data
5. /swl-skill-qa-new-automation (ou new-mobile-automation / new-performance-test / new-contract-tests)
6. /swl-skill-qa-safe-test-commit

### Verificar release readiness
1. /swl-skill-qa-check-environment
2. /swl-skill-qa-check-coverage
3. (executar a suíte e gerar os arquivos de resultado reais)
4. /swl-skill-qa-generate-test-report
5. /swl-skill-qa-check-performance-results (se houver teste de carga)
6. /swl-skill-qa-check-security e /swl-skill-qa-check-accessibility
7. /swl-skill-qa-check-data-quality

### Teste ou suíte falhando no CI
1. /swl-skill-qa-check-environment (descarta causa de ambiente)
2. /swl-skill-qa-diagnose-failure
3. conforme a classificação: /swl-skill-qa-report-bug (bug de produto) ou /swl-skill-qa-check-flakiness (flakiness)
4. /swl-skill-qa-safe-test-commit

### Assumir/auditar suíte já existente
1. /swl-skill-qa-generate-rules (projeto legado sem .claude/rules/qa)
2. /swl-skill-qa-plan-strategy
3. /swl-skill-qa-check-flakiness
4. /swl-skill-qa-check-coverage
5. /swl-skill-qa-review-tests
6. /swl-skill-qa-risk-priority

### Fechar entrega após rodada de testes
1. /swl-skill-qa-check-coverage
2. /swl-skill-qa-generate-test-report
3. /swl-skill-qa-check-data-quality
4. /swl-skill-qa-update-test-docs
5. /swl-skill-qa-describe-test-pr
6. /swl-skill-qa-safe-test-commit (se houver testes não commitados)

### Sessão exploratória e o que fazer com os achados
1. /swl-skill-qa-exploratory-session
2. /swl-skill-qa-report-bug (para cada bug encontrado)
3. /swl-skill-qa-risk-priority
4. se virar automação: /swl-skill-qa-new-bdd-scenarios ou /swl-skill-qa-new-test-cases -> /swl-skill-qa-new-test-data -> /swl-skill-qa-new-automation -> /swl-skill-qa-safe-test-commit
```

## Preciso de uma URL para testar?

As skills geram ou verificam código de teste — elas não sobem a aplicação. Alguém
(você, o Docker Compose do projeto, o pipeline de CI) precisa ter a aplicação
rodando em algum endereço acessível antes do teste gerado conseguir bater nela.

O que esse "endereço" significa varia por tipo de skill:

| Tipo de skill | O que precisa estar de pé |
|---|---|
| Web/E2E (`swl-skill-qa-new-automation` com Playwright/Cypress/Selenium) | Uma URL — localhost, staging, ou o `baseURL` já configurado no framework |
| API (`swl-skill-qa-new-automation` com RestAssured/Postman, `swl-skill-qa-new-contract-tests`) | Um endpoint base — mesma lógica de URL |
| Mobile (`swl-skill-qa-new-mobile-automation`) | Não é URL — é emulador/simulador ou dispositivo físico rodando, com o app já instalado |
| Performance (`swl-skill-qa-new-performance-test`) | URL/endpoint, com o cuidado de nunca apontar pra produção sem aprovação explícita |
| Contrato (`swl-skill-qa-new-contract-tests`) | Pode não precisar de nada rodando, se o teste for só validação de schema contra um arquivo OpenAPI já existente |

**Recomendação prática:** documente a URL/porta padrão do ambiente local (ou onde
fica o staging) no `CLAUDE.md` do projeto. Assim, as skills que precisam desse
endereço param de ter que perguntar toda vez.

Antes de rodar a suíte, vale confirmar que esse endereço está de pé de verdade —
é exatamente pra isso que existe a
[swl-skill-qa-check-environment](skills/swl-skill-qa-check-environment.html):
ela confirma health check dos serviços, seed de dados e feature flags antes da
execução, em vez de você descobrir no meio da suíte que o ambiente não respondia.
"""

install_html = render_md(install_md)

full_text = install_md + " ".join(s["name"] for s in SKILLS)
words, minutes = word_count_and_time(full_text)
meta_line = f"{words} palavras&nbsp;&nbsp;|&nbsp;&nbsp;{minutes} min"

body_html = f"""
<div class="eyebrow"><span class="cat-pill">Fundamentos</span></div>
<h1>Como instalar e usar</h1>
<p>Instruções para instalar as skills de QA da Base2 no Claude Code e adaptá-las ao
contexto do seu projeto.</p>

<h2>Baixar as skills</h2>
{download_html}

{install_html}

<h2>Todos os comandos</h2>
<table>
<thead><tr><th>Comando</th><th>O que faz</th></tr></thead>
<tbody>
{command_rows}
</tbody>
</table>
"""

html = page_shell(
    base=base,
    title_tag="Como instalar e usar",
    active_folder=None,
    active_page="instalacao",
    meta_line=meta_line,
    body_html=body_html,
)
with open(f"{OUT_DIR}/instalacao.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Built instalacao.html")
