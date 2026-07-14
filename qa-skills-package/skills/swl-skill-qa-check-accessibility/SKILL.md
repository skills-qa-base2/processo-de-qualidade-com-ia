---
name: swl-skill-qa-check-accessibility
description: Audita acessibilidade (WCAG) de telas/fluxos usando a ferramenta já presente no projeto (axe-core, pa11y, Lighthouse ou equivalente) — nunca declara conformidade com um nível WCAG sem execução real da ferramenta.
argument-hint: <URL, tela ou componente a auditar>
metadata:
  version: 1.0.1
  validated: false
---

## Passos

## 1. Detecção da ferramenta
Leia o CLAUDE.md e os arquivos de configuração do projeto (`package.json` com `axe-core`/`@axe-core/playwright`/`pa11y`, config de Lighthouse CI) para identificar a ferramenta de auditoria de acessibilidade já em uso. Nunca introduza uma ferramenta nova sem confirmação explícita do usuário.

## 2. Definição do escopo
Esclareça com o usuário: qual nível WCAG é o alvo (A, AA ou AAA — não assuma AA por padrão sem confirmar) e quais telas/fluxos serão auditados.

## 3. Execução da auditoria
Rode a ferramenta detectada contra a(s) tela(s)/fluxo(s) definidos no passo 2. Registre exatamente quais URLs/componentes foram exercitados.

## 4. Classificação dos achados
Reporte cada violação com: critério WCAG violado (ex: 1.1.1 Conteúdo Não-textual), elemento/seletor afetado, severidade (Crítico: bloqueia uso por leitor de tela ou navegação por teclado / Alto / Médio / Baixo) e sugestão de correção.

## 5. Saída
```
Ferramenta usada: <nome e versão>
Nível WCAG alvo: <A/AA/AAA>
Telas/fluxos auditados: <lista>

Violações encontradas:
- [critério WCAG] [seletor/elemento]: descrição — severidade

Veredito: CONFORME <nível> NAS TELAS AUDITADAS / NÃO CONFORME (N violações) / AUDITORIA PARCIAL
```

## Guardrail
Nunca declare conformidade com um nível WCAG (A/AA/AAA) sem execução real da ferramenta contra as telas/fluxos testados — a mesma lógica de "nunca declarar cobertura maior do que a efetivamente exercitada" da `swl-skill-qa-new-mobile-automation` se aplica aqui: "conforme WCAG AA" só pode significar "essas telas específicas, testadas nesta data, com esta ferramenta" — nunca uma extrapolação para o resto do sistema.
