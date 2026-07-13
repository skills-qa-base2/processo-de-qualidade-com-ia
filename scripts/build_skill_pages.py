import json, re, os, math, base64
import markdown as md

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

with open(os.path.join(SCRIPT_DIR, "skills_data.json"), encoding="utf-8") as f:
    SKILLS = json.load(f)

CATEGORY_ORDER = ["Planejamento", "Geração", "Verificação", "Diagnóstico", "Entrega"]

SITE_NAME = "Processo de Qualidade com IA"

OUT_DIR = REPO_ROOT

with open(f"{OUT_DIR}/assets/style.css", encoding="utf-8") as f:
    CSS_CONTENT = f.read()

with open(f"{OUT_DIR}/assets/app.js", encoding="utf-8") as f:
    JS_CONTENT = f.read()

with open(f"{OUT_DIR}/assets/banner_base2.png", "rb") as f:
    BANNER_B64 = base64.b64encode(f.read()).decode("ascii")
BANNER_DATA_URI = f"data:image/png;base64,{BANNER_B64}"

def slug(folder):
    return folder  # use full folder name as filename, e.g. swl-skill-qa-plan-strategy

def skill_url(folder, base=""):
    return f"{base}skills/{slug(folder)}.html"

def word_count_and_time(text):
    words = len(re.findall(r"\S+", text))
    minutes = max(1, math.ceil(words / 220))
    return words, minutes

def render_md(text):
    return md.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])

def preprocess_steps_md(text):
    """Fix common formatting quirks in the SKILL.md bodies:
    - insert a blank line before bullet/numbered lists glued to the previous paragraph
    - demote numbered '## N. Título' sub-steps to h3, keep 'Passos' as the single h2
    """
    lines = text.split("\n")
    out = []
    list_item_re = re.compile(r"^\s*(-\s+|\d+\.\s+)")
    for i, line in enumerate(lines):
        if list_item_re.match(line):
            prev = out[-1] if out else ""
            if prev.strip() != "" and not list_item_re.match(prev):
                out.append("")
        out.append(line)
    text = "\n".join(out)

    # Demote "## N. Something" to "### N. Something", keep plain "## Passos" as-is
    text = re.sub(r"^## (\d+\.\s.*)$", r"### \1", text, flags=re.M)
    return text

_SEARCH_INDEX_CACHE = None

def build_search_index_json():
    global _SEARCH_INDEX_CACHE
    if _SEARCH_INDEX_CACHE is not None:
        return _SEARCH_INDEX_CACHE
    items = []
    items.append({
        "title": "Início",
        "desc": "Visão geral das skills de QA da Base2 para Claude Code.",
        "url": "index.html",
        "command": "",
        "category": "Fundamentos",
    })
    items.append({
        "title": "Como instalar e usar",
        "desc": "Instalação por projeto ou global, e como personalizar via CLAUDE.md.",
        "url": "instalacao.html",
        "command": "",
        "category": "Fundamentos",
    })
    for s in SKILLS:
        items.append({
            "title": s["title"],
            "desc": s["description"],
            "url": skill_url(s["folder"]),
            "command": f"/{s['name']}",
            "category": s["category"],
        })
    _SEARCH_INDEX_CACHE = json.dumps(items, ensure_ascii=False)
    return _SEARCH_INDEX_CACHE

def nav_html(base, active_folder=None, active_page=None):
    groups = {c: [] for c in CATEGORY_ORDER}
    for s in SKILLS:
        groups[s["category"]].append(s)

    out = []
    out.append('<div class="nav-group">')
    out.append('<div class="nav-group-label">// FUNDAMENTOS</div>')
    out.append('<ul>')
    out.append(f'<li><a href="{base}index.html" class="{"active" if active_page=="index" else ""}">Início</a></li>')
    out.append(f'<li><a href="{base}instalacao.html" class="{"active" if active_page=="instalacao" else ""}">Como instalar e usar</a></li>')
    out.append('</ul></div>')

    for cat in CATEGORY_ORDER:
        out.append('<div class="nav-group">')
        out.append(f'<div class="nav-group-label">// {cat.upper()}</div>')
        out.append('<ul>')
        for s in groups[cat]:
            active_cls = "active" if s["folder"] == active_folder else ""
            out.append(f'<li><a href="{skill_url(s["folder"], base)}" class="{active_cls}">{s["title"]}</a></li>')
        out.append('</ul></div>')
    return "\n".join(out)

def page_shell(base, title_tag, active_folder, active_page, meta_line, body_html, prev_next=""):
    search_index_json = build_search_index_json()

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_tag} · {SITE_NAME}</title>
<meta name="description" content="{SITE_NAME} · Skills de QA da Base2 Tecnologia para Claude Code.">
<style>
{CSS_CONTENT}
</style>
</head>
<body>

<div class="banner-wrap">
  <img src="{BANNER_DATA_URI}" alt="Base2 — Qualidade que destrava o crescimento" />
</div>

<div class="utility-bar">
  <div class="crumb">
    <a href="{base}index.html"><b>BASE2</b></a>
    <span class="sep">/</span>
    <span>{SITE_NAME}</span>
  </div>
  <div style="display:flex; align-items:center; gap:8px;">
    <button class="menu-toggle" data-menu-toggle type="button">☰ menu</button>
    <button class="theme-toggle" data-theme-toggle type="button">◐ escuro</button>
  </div>
</div>

<div class="layout">
  <aside class="sidebar">
    <div class="search-box">
      <input type="text" placeholder="Buscar na documentação..." data-search-input data-base="{base}">
      <div class="search-results" data-search-results></div>
    </div>
    {nav_html(base, active_folder, active_page)}
  </aside>

  <main class="content">
    <div class="content-meta">{meta_line}</div>
    {body_html}
    {prev_next}
    <div class="footer-note">Base2 Tecnologia · {SITE_NAME} · mantido pela equipe de engenharia</div>
  </main>
</div>

<script>
window.SKILLS_SEARCH_INDEX = {search_index_json};
</script>
<script>
{JS_CONTENT}
</script>
</body>
</html>
"""

def prev_next_block(base, idx):
    parts = []
    if idx > 0:
        p = SKILLS[idx - 1]
        parts.append(f'<a href="{skill_url(p["folder"], base)}"><span class="pn-label">◄ anterior</span>{p["title"]}</a>')
    else:
        parts.append('<span></span>')
    if idx < len(SKILLS) - 1:
        n = SKILLS[idx + 1]
        parts.append(f'<a class="pn-next" href="{skill_url(n["folder"], base)}"><span class="pn-label">próxima ►</span>{n["title"]}</a>')
    else:
        parts.append('<span></span>')
    return f'<div class="page-nav">{"".join(parts)}</div>'

# ---------------------------------------------------------------
# Skill pages
# ---------------------------------------------------------------
def build_skill_page(s, idx):
    base = "../"
    full_text_for_count = s["description"] + " " + s["body_md"] + " " + (s["guardrail_md"] or "")
    words, minutes = word_count_and_time(full_text_for_count)
    meta_line = f"{words} palavras&nbsp;&nbsp;|&nbsp;&nbsp;{minutes} min"

    body_md_html = render_md(preprocess_steps_md(s["body_md"]))
    guardrail_html = ""
    if s["guardrail_md"]:
        guardrail_html = f"""
        <div class="guardrail-box">
          <div class="g-label">⚑ GUARDRAIL ANTI-INVENÇÃO</div>
          {render_md(s["guardrail_md"])}
        </div>
        """

    body_html = f"""
    <div class="eyebrow">
      <span class="cat-pill">{s['category']}</span>
      <span class="ver">versão {s['version']}</span>
    </div>
    <h1>{s['title']}</h1>
    <p>{s['description']}</p>

    <div class="usage-block">
      <div>
        <div class="usage-label">COMANDO</div>
        <div class="usage-cmd">/{s['name']} {s['argument_hint']}</div>
      </div>
    </div>

    {body_md_html}
    {guardrail_html}
    """

    html = page_shell(
        base=base,
        title_tag=s["title"],
        active_folder=s["folder"],
        active_page="skill",
        meta_line=meta_line,
        body_html=body_html,
        prev_next=prev_next_block(base, idx),
    )
    out_path = os.path.join(OUT_DIR, "skills", f"{slug(s['folder'])}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

for i, s in enumerate(SKILLS):
    build_skill_page(s, i)

print(f"Built {len(SKILLS)} skill pages")
