# Base2 Skills de QA para Claude Code

Skills de QA da Base2 Tecnologia para uso com **Claude Code CLI**. Cobrem frontend/web, API, integração, contrato, mobile e performance — funcionam em qualquer projeto, independente de stack ou framework de automação (Playwright, Cypress, Selenium, Robot Framework, RestAssured, Postman/Newman, Testcontainers, WireMock/MockServer, Appium, Espresso, XCUITest, Detox, Maestro, k6, JMeter, Gatling, Artillery, Cucumber, SpecFlow).

---

## O que são as skills?

Skills são instruções salvas que o Claude executa quando você digita um comando `/nome-da-skill` no Claude Code. Elas padronizam tarefas repetitivas de QA como planejar estratégia de teste, gerar cenários BDD/casos de teste, automatizar, criar massa de dados fictícia e verificar qualidade antes de commitar.

---

## Como instalar

### Opção 1 — Projeto específico

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

### Opção 2 — Disponível globalmente (usuário)

Copie as pastas das skills para o diretório global do Claude Code:

```powershell
# Windows
Copy-Item -Recurse ".\skills\swl-skill-qa-plan-strategy" "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse ".\skills\swl-skill-qa-new-test-cases" "$env:USERPROFILE\.claude\skills\"
# ... repita para cada skill desejada
```

```bash
# macOS / Linux
cp -r ./skills/swl-skill-qa-plan-strategy ~/.claude/skills/
cp -r ./skills/swl-skill-qa-new-test-cases ~/.claude/skills/
# ... repita para cada skill desejada
```

As skills ficam disponíveis em todos os projetos do usuário.

---

## Como usar

Com o Claude Code aberto em qualquer projeto, digite:

| Comando | O que faz |
|---|---|
| `/swl-skill-qa-plan-strategy` | Entrevista estruturada para definir a estratégia de testes antes de gerar qualquer cenário |
| `/swl-skill-qa-new-bdd-scenarios` | Gera cenários BDD (Gherkin) a partir de critérios de aceite |
| `/swl-skill-qa-new-test-cases` | Gera casos de teste estruturados a partir de uma user story |
| `/swl-skill-qa-new-test-data` | Gera massa de dados de teste fictícia via factories/fixtures |
| `/swl-skill-qa-new-automation` | Gera código de automação web/API/integração detectando o framework do projeto |
| `/swl-skill-qa-new-mobile-automation` | Gera código de automação mobile (Appium/Espresso/XCUITest/Detox/Maestro) |
| `/swl-skill-qa-new-contract-tests` | Gera testes de contrato/schema de API (OpenAPI/Pact) a partir de especificação real |
| `/swl-skill-qa-new-performance-test` | Gera script de teste de carga/stress/spike/soak (k6/JMeter/Gatling/Artillery) |
| `/swl-skill-qa-check-performance-results` | Analisa resultado real de teste de carga contra thresholds definidos |
| `/swl-skill-qa-check-coverage` | Analisa gaps de cobertura funcional (critérios x cenários) |
| `/swl-skill-qa-check-flakiness` | Detecta padrões de instabilidade em testes automatizados |
| `/swl-skill-qa-check-data-quality` | Audita relatórios/documentos de QA gerados por IA contra dados fabricados |
| `/swl-skill-qa-review-tests` | Revisa testes quanto a nomenclatura, asserts e cobertura real |
| `/swl-skill-qa-risk-priority` | Prioriza cenários por criticidade de negócio e risco técnico |
| `/swl-skill-qa-diagnose-failure` | Rastreia uma falha de teste até a causa raiz |
| `/swl-skill-qa-report-bug` | Gera relatório de bug estruturado |
| `/swl-skill-qa-exploratory-session` | Conduz e documenta uma sessão de teste exploratório |
| `/swl-skill-qa-generate-rules` | Gera `.claude/rules/qa/` a partir de documentação ou entrevista |
| `/swl-skill-qa-generate-test-report` | Gera relatório executivo a partir de execução real (JSON/XML) |
| `/swl-skill-qa-describe-test-pr` | Gera descrição de PR de testes |
| `/swl-skill-qa-update-test-docs` | Atualiza README/glossário/mapa de cobertura de testes |
| `/swl-skill-qa-safe-test-commit` | Pipeline completo (coverage, data-quality, flakiness, review) antes de commit |

---

## Skills disponíveis

| Skill | Categoria | Descrição |
|---|---|---|
| `swl-skill-qa-plan-strategy` | Planejamento | Entrevista estruturada para levantar a estratégia de testes |
| `swl-skill-qa-generate-rules` | Planejamento | Gera project rules de QA a partir de documentação ou entrevista |
| `swl-skill-qa-new-bdd-scenarios` | Geração | Cenários BDD em Gherkin a partir de critérios de aceite |
| `swl-skill-qa-new-test-cases` | Geração | Casos de teste estruturados a partir de user story |
| `swl-skill-qa-new-test-data` | Geração | Massa de dados fictícia via factories/fixtures |
| `swl-skill-qa-new-automation` | Geração | Código de automação web/API/integração detectando o framework do projeto |
| `swl-skill-qa-new-mobile-automation` | Geração | Código de automação mobile (Appium/Espresso/XCUITest/Detox/Maestro) |
| `swl-skill-qa-new-contract-tests` | Geração | Testes de contrato/schema de API (OpenAPI/Pact) |
| `swl-skill-qa-new-performance-test` | Geração | Script de teste de carga/stress/spike/soak |
| `swl-skill-qa-check-performance-results` | Verificação | Resultado real de teste de carga contra thresholds |
| `swl-skill-qa-check-coverage` | Verificação | Gaps de cobertura funcional |
| `swl-skill-qa-check-flakiness` | Verificação | Padrões de instabilidade em testes automatizados |
| `swl-skill-qa-check-data-quality` | Verificação | Dados fabricados em relatórios/documentos gerados por IA |
| `swl-skill-qa-review-tests` | Verificação | Nomenclatura, asserts e cobertura real de testes |
| `swl-skill-qa-risk-priority` | Verificação | Priorização de cenários por risco |
| `swl-skill-qa-diagnose-failure` | Diagnóstico | Causa raiz de falha de teste |
| `swl-skill-qa-report-bug` | Diagnóstico | Relatório de bug estruturado |
| `swl-skill-qa-exploratory-session` | Diagnóstico | Sessão de teste exploratório documentada |
| `swl-skill-qa-generate-test-report` | Entrega | Relatório executivo a partir de execução real |
| `swl-skill-qa-describe-test-pr` | Entrega | Descrição de PR de testes |
| `swl-skill-qa-update-test-docs` | Entrega | Atualização de documentação de testes |
| `swl-skill-qa-safe-test-commit` | Entrega | Pipeline de qualidade antes de commit |

---

## Como personalizar para um projeto

As skills leem o `CLAUDE.md` do projeto (e `.claude/rules/qa/`, quando gerado por `swl-skill-qa-generate-rules`) para adaptar o comportamento ao contexto específico. Documente no `CLAUDE.md` do seu projeto:

- Framework de automação e padrão de organização (ex: Page Object Model)
- Ferramenta de gestão de casos de teste em uso
- Convenções de nomenclatura de cenários
- Política de dados de teste

Quanto mais completo o `CLAUDE.md`, mais preciso o resultado das skills.

---

## Princípio comum a todas as skills

Toda skill desta coleção tem um guardrail contra fabricação: diante de informação ausente ou ambígua (regra de negócio não confirmada, severidade desconhecida, dado sem fonte rastreável), a skill deve marcar o ponto como pendente (`a confirmar`, `[REGRA A CONFIRMAR COM PO]`) em vez de inventar. Esse comportamento foi validado com testes adversariais antes da publicação desta versão — ver histórico em [MANIFEST.md](MANIFEST.md).

---

## Versões e atualizações

Consulte [MANIFEST.md](MANIFEST.md) para verificar as versões disponíveis e o histórico de mudanças.

---

*Mantido pela equipe de engenharia da Base2 Tecnologia.*
