---
name: swl-skill-qa-check-coverage
description: Analisa gaps de cobertura de cenários frente aos requisitos e critérios de aceite — cobertura funcional, não cobertura de código.
argument-hint: <NomeDaFeatureOuMódulo>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Levantamento das duas fontes
Reúna: (a) os critérios de aceite / requisitos da feature, e (b) os casos de teste ou cenários BDD já existentes para ela.

## 2. Cruzamento
Para cada critério de aceite, verifique se existe ao menos um cenário de happy path, um edge case relevante e um cenário negativo cobrindo-o.

## 3. Relato de gaps
Liste, sem arredondar para "está tudo coberto":
- Critérios sem nenhum cenário
- Critérios só com happy path (faltando negativo/edge)
- Cenários existentes que não correspondem a nenhum critério atual (possível teste órfão)

## 4. Saída
Relatório objetivo com uma linha por gap encontrado, sem inflar números. Se a cobertura estiver completa, diga isso claramente — não invente gaps para parecer útil.

## Guardrail
Esta skill audita cenários **e não substitui execução real**: cobertura completa de cenários não significa que os testes foram executados com sucesso. Nunca reporte "cobertura de X%" como métrica de execução — isso é papel do `swl-skill-qa-generate-test-report`.
