---
name: swl-skill-qa-select-regression-suite
description: Seleciona o subconjunto de regressão a executar numa release, cruzando o diff de código com a matriz de risco e o histórico de bugs, em vez de rodar tudo ou escolher no feeling. Use quando não há tempo ou ambiente para a suíte completa.
argument-hint: <tag/branch de release ou intervalo de commits>
metadata:
  version: 1.0.0
  validated: false
---

## Passos

## 1. Escopo da release
Determine o intervalo a analisar (`git diff <tag-anterior>...<tag-atual>`). Se o intervalo não for informado nem dedutível das tags, pergunte — comparar contra a base errada produz uma seleção sem valor.

## 2. Mapeamento de impacto
Para cada área alterada, identifique os módulos e fluxos afetados, incluindo o impacto indireto e dizendo como o inferiu: código compartilhado (helper, middleware, componente de UI base) afeta todo consumidor; contrato de API afeta os consumidores conhecidos; schema ou migration afeta todo fluxo que lê ou grava a tabela; configuração, dependência ou build afeta a aplicação inteira. Impacto não rastreável pelo código (ex: mudança em serviço externo) entra como área de risco a confirmar com o time.

## 3. Cruzamento com risco
Cruze as áreas impactadas com a matriz de `swl-skill-qa-risk-priority` e com o histórico de `swl-skill-qa-check-ci-history`, se existirem. Se nenhuma das duas fontes existir, diga isso e trate a seleção como preliminar, baseada só no diff.

## 4. Montagem da seleção
Classifique em três faixas, justificando cada uma pelo impacto que a motivou:
- **Obrigatórios**: fluxos críticos diretamente impactados, mais os fluxos críticos de negócio que nunca saem da regressão (login, pagamento, permissão), mesmo sem alteração aparente
- **Recomendados**: impacto indireto ou histórico de regressão na área
- **Fora desta regressão**: áreas sem relação com o diff — liste explicitamente, para que a decisão de não rodar fique registrada

## 5. Saída
Release, arquivos alterados, módulos impactados, fontes de risco usadas, as três faixas com justificativa, e a seção "riscos aceitos ao não rodar a suíte completa" em termos de negócio. Para executar, use `swl-skill-qa-run-tests` com o filtro correspondente, registrando que a execução foi parcial e por seleção de risco.

## Guardrail
Esta skill recomenda um recorte; a decisão de não executar parte da suíte é do time e precisa ser tomada com a seção de riscos aceitos à vista. Nunca apresente a seleção como equivalente à regressão completa. Nunca marque uma área como dispensável só porque nenhum arquivo dela mudou: dependência compartilhada, configuração e migration quebram exatamente as áreas que ninguém tocou. Na dúvida sobre impacto indireto, inclua o cenário e explique a dúvida.
