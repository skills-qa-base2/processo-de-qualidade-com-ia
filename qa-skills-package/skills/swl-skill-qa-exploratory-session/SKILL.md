---
name: swl-skill-qa-exploratory-session
description: Conduz e documenta uma sessão de teste exploratório estruturada (session-based test management) — charter, tempo, notas e bugs encontrados.
argument-hint: <ÁreaOuFuncionalidadeAExplorar>
metadata:
  version: 1.0.0
---

## Passos

## 1. Definição do charter
Antes de iniciar, defina com o usuário:
- **Missão**: o que será explorado e por quê
- **Escopo**: o que está dentro e fora da sessão
- **Tempo-caixa**: duração da sessão (ex: 60-90 min)

## 2. Condução da sessão
Durante a sessão, registre em tempo real:
- Ações realizadas
- Observações e comportamentos inesperados
- Dúvidas que surgiram sobre regra de negócio
- Bugs encontrados (encaminhar para `swl-skill-qa-report-bug`)

## 3. Relatório da sessão
Ao final, gere:
```
Charter: <missão e escopo>
Duração: <tempo real gasto>
Áreas cobertas: <lista>
Bugs encontrados: <lista com severidade>
Dúvidas em aberto: <lista para levar ao PO/dev>
Cobertura percebida: <o que ainda não foi explorado por falta de tempo>
```

## Guardrail
Teste exploratório documenta o que foi de fato observado durante a sessão — nunca preencha "áreas cobertas" com funcionalidades que não foram realmente exercitadas na sessão registrada.
