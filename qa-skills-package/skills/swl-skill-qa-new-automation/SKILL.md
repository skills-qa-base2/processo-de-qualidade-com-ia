---
name: swl-skill-qa-new-automation
description: Gera código de automação de teste detectando o framework do projeto (Playwright, Cypress, Selenium, Robot Framework, RestAssured, Postman/Newman, Testcontainers, WireMock/MockServer, Cucumber, SpecFlow) a partir do CLAUDE.md e rules. Para mobile use swl-skill-qa-new-mobile-automation; para performance/carga use swl-skill-qa-new-performance-test.
argument-hint: <NomeDoCenárioOuArquivoFeature>
metadata:
  version: 1.1.0
---

## Passos

## 1. Detecção do framework
Leia o CLAUDE.md e os arquivos de configuração do projeto (`package.json`, `.csproj`, `pom.xml`, `requirements.txt`, arquivos `.robot`/`robot.yaml`, `docker-compose.yml` com serviços de teste) para identificar o framework de automação já em uso — web/E2E (Playwright, Cypress, Selenium, Robot Framework), API (RestAssured, Postman/Newman), integração/service virtualization (Testcontainers, WireMock, MockServer) ou glue BDD (Cucumber, SpecFlow). Nunca introduza um framework novo sem confirmação explícita do usuário.

Se o cenário for de automação **mobile**, use `swl-skill-qa-new-mobile-automation` em vez desta skill. Se for **teste de carga/performance**, use `swl-skill-qa-new-performance-test`.

## 2. Origem do cenário
Use como fonte um cenário BDD (`swl-skill-qa-new-bdd-scenarios`) ou caso de teste (`swl-skill-qa-new-test-cases`) já existente. Se nenhum for fornecido, pergunte qual cenário automatizar.

## 3. Geração do código
Gere o teste seguindo os padrões já existentes no projeto:
- Reutilize Page Objects / componentes de API já existentes; não duplique
- Use seletores estáveis (`data-testid`, atributos semânticos) — nunca seletores frágeis (XPath posicional, classes CSS de estilo)
- Waits explícitos condicionados a estado da aplicação — nunca `sleep`/espera fixa
- Dados de teste via massa gerada por `swl-skill-qa-new-test-data`, nunca hardcoded inline repetido

## 4. Registro no pipeline
Adicione o teste à suíte/CI conforme convenção do projeto (tag, grupo, pasta).

## Guardrail
Todo teste gerado deve ser marcado com o comentário `// generated-by-ai: reviewed` (ou equivalente na linguagem) **somente após** revisão humana. Testes sem esse comentário não devem ser aceitos em PR — não adicione o comentário antes da revisão real acontecer.
