---
name: swl-skill-qa-update-test-docs
description: Atualiza a documentação de testes do projeto (README de automação, glossário de cenários, mapa de cobertura) com base nas mudanças da branch atual.
argument-hint: (sem argumento — analisa a branch atual)
metadata:
  version: 1.1.0
  validated: false
---

## Passos

## 1. Identificação das mudanças
Descubra a branch base antes de comparar: a base do PR aberto (`gh pr view --json baseRefName`), senão o upstream (`git rev-parse --abbrev-ref @{u}`), senão o HEAD do remoto (`git symbolic-ref refs/remotes/origin/HEAD`). Se nada resolver, pergunte — não assuma `main` nem `master`. Com `git diff <base>...HEAD`, identifique cenários, suites ou fixtures novos ou alterados.

## 2. Atualização da documentação
Atualize, conforme aplicável:
- README de automação (como rodar a suíte, variáveis de ambiente necessárias)
- Glossário de cenários (se o projeto mantiver um mapa de cenários por módulo)
- Mapa de cobertura por critério de aceite

## 3. Saída
Aplique as mudanças diretamente nos arquivos de documentação existentes, preservando a estrutura e o tom já usados no projeto.

## Guardrail
Nunca remova documentação de cenários existentes que ainda estão ativos na suíte, mesmo que não tenham sido tocados nesta branch.
