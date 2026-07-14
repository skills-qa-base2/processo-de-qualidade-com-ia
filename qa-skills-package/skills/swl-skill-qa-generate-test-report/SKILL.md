---
name: swl-skill-qa-generate-test-report
description: Gera relatório executivo de execução de testes a partir do resultado real de execução (JSON/XML do test runner), sem inventar métricas.
argument-hint: <caminho-do-arquivo-de-resultado>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Leitura do resultado real
Leia o arquivo de resultado de execução (JUnit XML, JSON do Playwright/Cypress, relatório do Xray, etc.). Nunca gere o relatório a partir de estimativa ou memória de execuções anteriores.

## 2. Extração de métricas
Extraia apenas o que está no arquivo: total executado, passou, falhou, pulado, tempo de execução, cenários com falha e sua mensagem de erro.

## 3. Geração do resumo
```
Total de cenários executados: <N>
Sucesso: <N> (<%>)
Falha: <N> (<%>)
Pulado: <N>
Tempo total: <duração>

Falhas encontradas:
- <cenário>: <mensagem de erro resumida> — Bug: <link, se já reportado>
```

## 4. Contextualização
Compare com a execução anterior apenas se o arquivo correspondente também for fornecido — nunca infira tendência sem os dois pontos de dados.

## Guardrail
Se o arquivo de resultado não puder ser lido ou estiver incompleto, diga isso claramente e não preencha os números faltantes com estimativa. Um relatório de execução existe para ser confiável.
