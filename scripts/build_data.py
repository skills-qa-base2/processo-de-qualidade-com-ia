import os, re, json, yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
SKILLS_DIR = os.path.join(REPO_ROOT, "qa-skills-package", "skills")

CATEGORY_ORDER = ["Planejamento", "Geração", "Verificação", "Diagnóstico", "Entrega"]

CATEGORY_MAP = {
    "swl-skill-qa-plan-strategy": "Planejamento",
    "swl-skill-qa-generate-rules": "Planejamento",
    "swl-skill-qa-new-bdd-scenarios": "Geração",
    "swl-skill-qa-new-test-cases": "Geração",
    "swl-skill-qa-new-test-data": "Geração",
    "swl-skill-qa-new-automation": "Geração",
    "swl-skill-qa-new-mobile-automation": "Geração",
    "swl-skill-qa-new-contract-tests": "Geração",
    "swl-skill-qa-new-performance-test": "Geração",
    "swl-skill-qa-check-performance-results": "Verificação",
    "swl-skill-qa-check-coverage": "Verificação",
    "swl-skill-qa-check-flakiness": "Verificação",
    "swl-skill-qa-check-data-quality": "Verificação",
    "swl-skill-qa-check-security": "Verificação",
    "swl-skill-qa-check-accessibility": "Verificação",
    "swl-skill-qa-check-environment": "Verificação",
    "swl-skill-qa-review-tests": "Verificação",
    "swl-skill-qa-risk-priority": "Verificação",
    "swl-skill-qa-diagnose-failure": "Diagnóstico",
    "swl-skill-qa-report-bug": "Diagnóstico",
    "swl-skill-qa-exploratory-session": "Diagnóstico",
    "swl-skill-qa-generate-test-report": "Entrega",
    "swl-skill-qa-describe-test-pr": "Entrega",
    "swl-skill-qa-update-test-docs": "Entrega",
    "swl-skill-qa-safe-test-commit": "Entrega",
}

# Nice short display titles (Portuguese, human readable) for nav/cards
TITLE_MAP = {
    "swl-skill-qa-plan-strategy": "Planejar estratégia de testes",
    "swl-skill-qa-generate-rules": "Gerar regras de QA do projeto",
    "swl-skill-qa-new-bdd-scenarios": "Gerar cenários BDD",
    "swl-skill-qa-new-test-cases": "Gerar casos de teste",
    "swl-skill-qa-new-test-data": "Gerar massa de dados de teste",
    "swl-skill-qa-new-automation": "Gerar automação (web/API/integração)",
    "swl-skill-qa-new-mobile-automation": "Gerar automação mobile",
    "swl-skill-qa-new-contract-tests": "Gerar testes de contrato",
    "swl-skill-qa-new-performance-test": "Gerar teste de performance",
    "swl-skill-qa-check-performance-results": "Verificar resultado de performance",
    "swl-skill-qa-check-coverage": "Verificar cobertura de cenários",
    "swl-skill-qa-check-flakiness": "Detectar flakiness",
    "swl-skill-qa-check-data-quality": "Auditar qualidade de dados",
    "swl-skill-qa-check-security": "Verificar segurança (multi-stack)",
    "swl-skill-qa-check-accessibility": "Auditar acessibilidade",
    "swl-skill-qa-check-environment": "Validar ambiente de teste",
    "swl-skill-qa-review-tests": "Revisar testes",
    "swl-skill-qa-risk-priority": "Priorizar por risco",
    "swl-skill-qa-diagnose-failure": "Diagnosticar falha de teste",
    "swl-skill-qa-report-bug": "Reportar bug",
    "swl-skill-qa-exploratory-session": "Conduzir sessão exploratória",
    "swl-skill-qa-generate-test-report": "Gerar relatório de execução",
    "swl-skill-qa-describe-test-pr": "Descrever PR de testes",
    "swl-skill-qa-update-test-docs": "Atualizar documentação de testes",
    "swl-skill-qa-safe-test-commit": "Pipeline de commit seguro",
}

def parse_skill(folder):
    path = os.path.join(SKILLS_DIR, folder, "SKILL.md")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    front_raw, body = m.group(1), m.group(2).strip()
    front = yaml.safe_load(front_raw)
    version = front.get("metadata", {}).get("version", "1.0.0")
    validated = front["metadata"]["validated"]

    # Split out Guardrail section
    guardrail = None
    gmatch = re.search(r"\n## Guardrail\n(.*)$", body, re.S)
    if gmatch:
        guardrail = gmatch.group(1).strip()
        body = body[:gmatch.start()].strip()

    return {
        "folder": folder,
        "name": front["name"],
        "description": front["description"],
        "argument_hint": front.get("argument-hint", ""),
        "version": version,
        "validated": validated,
        "category": CATEGORY_MAP.get(folder, "Outros"),
        "title": TITLE_MAP.get(folder, folder),
        "body_md": body,
        "guardrail_md": guardrail,
    }

def main():
    folders = sorted(os.listdir(SKILLS_DIR))
    skills = [parse_skill(f) for f in folders if os.path.isdir(os.path.join(SKILLS_DIR, f))]
    skills.sort(key=lambda s: (CATEGORY_ORDER.index(s["category"]), s["title"]))
    with open(os.path.join(SCRIPT_DIR, "skills_data.json"), "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)
    print(f"Parsed {len(skills)} skills")

if __name__ == "__main__":
    main()
