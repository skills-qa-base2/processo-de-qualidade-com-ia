---
name: swl-skill-qa-new-test-cases
description: Gera casos de teste estruturados a partir de uma user story, card ou requisito, cobrindo happy path, edge cases e cenários negativos.
argument-hint: <UserStoryOuDescriçãoDoRequisito>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Leitura do requisito
Leia a descrição fornecida e os critérios de aceite. Se estiverem incompletos ou ambíguos, pergunte ao usuário antes de gerar os casos — nunca preencha lacunas de regra de negócio por conta própria.

## 2. Identificação de pré-condições
Liste o estado inicial necessário (dados cadastrados, permissões, ambiente) para cada fluxo.

## 3. Geração dos casos
Gere casos cobrindo:
- **Happy path**: fluxo principal com dados válidos
- **Edge cases**: limites de campo, valores extremos, formatos-limite
- **Cenários negativos**: dados inválidos, permissão negada, recurso inexistente, falha de serviço externo

Formato de cada caso:
```
Título: <objetivo do teste em verbo no infinitivo>
Pré-condição: <estado inicial>
Passos: <ações numeradas>
Resultado esperado: <o que deve acontecer>
Prioridade: <Crítico/Alto/Médio/Baixo — usar swl-skill-qa-risk-priority se disponível>
```

## 4. Saída
Salve no formato de gestão de teste do projeto (ferramenta configurada em CLAUDE.md, planilha ou markdown em `docs/qa/casos-de-teste/`).

## Guardrail
Nunca gere um caso de teste com resultado esperado inventado quando a regra de negócio não foi explicitada — marque como `[REGRA A CONFIRMAR COM PO]` em vez de assumir um comportamento.
