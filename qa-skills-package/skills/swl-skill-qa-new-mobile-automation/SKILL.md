---
name: swl-skill-qa-new-mobile-automation
description: Gera código de automação de teste mobile detectando o framework do projeto (Appium, Espresso, XCUITest, Detox, Maestro) a partir do CLAUDE.md e rules — cobre concerns específicas de mobile (matriz de dispositivo/OS, permissões, conectividade).
argument-hint: <NomeDoCenárioOuTelaAAutomatizar>
metadata:
  version: 1.0.1
  validated: true
---

## Passos

## 1. Detecção do framework
Leia o CLAUDE.md e os arquivos de configuração do projeto (`appium.config.*`, `wdio.conf.js`, `build.gradle` com dependência de Espresso, `Podfile`/target de XCTest, `.detoxrc.*`, `.maestro/*.yaml`) para identificar o framework mobile já em uso. Nunca introduza um framework novo sem confirmação explícita do usuário.

## 2. Origem do cenário
Use como fonte um cenário BDD (`swl-skill-qa-new-bdd-scenarios`) ou caso de teste (`swl-skill-qa-new-test-cases`) já existente. Se nenhum for fornecido, pergunte qual tela/fluxo automatizar.

## 3. Geração do código
Gere o teste seguindo os padrões já existentes no projeto:
- Reutilize Screen Objects/componentes já existentes; não duplique
- Use seletores estáveis (accessibility id, `resource-id`, `testID`) — nunca índice de posição de elemento nem coordenadas de tela
- Waits explícitos condicionados a estado do elemento/app — nunca `sleep`/espera fixa
- Trate estados específicos de mobile quando relevantes ao cenário: diálogo de permissão do SO, app indo para background/foreground, conectividade (offline/modo avião)
- Dados de teste via massa gerada por `swl-skill-qa-new-test-data`, nunca hardcoded inline repetido

## 4. Matriz de dispositivo/OS
Declare explicitamente em qual dispositivo/emulador e versão de OS o teste foi gerado/executado.

## 5. Registro no pipeline
Adicione o teste à suíte/CI conforme convenção do projeto (tag, grupo, pasta).

## Guardrail
Nunca afirme que um cenário foi validado em um dispositivo ou versão de OS sem execução real registrada — fragmentação de dispositivo é a causa mais comum de falso-positivo em QA mobile. Todo teste gerado deve ser marcado com o comentário `// generated-by-ai: pending-review` (ou equivalente na linguagem) **somente após** revisão humana.
