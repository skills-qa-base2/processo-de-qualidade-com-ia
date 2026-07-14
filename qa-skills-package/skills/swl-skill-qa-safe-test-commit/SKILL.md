---
name: swl-skill-qa-safe-test-commit
description: Pipeline completo antes de commitar testes gerados por IA — check-coverage, check-data-quality, check-flakiness e review-tests em sequência, com tag de rastreabilidade.
argument-hint: "<contexto da mudança>"
metadata:
  version: 1.0.0
  validated: true
---

## Passos

Execute em sequência, interrompendo se qualquer etapa encontrar um problema crítico:

1. `swl-skill-qa-check-coverage` — garante que os critérios de aceite relevantes estão cobertos
2. `swl-skill-qa-check-data-quality` — garante que nenhum dado fabricado foi incluído em relatórios/documentação anexos
3. `swl-skill-qa-check-flakiness` — garante que nenhum padrão de instabilidade óbvio foi introduzido
4. `swl-skill-qa-review-tests` — garante nomenclatura e asserts de qualidade

## Tratamento de resultados
| Severidade | Ação |
|---|---|
| Crítica (dado fabricado, cenário essencial sem cobertura) | Bloqueia o commit até corrigir |
| Alta (flakiness clara, assert fraco) | Corrigir antes de prosseguir |
| Média/Baixa | Registrar como observação, pode prosseguir |

## Geração do commit
Após as verificações, gere a mensagem de commit no padrão Conventional Commits com a tag `[ai-assisted-test]`, e faça commit + push.

```
test(produto): adicionar cenarios de cadastro de Produto [ai-assisted-test]

- Adiciona casos de teste happy path, edge case e negativo
- Cobertura verificada via swl-skill-qa-check-coverage
- Dados de teste gerados via swl-skill-qa-new-test-data (ficticios)

Refs: PROJ-142
Generated-by: Claude Code /swl-skill-qa-new-test-cases + /swl-skill-qa-new-automation
Reviewed-by: <nome do QA>
```

## Guardrail
Nunca pule uma etapa do pipeline mesmo que o usuário peça pressa — se for necessário pular, registre explicitamente no corpo do commit qual verificação foi pulada e por quê, para que fique rastreável.
