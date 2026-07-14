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
