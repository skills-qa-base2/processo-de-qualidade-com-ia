---
name: swl-skill-qa-generate-rules
description: Gera .claude/rules/qa/ a partir de documentação técnica existente ou entrevista com o time — útil para configurar projetos legados sem processo de teste definido.
argument-hint: <NomeDoProjeto>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Levantamento de fontes
Busque documentação existente sobre o processo de teste do projeto (planilhas, wiki, README). Se não houver nada, conduza uma entrevista curta com o usuário cobrindo: ferramentas usadas, convenções de nomenclatura de cenários, estrutura de pastas de teste, política de dados de teste.

## 2. Geração dos arquivos de regras
Gere em `.claude/rules/qa/`:
- `padroes-teste.md` — nomenclatura, estrutura de pastas, convenções de asserts
- `restricoes-teste.md` — o que a IA não deve fazer (ex: não usar dados reais, não pular etapas do swl-skill-qa-safe-test-commit)
- `convencoes-teste.md` — ferramentas de automação e gestão de casos em uso, ambientes disponíveis

## 3. Validação
Apresente o conteúdo gerado ao usuário antes de considerar finalizado — regras de projeto legado frequentemente têm exceções que só quem já trabalha no projeto conhece.

## Guardrail
Nunca infira convenções de um projeto a partir de suposições genéricas quando não há documentação nem confirmação do usuário — é melhor deixar uma seção marcada como "a definir" do que gerar uma regra incorreta que a IA passará a seguir automaticamente depois.
