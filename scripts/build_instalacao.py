import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_skill_pages import SKILLS, page_shell, render_md, word_count_and_time, OUT_DIR

base = ""

command_rows = "\n".join(
    f"<tr><td><code>/{s['name']}</code></td><td>{s['description']}</td></tr>"
    for s in SKILLS
)

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
