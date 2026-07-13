---
name: swl-skill-qa-plan-strategy
description: Entrevista estruturada para levantar a estratégia de testes de um projeto ou feature antes de gerar qualquer cenário — níveis de teste, ferramentas, ambientes e riscos.
argument-hint: <NomeDoProjetoOuFeature>
metadata:
  version: 1.0.0
---

## Passos

## 1. Levantamento de contexto
Leia o CLAUDE.md e os arquivos em `.claude/rules/qa/` (se existirem). Identifique:
- Stack e arquitetura do sistema (monolito, microsserviços, mobile, integrações)
- Ferramentas de gestão de teste já em uso (Jira/Xray, Zephyr, TestLink, planilha)
- Framework de automação já configurado, se houver

Se não houver contexto de QA registrado, pergunte ao usuário antes de prosseguir. Nunca assuma um framework ou ferramenta que não foi confirmado.

## 2. Perguntas estruturadas
Faça, na ordem, e registre as respostas:
1. Quais níveis de teste já existem hoje (unitário, integração, sistema, aceitação)?
2. Existe QA dedicado ou os devs testam o próprio código?
3. Em que momento do ciclo o QA é envolvido — no refinamento, no desenvolvimento, ou só na entrega?
4. Qual a criticidade do sistema (financeiro, dados pessoais, produção crítica)?
5. Existe ambiente de teste dedicado e massa de dados própria?

## 3. Definição da pirâmide de testes aplicável
Com base nas respostas, proponha a distribuição entre teste unitário, integração, sistema/E2E e aceitação — nunca proponha 100% E2E por padrão.

## 4. Saída
Gere `docs/qa/estrategia-teste.md` contendo:
- Resumo do contexto levantado
- Pirâmide de testes proposta com justificativa
- Ferramentas recomendadas (gestão de casos + automação)
- Riscos identificados e como serão tratados

## Guardrail
Nunca invente respostas às perguntas da Seção 2 — se o usuário não souber, registre como "a confirmar" e sinalize como risco em aberto.
