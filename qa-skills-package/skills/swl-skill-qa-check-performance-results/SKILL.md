---
name: swl-skill-qa-check-performance-results
description: Analisa o resultado real de uma execução de teste de performance (k6, JMeter, Gatling) e reporta métricas contra os thresholds definidos, sem inventar números.
argument-hint: <caminho-do-arquivo-de-resultado>
metadata:
  version: 1.0.0
---

## Passos

## 1. Leitura do resultado real
Leia o arquivo de saída real da execução (k6 summary JSON, JMeter `.jtl`/CSV, Gatling simulation log). Nunca gere o relatório a partir de estimativa ou memória de execuções anteriores.

## 2. Extração de métricas
Extraia apenas o que está no arquivo: latência (p50/p95/p99), taxa de erro, throughput (RPS), duração total, número de usuários virtuais.

## 3. Comparação com thresholds
Se os thresholds da estratégia (definidos via `swl-skill-qa-new-performance-test`) estiverem disponíveis, compare e sinalize violação. Se não estiverem disponíveis, apresente as métricas brutas e avise explicitamente que não há threshold definido para julgar aprovação/reprovação.

## 4. Geração do resumo
```
Tipo de teste: <smoke/load/stress/spike/soak, se conhecido>
Duração: <duração real>
Usuários virtuais: <N>
Latência p95: <valor> | Threshold: <valor ou "não definido">
Latência p99: <valor> | Threshold: <valor ou "não definido">
Taxa de erro: <valor> | Threshold: <valor ou "não definido">
Throughput: <RPS>

Veredito: DENTRO DO THRESHOLD / VIOLOU THRESHOLD / SEM THRESHOLD DEFINIDO PARA COMPARAR
```

## Guardrail
Se o arquivo de resultado não puder ser lido ou estiver incompleto, diga isso claramente e não preencha as métricas faltantes com estimativa. Nunca aprove um teste de carga como "dentro do esperado" sem um threshold real contra o qual comparar.
