---
name: swl-skill-qa-describe-test-pr
description: Gera a descrição de um Pull Request de testes, identificando automaticamente cenários gerados por IA versus escritos manualmente.
argument-hint: (sem argumento — analisa a branch atual)
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Análise da branch
Analise os commits e arquivos de teste modificados na branch atual em relação à base.

## 2. Categorização
Separe: arquivos de teste gerados por skill de IA (identificáveis pela tag `[ai-assisted-test]` nos commits) vs. escritos ou ajustados manualmente.

## 3. Geração da descrição
```
## Descrição
<resumo do que foi testado>

## Uso de IA
- Ferramenta: Claude Code CLI
- Cenários gerados por IA: <lista>
- Cenários/ajustes manuais: <lista>

## Cobertura
<resultado do swl-skill-qa-check-coverage mais recente>

## Checklist
- [ ] Testes revisados e marcados com generated-by-ai: reviewed
- [ ] swl-skill-qa-check-flakiness executado
- [ ] Nenhum dado real de cliente usado como massa de teste
```

## Guardrail
Nunca afirme que um cenário foi "revisado" na descrição do PR se o comentário `generated-by-ai: reviewed` não estiver presente no arquivo correspondente.
