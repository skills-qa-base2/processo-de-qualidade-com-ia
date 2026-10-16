---
name: swl-skill-qa-new-test-cases
description: Gera casos de teste estruturados a partir de uma user story, card ou requisito, aplicando técnicas de especificação (partição de equivalência, valor limite, tabela de decisão, transição de estados) e registrando a técnica que originou cada caso.
argument-hint: <UserStoryOuDescriçãoDoRequisito>
metadata:
  version: 1.1.0
  validated: true
---

## Passos

## 1. Leitura do requisito
Leia a descrição fornecida e os critérios de aceite. Se estiverem incompletos ou ambíguos, pergunte ao usuário antes de gerar os casos.

## 2. Identificação de pré-condições
Liste o estado inicial necessário (dados cadastrados, permissões, ambiente) para cada fluxo.

## 3. Seleção da técnica
Para cada regra do requisito, aplique só a técnica que couber:
- **Partição de equivalência** — faixas ou categorias de valor: um caso por classe válida e por inválida, não um por valor
- **Valor limite** — limite numérico, de tamanho ou de data: três valores por fronteira (abaixo, na fronteira, acima)
- **Tabela de decisão** — resultado que depende de duas ou mais condições combinadas: uma linha por combinação relevante
- **Transição de estados** — recurso que muda de estado: cada transição válida e as inválidas que a regra proíbe

Regra sem nenhuma dessas características gera caso direto — não force técnica.

## 4. Geração dos casos
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
Técnica: <técnica aplicada e o que ela originou — ex: valor limite, fronteira inferior de 18 anos>
```

## 5. Saída
Salve no formato de gestão de teste do projeto (ferramenta configurada em CLAUDE.md, planilha ou markdown em `docs/qa/casos-de-teste/`).

## Guardrail
Nunca gere um caso de teste com resultado esperado inventado quando a regra de negócio não foi explicitada — marque como `[REGRA A CONFIRMAR COM PO]` em vez de assumir um comportamento.

Nunca derive valor limite sem o limite estar explícito na regra: marque `[LIMITE A CONFIRMAR COM PO]`. Nunca invente classe de equivalência, condição de tabela de decisão ou estado e transição que o requisito não descreve — o que faltar vira pergunta, não suposição. Nunca declare uma técnica "aplicada por completo" quando a regra de origem está incompleta: diga qual parte ficou de fora e por quê.
