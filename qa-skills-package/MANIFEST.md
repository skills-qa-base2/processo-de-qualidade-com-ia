# Base2 Skills de QA — Manifest

Skills de QA da Base2 Tecnologia para Claude Code. Cobrem frontend/web, API, integração, contrato, mobile e performance — funcionam em qualquer projeto, independente de stack ou framework de automação.

## Skills disponíveis

| Skill | Versão | Categoria | Descrição |
|---|---|---|---|
| `swl-skill-qa-plan-strategy` | 1.0.0 | Planejamento | Entrevista estruturada para levantar a estratégia de testes de um projeto ou feature antes de gerar qualquer cenário |
| `swl-skill-qa-generate-rules` | 1.0.0 | Planejamento | Gera `.claude/rules/qa/` a partir de documentação técnica existente ou entrevista com o time |
| `swl-skill-qa-review-requirements` | 1.0.0 | Planejamento | Revisa user story no refinamento: testabilidade, critérios de aceite verificáveis e lacunas de regra |
| `swl-skill-qa-new-bdd-scenarios` | 1.0.0 | Geração | Gera cenários BDD em Gherkin a partir de critérios de aceite |
| `swl-skill-qa-new-test-cases` | 1.0.1 | Geração | Gera casos de teste estruturados a partir de user story, cobrindo happy path, edge cases e negativos |
| `swl-skill-qa-new-test-data` | 1.0.0 | Geração | Gera massa de dados de teste fictícia via factories/fixtures |
| `swl-skill-qa-new-automation` | 1.2.0 | Geração | Gera código de automação web/API/integração detectando o framework do projeto (Playwright, Cypress, Selenium, Robot Framework, RestAssured, Postman/Newman, Testcontainers, WireMock/MockServer, Cucumber, SpecFlow) |
| `swl-skill-qa-new-mobile-automation` | 1.1.0 | Geração | Gera código de automação mobile detectando o framework do projeto (Appium, Espresso, XCUITest, Detox, Maestro) |
| `swl-skill-qa-new-contract-tests` | 1.0.1 | Geração | Gera testes de contrato/schema de API (OpenAPI/JSON Schema, Pact/Spring Cloud Contract) a partir de especificação real |
| `swl-skill-qa-new-performance-test` | 1.0.1 | Geração | Gera scripts de teste de performance (smoke/load/stress/spike/soak) detectando a ferramenta do projeto (k6, JMeter, Gatling, Artillery) |
| `swl-skill-qa-check-performance-results` | 1.0.0 | Verificação | Analisa resultado real de execução de teste de performance contra thresholds definidos |
| `swl-skill-qa-check-coverage` | 1.1.0 | Verificação | Analisa gaps de cobertura de cenários frente a requisitos e critérios de aceite |
| `swl-skill-qa-check-flakiness` | 1.0.0 | Verificação | Detecta padrões de instabilidade em testes automatizados |
| `swl-skill-qa-check-data-quality` | 1.0.0 | Verificação | Audita documentos/relatórios de QA gerados por IA em busca de dados fabricados |
| `swl-skill-qa-review-tests` | 1.1.0 | Verificação | Revisa testes quanto a nomenclatura, clareza de asserts e cobertura real; única skill que promove o marcador `generated-by-ai` para `reviewed` |
| `swl-skill-qa-risk-priority` | 1.0.0 | Verificação | Prioriza cenários por criticidade de negócio e risco técnico |
| `swl-skill-qa-check-security` | 1.0.1 | Verificação | Verificação de segurança stack-agnóstica (Node, Python, Java, mobile) — complementa, não duplica, a `swl-skill-check-security` do org-skills (.NET Web API) |
| `swl-skill-qa-check-accessibility` | 1.0.1 | Verificação | Audita acessibilidade (WCAG) via ferramenta já presente no projeto (axe-core, pa11y, Lighthouse) |
| `swl-skill-qa-check-environment` | 1.0.1 | Verificação | Valida que um ambiente está pronto para rodar a suíte (health check, seed de dados, feature flags) |
| `swl-skill-qa-run-tests` | 1.0.0 | Verificação | Executa a suíte detectando o runner do projeto e captura o arquivo real de resultado |
| `swl-skill-qa-check-ci-history` | 1.0.0 | Verificação | Identifica flakiness por evidência do histórico do CI, separando teste flaky de teste cronicamente quebrado |
| `swl-skill-qa-select-regression-suite` | 1.0.0 | Verificação | Seleciona o recorte de regressão de uma release cruzando diff de código com matriz de risco |
| `swl-skill-qa-diagnose-failure` | 1.0.0 | Diagnóstico | Rastreia falha de teste até a causa raiz, distinguindo bug de produto, teste mal escrito ou ambiente |
| `swl-skill-qa-report-bug` | 1.0.0 | Diagnóstico | Gera relatório de bug estruturado pronto para o sistema de gestão do projeto |
| `swl-skill-qa-exploratory-session` | 1.0.0 | Diagnóstico | Conduz e documenta uma sessão de teste exploratório estruturada |
| `swl-skill-qa-generate-test-report` | 1.0.0 | Entrega | Gera relatório executivo a partir do resultado real de execução (JSON/XML), sem inventar métricas |
| `swl-skill-qa-describe-test-pr` | 1.1.0 | Entrega | Gera descrição de PR de testes, distinguindo cenários gerados por IA de escritos manualmente |
| `swl-skill-qa-update-test-docs` | 1.1.0 | Entrega | Atualiza documentação de testes com base nas mudanças da branch atual |
| `swl-skill-qa-safe-test-commit` | 1.1.0 | Entrega | Pipeline completo (execução da suíte, coverage, data-quality, flakiness, review) antes de commitar testes gerados por IA |
| `swl-skill-qa-release-signoff` | 1.0.0 | Entrega | Consolida as evidências reais de uma release num parecer go/no-go rastreável |

### swl-skill-qa-release-signoff
- **1.0.0** — Versão inicial. Consolida execução, cobertura, bugs abertos e não-funcionais numa tabela de evidências com fonte e data de cada item. Evidência faltando resulta em EVIDÊNCIA INSUFICIENTE, nunca em LIBERAR; ausência de bug reportado não é tratada como evidência de qualidade.

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

**Nota sobre as 5 skills adicionadas nesta rodada**: `qa-review-requirements`, `qa-run-tests`, `qa-check-ci-history`, `qa-select-regression-suite` e `qa-release-signoff` seguem o mesmo formato e a mesma convenção de guardrail anti-invenção das demais, mas **ainda não passaram pelo teste adversarial** — estão com `validated: false`. Tratar como pendentes de validação.

**Nota sobre as 7 skills alteradas em 1.1.0/1.2.0**: `qa-new-automation`, `qa-new-mobile-automation`, `qa-review-tests`, `qa-safe-test-commit`, `qa-describe-test-pr`, `qa-update-test-docs` e `qa-check-coverage` tiveram frases do `## Guardrail` reescritas nesta rodada. Seguindo a regra registrada em `EFICIENCIA-TOKENS.md`, todas foram marcadas com `validated: false` e precisam passar de novo pelo teste adversarial antes de voltarem ao mesmo nível de confiança das demais.

**Nota sobre `qa-check-security`, `qa-check-accessibility` e `qa-check-environment`**: essas 3 skills seguem o mesmo formato e a mesma convenção de guardrail anti-invenção das demais, mas **ainda não passaram pelo teste adversarial** aplicado às skills anteriores (ver `AUDITORIA-COBERTURA.md`, Parte 3). Tratar como pendente de validação antes de considerar o mesmo nível de confiança das outras 22.

---

## Histórico de versões

### swl-skill-qa-plan-strategy
- **1.0.0** — Versão inicial conforme ao padrão Base2 (`name` prefixado, `metadata.version`). Entrevista de 5 perguntas obrigatórias com guardrail anti-invenção de resposta.

### swl-skill-qa-generate-rules
- **1.0.0** — Versão inicial conforme ao padrão Base2. Gera `padroes-teste.md`, `restricoes-teste.md` e `convencoes-teste.md`; nunca infere convenção sem fonte.

### swl-skill-qa-new-bdd-scenarios
- **1.0.0** — Versão inicial conforme ao padrão Base2. Gera `.feature` com happy path, edge case e negativo por critério; um `Quando` por ação de negócio.

### swl-skill-qa-new-test-cases
- **1.0.1** — Reduz verbosidade (217 → 206 palavras, -5,1%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Marca `[REGRA A CONFIRMAR COM PO]` quando a regra de negócio não está explícita.

### swl-skill-qa-new-test-data
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca usa dado real como base, mesmo se colado pelo usuário como exemplo.

### swl-skill-qa-new-automation
- **1.2.0** — Corrige o marcador de rastreabilidade: o teste passa a nascer com `generated-by-ai: pending-review`, e a promoção para `reviewed` passa a ser atribuição exclusiva de `swl-skill-qa-review-tests`. A redação anterior ("marcado com `reviewed` **somente após** revisão humana") deixava o teste sem marcador nenhum no momento da geração, o que quebrava a detecção de `swl-skill-qa-describe-test-pr` e divergia do comportamento já documentado neste manifest na entrada 1.0.0.
- **1.1.0** — Adiciona Robot Framework (web) e Testcontainers/WireMock/MockServer (integração) à detecção de framework; remove k6 da lista (passa a ser responsabilidade de `swl-skill-qa-new-performance-test`); passa a apontar para `swl-skill-qa-new-mobile-automation` quando o cenário for mobile.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Detecta framework via CLAUDE.md/config; marca `generated-by-ai: pending-review` até revisão humana.

### swl-skill-qa-new-mobile-automation
- **1.1.0** — Corrige contradição no guardrail: dizia marcar `generated-by-ai: pending-review` "**somente após** revisão humana", o que é logicamente impossível — `pending-review` é o estado anterior à revisão. Alinhado com `swl-skill-qa-new-automation` (duplicação intencional dos 4 trechos, conforme `AGENTS.md`).
- **1.0.1** — Reduz verbosidade (317 → 298 palavras, -6,0%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Detecta Appium/Espresso/XCUITest/Detox/Maestro; nunca declara cobertura de dispositivo/OS além do efetivamente testado.

### swl-skill-qa-new-contract-tests
- **1.0.1** — Reduz verbosidade (279 → 264 palavras, -5,4%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca gera schema/contrato a partir de suposição — exige especificação real (OpenAPI, JSON Schema ou contrato Pact publicado).

### swl-skill-qa-new-performance-test
- **1.0.1** — Reduz verbosidade (294 → 278 palavras, -5,4%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca assume tipo de teste (smoke/load/stress/spike/soak) nem threshold de SLA sem confirmação.

### swl-skill-qa-check-performance-results
- **1.0.0** — Versão inicial conforme ao padrão Base2. Lê apenas resultado real de execução de performance; nunca aprova sem threshold definido para comparar.

### swl-skill-qa-check-coverage
- **1.1.0** — Passa a dizer onde procurar as duas fontes e a perguntar quando uma delas não é localizada, em vez de seguir com uma só. Impede o modo de falha em que os critérios de aceite são deduzidos dos próprios testes existentes, o que torna a auditoria circular e sempre conclui "tudo coberto".
- **1.0.0** — Versão inicial conforme ao padrão Base2. Não substitui execução real; não reporta "% de cobertura" como métrica de execução.

### swl-skill-qa-check-flakiness
- **1.0.0** — Versão inicial conforme ao padrão Base2. Varredura estática combinada com histórico de execução, quando disponível.

### swl-skill-qa-check-data-quality
- **1.0.0** — Versão inicial conforme ao padrão Base2. Guardrail anti-invenção: nunca completa dado faltante, apenas sinaliza.

### swl-skill-qa-review-tests
- **1.1.0** — Passa a ser a única skill do pacote autorizada a promover `generated-by-ai: pending-review` para `reviewed`, com três condições explícitas (observações apresentadas, confirmação humana explícita, teste executado com sucesso). Antes, nenhuma skill era dona dessa transição: as geradoras diziam que ela devia acontecer e esta dizia que não editava o teste.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Não corrige teste automaticamente; marcador `reviewed` só após validação humana real.

### swl-skill-qa-review-requirements
- **1.0.0** — Versão inicial. Cobre a lacuna de QA no refinamento: testa a verificabilidade de cada critério de aceite, levanta as lacunas clássicas (permissão, estado, limites, concorrência, falha de dependência, retroatividade, não-funcionais, observabilidade) e nunca responde por conta própria uma pergunta destinada ao PO.

### swl-skill-qa-run-tests
- **1.0.0** — Versão inicial. Fecha o ciclo entre geração e relatório: nenhuma skill do pacote executava a suíte, então `qa-generate-test-report` dependia de um arquivo que ninguém produzia e `qa-safe-test-commit` commitava teste nunca executado. Nunca reporta resultado que não veio de execução real, e nunca altera teste ou configuração para a suíte passar.

### swl-skill-qa-check-ci-history
- **1.0.0** — Versão inicial. Fornece a evidência de execução que o guardrail de `qa-check-flakiness` já exigia e que nada no pacote produzia. Distingue flaky confirmado (passa e falha na mesma revisão) de teste cronicamente quebrado, para que retry não seja ligado sobre regressão real.

### swl-skill-qa-select-regression-suite
- **1.0.0** — Versão inicial. Recorte de regressão por diff mais matriz de risco, com seção explícita de riscos aceitos. Nunca marca uma área como dispensável só porque nenhum arquivo dela mudou — dependência compartilhada, configuração e migration quebram justamente as áreas que ninguém tocou.

### swl-skill-qa-risk-priority
- **1.0.0** — Versão inicial conforme ao padrão Base2. Classificação sempre rastreável aos critérios individuais; omite histórico de bugs sem dado real.

### swl-skill-qa-check-security
- **1.0.1** — Reduz verbosidade (389 → 359 palavras, -7,7%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial. Verificação de segurança stack-agnóstica (fora de .NET Web API); guardrail exige evidência real de execução (request/response observado) para qualquer achado, nunca "aprovado" por ausência de teste. Pendente de teste adversarial (ver nota em "Validação desta versão").

### swl-skill-qa-check-accessibility
- **1.0.1** — Reduz verbosidade (300 → 288 palavras, -4,0%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial. Audita WCAG via ferramenta já presente no projeto; guardrail nunca declara conformidade além das telas efetivamente auditadas. Pendente de teste adversarial.

### swl-skill-qa-check-environment
- **1.0.1** — Reduz verbosidade (355 → 344 palavras, -3,1%) sem mudança de comportamento, conforme `EFICIENCIA-TOKENS.md`.
- **1.0.0** — Versão inicial. Valida ambiente antes da execução (health check, seed, feature flags); guardrail nunca presume "ambiente pronto" sem checar de fato. Pendente de teste adversarial.

### swl-skill-qa-diagnose-failure
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca classifica como "flaky"/"ambiente" para evitar investigar mais a fundo.

### swl-skill-qa-report-bug
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca preenche resultado esperado ou passos com suposição.

### swl-skill-qa-exploratory-session
- **1.0.0** — Versão inicial conforme ao padrão Base2. "Áreas cobertas" reflete só o que foi de fato exercitado na sessão.

### swl-skill-qa-generate-test-report
- **1.0.0** — Versão inicial conforme ao padrão Base2. Lê apenas resultado real de execução; nunca estima número faltante.

### swl-skill-qa-describe-test-pr
- **1.1.0** — Passa a resolver a branch base de fato (PR → upstream → `origin/HEAD` → perguntar) em vez de comparar com "a base" indefinida, e a identificar teste gerado por IA pelo marcador no arquivo em vez da tag do commit, que some quando o commit não passa por `swl-skill-qa-safe-test-commit`. Separa `reviewed` de `pending-review` na descrição.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca afirma "revisado" sem o marcador `generated-by-ai: reviewed` presente no arquivo.

### swl-skill-qa-update-test-docs
- **1.1.0** — Passa a resolver a branch base de fato (PR → upstream → `origin/HEAD` → perguntar) em vez de comparar com "a base" indefinida.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Nunca remove documentação de cenário ainda ativo na suíte.

### swl-skill-qa-safe-test-commit
- **1.1.0** — Adiciona a execução da suíte como primeira etapa do pipeline: a versão anterior commitava e dava push em teste que nunca foi executado. Commit e push passam a exigir confirmação separada, e o commit na branch base é bloqueado. Resolve a contradição do guardrail ("nunca pule" seguido de "se pular, registre") definindo que pular exige decisão explícita do usuário registrada como `Skipped-check:`. Define a origem de `Reviewed-by:`.
- **1.0.0** — Versão inicial conforme ao padrão Base2. Referências às demais skills do pipeline usam nome completo prefixado. Bloqueia o commit em caso de problema crítico em qualquer etapa.
