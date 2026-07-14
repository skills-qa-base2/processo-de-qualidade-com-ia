---
name: swl-skill-qa-update-test-docs
description: Atualiza a documentação de testes do projeto (README de automação, glossário de cenários, mapa de cobertura) com base nas mudanças da branch atual.
argument-hint: (sem argumento — analisa a branch atual)
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Identificação das mudanças
Compare a branch atual com a base para identificar cenários, suites ou fixtures novos ou alterados.

## 2. Atualização da documentação
Atualize, conforme aplicável:
- README de automação (como rodar a suíte, variáveis de ambiente necessárias)
- Glossário de cenários (se o projeto mantiver um mapa de cenários por módulo)
- Mapa de cobertura por critério de aceite

## 3. Saída
Aplique as mudanças diretamente nos arquivos de documentação existentes, preservando a estrutura e o tom já usados no projeto.

## Guardrail
Nunca remova documentação de cenários existentes que ainda estão ativos na suíte, mesmo que não tenham sido tocados nesta branch.
