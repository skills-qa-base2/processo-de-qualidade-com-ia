---
name: swl-skill-qa-new-bdd-scenarios
description: Gera cenários BDD em Gherkin (Dado/Quando/Então) a partir de critérios de aceite, prontos para uso por Cucumber, SpecFlow, Behave ou equivalente.
argument-hint: <NomeDaFeature>
metadata:
  version: 1.1.0
  validated: false
---

## Passos

## 1. Leitura dos critérios de aceite
Leia a User Story e critérios de aceite. Se não houver critérios claros, pergunte ao usuário — cenário BDD mal fundamentado gera automação inútil.

## 2. Geração do arquivo Feature
Gere um arquivo `.feature` com:
```gherkin
Funcionalidade: <nome da funcionalidade>
  Como <papel>
  Quero <ação>
  Para <benefício>

  Cenário: <happy path>
    Dado que <pré-condição>
    Quando <ação do usuário>
    Então <resultado esperado>

  Cenário: <edge case ou negativo>
    ...
```

## 3. Derivação dos cenários
Derive os `Exemplos` do `Esquema do Cenário` das classes de equivalência e dos limites da regra — três valores por fronteira (abaixo, na fronteira, acima) —, com a técnica identificável em cada linha.

Leve para o `.feature` apenas os cenários críticos do fluxo. Classes e limites de menor risco ficam nos casos de teste (`swl-skill-qa-new-test-cases`) e não viram E2E: cenário de borda ou negativo existe quando o risco justifica, nunca para cumprir número.

## 4. Saída
Salve em `features/<nome-da-feature>.feature` (ou caminho definido no CLAUDE.md/rules do projeto).

## Guardrail
Nunca combine múltiplas ações de negócio distintas em um único `Quando`. Um cenário deve testar uma coisa; se o critério de aceite descreve mais de uma regra, gere cenários separados.

Nunca preencha uma linha de `Exemplos` com valor de fronteira que a regra não declara — marque `[LIMITE A CONFIRMAR COM PO]` em vez de escolher um número plausível.
