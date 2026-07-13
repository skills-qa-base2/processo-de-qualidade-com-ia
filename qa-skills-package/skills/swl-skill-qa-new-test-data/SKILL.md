---
name: swl-skill-qa-new-test-data
description: Gera massa de dados de teste fictícia (nunca dados reais de cliente) via factories/fixtures, respeitando as regras de negócio do domínio.
argument-hint: <NomeDaEntidadeOuDomínio>
metadata:
  version: 1.0.0
---

## Passos

## 1. Identificação das regras do domínio
Leia o CLAUDE.md e o modelo/entidade envolvida. Identifique campos obrigatórios, formatos, valores válidos e regras de negócio (ex: CPF válido no formato mas fictício, faixas de valor aceitáveis).

## 2. Geração dos conjuntos de dados
Gere, usando a biblioteca de fixtures já usada no projeto (Faker, Bogus, factory_boy ou equivalente):
- Conjunto **válido** completo (happy path)
- Conjuntos de **borda** (valor mínimo, máximo, string vazia, campo opcional ausente)
- Conjuntos **inválidos** (formato incorreto, tipo errado, campo obrigatório ausente)

## 3. Saída
Salve como factory/fixture reutilizável em `test/factories/` (ou caminho de convenção do projeto) — nunca como valores soltos duplicados em cada teste.

## Guardrail
Dados fictícios apenas. Nunca use CPF, e-mail, telefone ou qualquer dado real de cliente, mesmo mascarado parcialmente, como base para massa de teste. Se o usuário colar dados reais para servir de exemplo, gere uma versão totalmente fictícia equivalente e avise que os dados reais não foram usados.
