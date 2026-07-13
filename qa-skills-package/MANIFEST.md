# Base2 Skills de QA — Manifest

Skills de QA da Base2 Tecnologia para Claude Code. Cobrem frontend/web, API, integração, contrato, mobile e performance — funcionam em qualquer projeto, independente de stack ou framework de automação.

## Skills disponíveis

| Skill | Versão | Categoria | Descrição |
|---|---|---|---|
| `swl-skill-qa-plan-strategy` | 1.0.0 | Planejamento | Entrevista estruturada para levantar a estratégia de testes de um projeto ou feature antes de gerar qualquer cenário |
| `swl-skill-qa-generate-rules` | 1.0.0 | Planejamento | Gera `.claude/rules/qa/` a partir de documentação técnica existente ou entrevista com o time |
| `swl-skill-qa-new-bdd-scenarios` | 1.0.0 | Geração | Gera cenários BDD em Gherkin a partir de critérios de aceite |
| `swl-skill-qa-new-test-cases` | 1.0.0 | Geração | Gera casos de teste estruturados a partir de user story, cobrindo happy path, edge cases e negativos |
| `swl-skill-qa-new-test-data` | 1.0.0 | Geração | Gera massa de dados de teste fictícia via factories/fixtures |
| `swl-skill-qa-new-automation` | 1.1.0 | Geração | Gera código de automação web/API/integração detectando o framework do projeto (Playwright, Cypress, Selenium, Robot Framework, RestAssured, Postman/Newman, Testcontainers, WireMock/MockServer, Cucumber, SpecFlow) |
| `swl-skill-qa-new-mobile-automation` | 1.0.0 | Geração | Gera código de automação mobile detectando o framework do projeto (Appium, Espresso, XCUITest, Detox, Maestro) |
| `swl-skill-qa-new-contract-tests` | 1.0.0 | Geração | Gera testes de contrato/schema de API (OpenAPI/JSON Schema, Pact/Spring Cloud Contract) a partir de especificação real |
| `swl-skill-qa-new-performance-test` | 1.0.0 | Geração | Gera scripts de teste de performance (smoke/load/stress/spike/soak) detectando a ferramenta do projeto (k6, JMeter, Gatling, Artillery) |
| `swl-skill-qa-check-performance-results` | 1.0.0 | Verificação | Analisa resultado real de execução de teste de performance contra thresholds definidos |
| `swl-skill-qa-check-coverage` | 1.0.0 | Verificação | Analisa gaps de cobertura de cenários frente a requisitos e critérios de aceite |
| `swl-skill-qa-check-flakiness` | 1.0.0 | Verificação | Detecta padrões de instabilidade em testes automatizados |
| `swl-skill-qa-check-data-quality` | 1.0.0 | Verificação | Audita documentos/relatórios de QA gerados por IA em busca de dados fabricados |
| `swl-skill-qa-review-tests` | 1.0.0 | Verificação | Revisa testes quanto a nomenclatura, clareza de asserts e cobertura real |
| `swl-skill-qa-risk-priority` | 1.0.0 | Verificação | Prioriza cenários por criticidade de negócio e risco técnico |
| `swl-skill-qa-diagnose-failure` | 1.0.0 | Diagnóstico | Rastreia falha de teste até a causa raiz, distinguindo bug de produto, teste mal escrito ou ambiente |
| `swl-skill-qa-report-bug` | 1.0.0 | Diagnóstico | Gera relatório de bug estruturado pronto para o sistema de gestão do projeto |
| `swl-skill-qa-exploratory-session` | 1.0.0 | Diagnóstico | Conduz e documenta uma sessão de teste exploratório estruturada |
| `swl-skill-qa-generate-test-report` | 1.0.0 | Entrega | Gera relatório executivo a partir do resultado real de execução (JSON/XML), sem inventar métricas |
| `swl-skill-qa-describe-test-pr` | 1.0.0 | Entrega | Gera descrição de PR de testes, distinguindo cenários gerados por IA de escritos manualmente |
| `swl-skill-qa-update-test-docs` | 1.0.0 | Entrega | Atualiza documentação de testes com base nas mudanças da branch atual |
| `swl-skill-qa-safe-test-commit` | 1.0.0 | Entrega | Pipeline completo (coverage, data-quality, flakiness, review) antes de commitar testes gerados por IA |

---

## Convenção de versionamento

| Incremento | Quando usar |
|---|---|
| **MAJOR** (X.0.0) | Mudança que quebra compatibilidade |
| **MINOR** (x.Y.0) | Nova seção, novo passo ou novo critério adicionado |
| **PATCH** (x.y.Z) | Correção de typo, texto ou exemplo sem mudança de comportamento |

---

## Validação desta versão

Antes da publicação 1.0.0, as 18 skills originais foram testadas funcionalmente contra cenários reais e adversariais (dado real colado propositalmente, métrica fabricada, regra de negócio ambígua, falha real de execução, gap de cobertura genuíno). Todos os guardrails resistiram — nenhuma skill inventou dado, arredondou resultado ou pulou uma etapa crítica quando pressionada.

As 4 skills adicionadas depois (mobile, contrato, performance) passaram pelo mesmo tipo de teste adversarial antes de entrar no pacote: `qa-new-mobile-automation` não inflou cobertura de dispositivo/OS além do testado; `qa-new-contract-tests` recusou gerar schema sem especificação real e gerou corretamente quando uma foi fornecida; `qa-new-performance-test` não assumiu tipo de teste nem inventou threshold de SLA; `qa-check-performance-results` reportou métricas reais extraídas de um resultado k6 sintético e recusou dar veredito de aprovação sem threshold definido. Relatório completo da auditoria disponível junto ao time que validou o pacote.

---

## Histórico de versões

### swl-skill-qa-plan-strategy
- **1.0.0** — Versão inicial conforme ao padrão Base2 (`name` prefixado, `metadata.version`). Entrevista de 5 perguntas obrigatórias com guardrail anti-invenção de resposta.

### swl-skill-qa-generate-rules
- **1.0.0** — Versão inicial conforme ao padrão Base2. Gera `padroes-teste.md`, `restricoes-teste.md` e `convencoes-teste.md`; nunca infere convenção sem fonte.

### swl-skill-qa-new-bdd-scenarios
- **1.0.0** — Versão inicial conforme ao padrão Base2. Gera `.feature` com happy path, edge case e negativo por critério; um `Quando` por ação de negócio.

### swl-skill-qa-new-test-cases
- **1.0.0** — Versão inicial conforme ao padrão Base2. Marca `[REGRA A CONFIRMAR COM PO]` quando a regra de negócio não está explícita.

### swl-skill-qa-new-test-data
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca usa dado real como base, mesmo se colado pelo usuário como exemplo.

### swl-skill-qa-new-automation
- **1.1.0** — Adiciona Robot Framework (web) e Testcontainers/WireMock/MockServer (integração) à detecção de framework; remove k6 da lista (passa a ser responsabilidade de `swl-skill-qa-new-performance-test`); passa a apontar para `swl-skill-qa-new-mobile-automation` quando o cenário for mobile.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Detecta framework via CLAUDE.md/config; marca `generated-by-ai: pending-review` até revisão humana.

### swl-skill-qa-new-mobile-automation
- **1.0.0** — Versão inicial conforme ao padrão Base2. Detecta Appium/Espresso/XCUITest/Detox/Maestro; nunca declara cobertura de dispositivo/OS além do efetivamente testado.

### swl-skill-qa-new-contract-tests
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca gera schema/contrato a partir de suposição — exige especificação real (OpenAPI, JSON Schema ou contrato Pact publicado).

### swl-skill-qa-new-performance-test
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca assume tipo de teste (smoke/load/stress/spike/soak) nem threshold de SLA sem confirmação.

### swl-skill-qa-check-performance-results
- **1.0.0** — Versão inicial conforme ao padrão Base2. Lê apenas resultado real de execução de performance; nunca aprova sem threshold definido para comparar.

### swl-skill-qa-check-coverage
- **1.0.0** — Versão inicial conforme ao padrão Base2. Não substitui execução real; não reporta "% de cobertura" como métrica de execução.

### swl-skill-qa-check-flakiness
- **1.0.0** — Versão inicial conforme ao padrão Base2. Varredura estática combinada com histórico de execução, quando disponível.

### swl-skill-qa-check-data-quality
- **1.0.0** — Versão inicial conforme ao padrão Base2. Guardrail anti-invenção: nunca completa dado faltante, apenas sinaliza.

### swl-skill-qa-review-tests
- **1.0.0** — Versão inicial conforme ao padrão Base2. Não corrige teste automaticamente; marcador `reviewed` só após validação humana real.

### swl-skill-qa-risk-priority
- **1.0.0** — Versão inicial conforme ao padrão Base2. Classificação sempre rastreável aos critérios individuais; omite histórico de bugs sem dado real.

### swl-skill-qa-diagnose-failure
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca classifica como "flaky"/"ambiente" para evitar investigar mais a fundo.

### swl-skill-qa-report-bug
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca preenche resultado esperado ou passos com suposição.

### swl-skill-qa-exploratory-session
- **1.0.0** — Versão inicial conforme ao padrão Base2. "Áreas cobertas" reflete só o que foi de fato exercitado na sessão.

### swl-skill-qa-generate-test-report
- **1.0.0** — Versão inicial conforme ao padrão Base2. Lê apenas resultado real de execução; nunca estima número faltante.

### swl-skill-qa-describe-test-pr
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca afirma "revisado" sem o marcador `generated-by-ai: reviewed` presente no arquivo.

### swl-skill-qa-update-test-docs
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca remove documentação de cenário ainda ativo na suíte.

### swl-skill-qa-safe-test-commit
- **1.0.0** — Versão inicial conforme ao padrão Base2. Referências às demais skills do pipeline usam nome completo prefixado. Bloqueia o commit em caso de problema crítico em qualquer etapa.
