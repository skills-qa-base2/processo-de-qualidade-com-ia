# Processo de Qualidade com IA — Base2

Coleção de skills de QA da Base2 Tecnologia para uso com **Claude Code**, com um site de
documentação para consulta e instalação.

Repositório: https://github.com/skills-qa-base2/processo-de-qualidade-com-ia

---

## O que é

Skills são instruções salvas que o Claude executa quando você digita um comando
`/nome-da-skill` no Claude Code. Essa coleção reúne **25 skills** que padronizam as tarefas
mais repetitivas de QA — planejar estratégia de teste, gerar cenários BDD e casos de teste,
automatizar, criar massa de dados fictícia, verificar qualidade antes de commitar, diagnosticar
falhas e fechar a entrega (relatório, PR, documentação).

Funcionam em qualquer projeto, independente de stack ou framework de automação: Playwright,
Cypress, Selenium, Robot Framework, RestAssured, Postman/Newman, Testcontainers,
WireMock/MockServer, Appium, Espresso, XCUITest, Detox, Maestro, k6, JMeter, Gatling,
Artillery, Cucumber, SpecFlow.

## Princípio comum a todas as skills

**Guardrail anti-invenção:** diante de informação ausente ou ambígua (regra de negócio não
confirmada, severidade desconhecida, dado sem fonte rastreável), a skill marca o ponto como
pendente (`a confirmar`) em vez de inventar. Esse comportamento foi validado com testes
adversariais antes da publicação — histórico completo em
[`qa-skills-package/MANIFEST.md`](qa-skills-package/MANIFEST.md).

## As 25 skills, por categoria

**Planejamento** (2) — antes de gerar qualquer cenário
- `swl-skill-qa-plan-strategy` — entrevista estruturada para levantar a estratégia de testes
- `swl-skill-qa-generate-rules` — gera `.claude/rules/qa/` a partir de documentação ou entrevista

**Geração** (7) — cenários, dados e automação
- `swl-skill-qa-new-bdd-scenarios` — cenários BDD (Gherkin) a partir de critérios de aceite
- `swl-skill-qa-new-test-cases` — casos de teste estruturados a partir de user story
- `swl-skill-qa-new-test-data` — massa de dados fictícia via factories/fixtures
- `swl-skill-qa-new-automation` — automação web/API/integração, detectando o framework do projeto
- `swl-skill-qa-new-mobile-automation` — automação mobile (Appium/Espresso/XCUITest/Detox/Maestro)
- `swl-skill-qa-new-contract-tests` — testes de contrato/schema de API (OpenAPI/Pact)
- `swl-skill-qa-new-performance-test` — script de carga/stress/spike/soak (k6/JMeter/Gatling/Artillery)

**Verificação** (9) — antes de confiar no resultado
- `swl-skill-qa-check-coverage` — gaps de cobertura funcional (critérios x cenários)
- `swl-skill-qa-check-flakiness` — padrões de instabilidade em testes automatizados
- `swl-skill-qa-check-data-quality` — audita relatórios/documentos de QA gerados por IA
- `swl-skill-qa-review-tests` — nomenclatura, asserts e cobertura real dos testes
- `swl-skill-qa-risk-priority` — prioriza cenários por criticidade de negócio e risco técnico
- `swl-skill-qa-check-performance-results` — resultado real de carga contra thresholds definidos
- `swl-skill-qa-check-security` — verificação de segurança stack-agnóstica (Node/Python/Java/mobile), complementar à check-security .NET do org-skills
- `swl-skill-qa-check-accessibility` — audita acessibilidade (WCAG) via ferramenta já presente no projeto
- `swl-skill-qa-check-environment` — valida que o ambiente está pronto antes da execução (health check, seed, feature flags)

**Diagnóstico** (3) — quando algo falha
- `swl-skill-qa-diagnose-failure` — rastreia uma falha até a causa raiz
- `swl-skill-qa-report-bug` — relatório de bug estruturado
- `swl-skill-qa-exploratory-session` — conduz e documenta uma sessão de teste exploratório

**Entrega** (4) — fechando o ciclo
- `swl-skill-qa-generate-test-report` — relatório executivo a partir de execução real
- `swl-skill-qa-describe-test-pr` — descrição de PR de testes
- `swl-skill-qa-update-test-docs` — atualiza README/glossário/mapa de cobertura
- `swl-skill-qa-safe-test-commit` — pipeline completo (coverage, data-quality, flakiness, review) antes de commitar

A descrição completa, o comando exato e os passos de cada skill estão na página dela dentro
do site (`skills/swl-skill-qa-<nome>.html`) ou no `SKILL.md` correspondente em
`qa-skills-package/skills/`.

---

## Como instalar

**Baixe** o pacote (`downloads/qa-skills-package.zip`, ou clone este repositório) e copie
as skills que quiser para dentro do seu projeto ou do seu usuário:

```bash
# por projeto — fica disponível só ali
cp -r ./qa-skills-package/skills/swl-skill-qa-plan-strategy seu-projeto/.claude/skills/

# globalmente — fica disponível em todos os projetos do usuário
cp -r ./qa-skills-package/skills/swl-skill-qa-plan-strategy ~/.claude/skills/
```

Para instalar todas de uma vez, instruções passo a passo (Windows e macOS/Linux) e como
personalizar via `CLAUDE.md`, veja a página **Como instalar e usar** do site
(`instalacao.html`).

Depois de instalada, use no Claude Code digitando o comando da skill (ex:
`/swl-skill-qa-plan-strategy`) seguido do argumento indicado.

---

## Estrutura do repositório

```
.
├── index.html                  → site: página inicial
├── instalacao.html              → site: como instalar e usar (com botão de download)
├── skills/
│   └── swl-skill-qa-*.html      → site: uma página por skill (25 no total)
├── downloads/
│   └── qa-skills-package.zip    → gerado a partir de qa-skills-package/ — não editar na mão
├── assets/
│   ├── style.css                → estilo-fonte do site (referência/edição)
│   ├── app.js                   → script-fonte do site (referência/edição)
│   └── banner_base2.png         → banner original da Base2
├── qa-skills-package/
│   ├── skills/*/SKILL.md        → fonte real de cada skill — o que de fato importa aqui
│   ├── README.md                → como instalar as skills (visão resumida)
│   └── MANIFEST.md              → versões e histórico de validação de cada skill
└── scripts/                      → geradores do site, a partir de qa-skills-package/
    ├── build_data.py
    ├── build_downloads.py
    ├── build_skill_pages.py
    ├── build_home.py
    └── build_instalacao.py
```

O que importa de verdade neste repositório é `qa-skills-package/skills/*/SKILL.md` — é a
fonte real de cada skill. Tudo em `index.html`, `instalacao.html`, `skills/*.html` e
`downloads/qa-skills-package.zip` é **gerado** a partir dela pelos scripts em `scripts/`.
Se precisar mudar o comportamento de uma skill, edite o `SKILL.md` correspondente, nunca o
HTML gerado.

---

## Como atualizar as skills (e o site)

Pré-requisitos: Python 3 com `markdown` e `PyYAML` (`pip install markdown pyyaml`).

Depois de editar um `SKILL.md` em `qa-skills-package/skills/`, rode a partir da pasta
`scripts/`, nessa ordem:

```bash
cd scripts
python3 build_data.py          # relê todas as SKILL.md → scripts/skills_data.json
python3 build_downloads.py     # regenera downloads/qa-skills-package.zip
python3 build_skill_pages.py   # regenera skills/*.html
python3 build_home.py          # regenera index.html
python3 build_instalacao.py    # regenera instalacao.html
```

**Adicionando uma skill nova:** crie a pasta
`qa-skills-package/skills/swl-skill-qa-<nome>/SKILL.md` seguindo o formato das demais
(frontmatter `name`/`description`/`argument-hint`/`metadata.version`, seção `## Passos` e
seção `## Guardrail`), registre-a em `CATEGORY_MAP` e `TITLE_MAP` no topo de
`scripts/build_data.py`, e rode os cinco scripts acima.

**Renomeando o site:** a constante `SITE_NAME` no topo de `scripts/build_skill_pages.py`.

---

## Identidade visual do site

- Verde escuro `#004d3d`, verde médio `#00964f`, lima `#9edc37` — paleta oficial Base2.
- O banner (`assets/banner_base2.png`) é usado sem nenhuma alteração, em largura total.
- Tipografia: Inter (texto) + mono (rótulos, comandos e código).

---

*Mantido pela equipe de engenharia da Base2 Tecnologia.*
