---
name: swl-skill-qa-describe-test-pr
description: Gera a descrição de um Pull Request de testes, identificando automaticamente cenários gerados por IA versus escritos manualmente.
argument-hint: (sem argumento — analisa a branch atual)
metadata:
  version: 1.1.0
  validated: true
---

## Passos

## 1. Análise da branch
Descubra a branch base antes de comparar: a base do PR aberto (`gh pr view --json baseRefName`), senão o upstream (`git rev-parse --abbrev-ref @{u}`), senão o HEAD do remoto (`git symbolic-ref refs/remotes/origin/HEAD`). Se nada resolver, pergunte — não assuma `main` nem `master`. Analise os commits e arquivos de teste modificados em `git diff <base>...HEAD`.

## 2. Categorização
Separe os testes gerados por IA dos escritos ou ajustados manualmente pelo marcador `generated-by-ai` no próprio arquivo — é a fonte de verdade e sobrevive a qualquer forma de commit. A tag `[ai-assisted-test]` na mensagem de commit é sinal secundário: pode faltar se o commit não passou por `swl-skill-qa-safe-test-commit`. Se as duas divergirem, reporte a divergência em vez de escolher uma.

## 3. Geração da descrição
```
## Descrição
<resumo do que foi testado>

## Uso de IA
- Ferramenta: Claude Code CLI
- Cenários gerados por IA e revisados (`reviewed`): <lista>
- Cenários gerados por IA pendentes (`pending-review`): <lista>
- Cenários/ajustes manuais: <lista>

## Cobertura
<resultado do swl-skill-qa-check-coverage mais recente>

## Checklist
- [ ] Testes revisados e marcados com generated-by-ai: reviewed
- [ ] swl-skill-qa-check-flakiness executado
- [ ] Nenhum dado real de cliente usado como massa de teste
```

## Guardrail
Nunca afirme que um cenário foi "revisado" na descrição do PR se o comentário `generated-by-ai: reviewed` não estiver presente no arquivo correspondente. Se um item do checklist não foi verificado, escreva "não executado" em vez de deixá-lo em branco — item vazio esconde o gap de quem revisa o PR.
