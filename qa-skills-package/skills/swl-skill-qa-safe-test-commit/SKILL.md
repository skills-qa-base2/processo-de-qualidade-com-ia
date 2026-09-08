---
name: swl-skill-qa-safe-test-commit
description: Pipeline completo antes de commitar testes gerados por IA — execução da suíte, check-coverage, check-data-quality, check-flakiness e review-tests em sequência, com tag de rastreabilidade.
argument-hint: "<contexto da mudança>"
metadata:
  version: 1.1.0
  validated: false
---

## Passos

Execute em sequência, interrompendo se qualquer etapa encontrar um problema crítico:

1. Execute a suíte de testes afetada pela mudança e confirme que passa. Teste falhando, ou que não pôde ser executado no ambiente atual, bloqueia o commit — é resultado a reportar, não etapa a pular.
2. `swl-skill-qa-check-coverage` — garante que os critérios de aceite relevantes estão cobertos
3. `swl-skill-qa-check-data-quality` — garante que nenhum dado fabricado foi incluído em relatórios/documentação anexos
4. `swl-skill-qa-check-flakiness` — garante que nenhum padrão de instabilidade óbvio foi introduzido
5. `swl-skill-qa-review-tests` — nomenclatura, asserts e promoção do marcador para `reviewed`

## Tratamento de resultados
| Severidade | Ação |
|---|---|
| Crítica (teste falhando, dado fabricado, cenário essencial sem cobertura) | Bloqueia o commit até corrigir |
| Alta (flakiness clara, assert fraco) | Corrigir antes de prosseguir |
| Média/Baixa | Registrar como observação, pode prosseguir |

## Geração do commit
Só depois das cinco etapas, gere a mensagem no padrão Conventional Commits com a tag `[ai-assisted-test]`.

```
test(produto): adicionar cenarios de cadastro de Produto [ai-assisted-test]

- Adiciona casos de teste happy path, edge case e negativo
- Cobertura verificada via swl-skill-qa-check-coverage
- Dados de teste gerados via swl-skill-qa-new-test-data (ficticios)

Refs: PROJ-142
Generated-by: Claude Code /swl-skill-qa-new-test-cases + /swl-skill-qa-new-automation
Reviewed-by: <nome do QA>
```

Preencha `Reviewed-by:` com quem confirmou a revisão na etapa 5, obtido de `git config user.name` e confirmado com o usuário; se ninguém confirmou, omita a linha. Não invente número de card em `Refs:`.

## Commit e push
Apresente a mensagem e o resumo das cinco etapas, e peça confirmação antes de commitar. O push é um passo separado, com confirmação própria — ele expõe o trabalho ao time e dispara o CI. Se a branch atual for a branch base do repositório, não commite: avise e proponha criar uma branch.

## Guardrail
As cinco etapas são obrigatórias. Se o usuário pedir pressa, reporte o que foi encontrado até ali e pergunte o que ele quer fazer — não pule a etapa por conta própria. Uma etapa só pode ser pulada por decisão explícita do usuário, e nesse caso o corpo do commit precisa registrar qual e por quê: `Skipped-check: <skill> (<motivo>, decisão de <nome>)`.
