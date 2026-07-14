---
name: swl-skill-qa-new-bdd-scenarios
description: Gera cenários BDD em Gherkin (Dado/Quando/Então) a partir de critérios de aceite, prontos para uso por Cucumber, SpecFlow, Behave ou equivalente.
argument-hint: <NomeDaFeature>
metadata:
  version: 1.0.0
  validated: true
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

## 3. Cobertura obrigatória
Gerar no mínimo: 1 cenário de happy path, 1 edge case, 1 cenário negativo por critério de aceite relevante. Usar `Esquema do Cenário` (Scenario Outline) com `Exemplos` quando houver variação de dados de entrada.

## 4. Saída
Salve em `features/<nome-da-feature>.feature` (ou caminho definido no CLAUDE.md/rules do projeto).

## Guardrail
Nunca combine múltiplas ações de negócio distintas em um único `Quando`. Um cenário deve testar uma coisa; se o critério de aceite descreve mais de uma regra, gere cenários separados.
