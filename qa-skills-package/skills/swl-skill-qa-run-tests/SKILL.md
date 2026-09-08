---
name: swl-skill-qa-run-tests
description: Executa a suíte de testes do projeto detectando o runner automaticamente, captura o arquivo de resultado e reporta o que passou e o que falhou. Use sempre que precisar do resultado real de execução — antes de commitar testes, ao investigar falha, ou como insumo de relatório.
argument-hint: [caminho, tag ou filtro — vazio executa a suíte configurada]
metadata:
  version: 1.0.0
  validated: false
---

## Passos

## 1. Detecção do runner
Se `.claude/rules/qa/convencoes-teste.md` registra o comando de execução do projeto, use exatamente esse comando. Senão detecte pelos arquivos: `package.json` (script `test`/`test:e2e`, Playwright, Cypress, Jest, Vitest), `.csproj`/`.sln` (`dotnet test`), `pom.xml`/`build.gradle` (`mvn test`/`gradle test`), `pytest.ini`/`pyproject.toml` (`pytest`), robotframework (`robot`). Se mais de um runner for plausível, pergunte qual — não escolha por conta própria.

## 2. Pré-condições e alvo
Confirme o que a suíte precisa (serviços no ar, variáveis de ambiente, seed de dados, aplicação servida) e contra qual ambiente vai rodar. Se algo faltar, diga o que falta e pare: suíte que quebra por ambiente não produz resultado de teste. Para a checagem completa use `swl-skill-qa-check-environment`. Nunca execute contra produção sem autorização explícita.

## 3. Execução com resultado persistido
Rode sempre com a flag de relatório de máquina, para o resultado ficar em arquivo e não só no terminal: Playwright `--reporter=json`, Jest/Vitest `--outputFile`, dotnet `--logger trx`, Maven/Gradle (Surefire/JUnit XML), pytest `--junitxml`, Robot `--xunit`. Salve em `test-results/` ou no caminho de convenção do projeto e informe o caminho gerado.

## 4. Relato
Reporte: comando exato executado, ambiente, escopo, passou/falhou/pulado/retried, duração, caminho do arquivo de resultado e a primeira linha do erro de cada falha. Se o usuário passou filtro, diga explicitamente que a execução foi parcial — nunca apresente execução parcial como se fosse a suíte inteira. Encaminhe as falhas para `swl-skill-qa-diagnose-failure` e o arquivo para `swl-skill-qa-generate-test-report`.

## Guardrail
Nunca reporte resultado que não veio de uma execução real nesta sessão. Se o comando não rodou, travou, estourou timeout ou o ambiente não subiu, diga exatamente isso em vez de preencher o resumo com números plausíveis. Nunca altere teste, assert ou configuração para fazer a suíte passar: se falhou, o resultado é "falhou", e corrigir é uma decisão separada tomada depois do diagnóstico. Teste pulado não é teste que passou, e retry que passou na segunda tentativa é sinal de flakiness que deve aparecer no relato, não ser absorvido no total de sucessos.
