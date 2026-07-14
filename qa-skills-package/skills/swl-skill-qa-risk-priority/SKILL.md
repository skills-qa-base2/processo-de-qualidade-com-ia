---
name: swl-skill-qa-risk-priority
description: Prioriza cenários de teste por criticidade de negócio e risco técnico, gerando uma matriz de priorização para orientar automação e execução manual.
argument-hint: <NomeDaFeatureOuMóduloAMapear>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Levantamento dos cenários
Liste os cenários já mapeados (via `swl-skill-qa-new-test-cases` ou `swl-skill-qa-new-bdd-scenarios`) ou peça ao usuário a lista de funcionalidades do módulo.

## 2. Critérios de classificação
Para cada cenário, avalie:
- **Impacto financeiro ou legal** se falhar (alto/médio/baixo)
- **Frequência de uso** pelo usuário final
- **Complexidade técnica** do fluxo (integrações, regras de negócio encadeadas)
- **Histórico de bugs** nessa área, se houver dados reais disponíveis

## 3. Classificação
Classifique cada cenário em Crítico / Alto / Médio / Baixo. Nunca classifique como Crítico ou Alto sem justificativa registrada por critério.

## 4. Saída
Gere uma matriz (tabela ou planilha, conforme convenção do projeto) com colunas: Cenário | Impacto | Frequência | Complexidade | Classificação Final | Recomendação (automatizar / testar manualmente a cada release / testar sob demanda).

## Guardrail
A classificação final deve ser rastreável aos critérios individuais — nunca apresente uma nota final sem mostrar como foi composta. Não usar dados de incidentes reais sem confirmação do usuário; se não houver histórico real, omita esse critério em vez de estimar.
