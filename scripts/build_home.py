import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_skill_pages import (
    SKILLS, CATEGORY_ORDER, page_shell, skill_url, word_count_and_time, render_md, OUT_DIR
)

# Search index is now embedded inline in every page by page_shell(); no external file needed.

# ---------------------------------------------------------------
# index.html (home)
# ---------------------------------------------------------------
def build_home():
    base = ""
    intro_text = """
    Skills de QA da Base2 Tecnologia para uso com Claude Code. Cobrem frontend/web, API,
    integração, contrato, mobile e performance, funcionando em qualquer projeto,
    independente de stack ou framework de automação.
    """
    words, minutes = word_count_and_time(intro_text + " ".join(s["description"] for s in SKILLS))
    meta_line = f"{words} palavras&nbsp;&nbsp;|&nbsp;&nbsp;{minutes} min"

    groups = {c: [] for c in CATEGORY_ORDER}
    for s in SKILLS:
        groups[s["category"]].append(s)

    validated_skills = [s for s in SKILLS if s["validated"]]
    pending_skills = [s for s in SKILLS if not s["validated"]]
    if pending_skills:
        pending_names = ", ".join(f"<code>/{s['name']}</code>" for s in pending_skills)
        validation_sentence = (
            f"{len(validated_skills)} de {len(SKILLS)} skills já foram validadas com teste "
            f"adversarial antes da publicação. {len(pending_skills)} ainda "
            f"{'está' if len(pending_skills) == 1 else 'estão'} pendente"
            f"{'' if len(pending_skills) == 1 else 's'}: {pending_names}."
        )
    else:
        validation_sentence = (
            f"Todas as {len(SKILLS)} skills já foram validadas com teste adversarial antes da publicação."
        )

    cards_html = []
    for cat in CATEGORY_ORDER:
        items = groups[cat]
        cards = []
        for s in items:
            cards.append(f"""
            <a class="skill-card" href="{skill_url(s['folder'], base)}">
              <div class="sc-title">{s['title']}</div>
              <div class="sc-cmd">/{s['name']}</div>
              <div class="sc-desc">{s['description']}</div>
              <div class="sc-go">Ver skill ✦</div>
            </a>
            """)
        cards_html.append(f"""
        <div class="cat-section">
          <h2>{cat} <span class="cat-count">{len(items)} skills</span></h2>
          <div class="card-grid">{''.join(cards)}</div>
        </div>
        """)

    body_html = f"""
    <div class="eyebrow"><span class="cat-pill">Documentação</span></div>
    <h1>Processo de Qualidade com IA</h1>
    <p>Skills de QA da Base2 Tecnologia para uso com Claude Code. Cobrem frontend/web, API,
    integração, contrato, mobile e performance, funcionando em qualquer projeto,
    independente de stack ou framework de automação.</p>
    <p>Skills são instruções salvas que o Claude executa quando você digita um comando
    <code>/nome-da-skill</code> no Claude Code. Elas padronizam tarefas repetitivas de QA
    como planejar estratégia de teste, gerar cenários BDD/casos de teste, automatizar,
    criar massa de dados fictícia e verificar qualidade antes de commitar.</p>

    <div class="callout">
      <div class="callout-label">// PRINCÍPIO-GUIA</div>
      <p><strong>Diante de dúvida, a skill sinaliza como pendente — nunca inventa.</strong></p>
      <p>Toda skill desta coleção tem um guardrail contra fabricação: diante de informação
      ausente ou ambígua (regra de negócio não confirmada, severidade desconhecida, dado sem
      fonte rastreável), a skill marca o ponto como pendente em vez de inventar. {validation_sentence}</p>
    </div>

    <p>Comece por <a href="{base}instalacao.html" style="color:var(--green); font-weight:600;">como instalar e usar</a>,
    ou explore as skills abaixo, organizadas por categoria.</p>

    {''.join(cards_html)}
    """

    html = page_shell(
        base=base,
        title_tag="Início",
        active_folder=None,
        active_page="index",
        meta_line=meta_line,
        body_html=body_html,
    )
    with open(f"{OUT_DIR}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

build_home()
print("Built index.html")
