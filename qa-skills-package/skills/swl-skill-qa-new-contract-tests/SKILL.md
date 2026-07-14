---
name: swl-skill-qa-new-contract-tests
description: Gera testes de contrato/schema para APIs (validação contra OpenAPI/JSON Schema, contratos consumer-driven via Pact/Spring Cloud Contract) a partir da especificação real da API — nunca infere contrato sem uma fonte.
argument-hint: <NomeDoServiçoOuEndpoint>
metadata:
  version: 1.0.1
  validated: true
---

## Passos

## 1. Levantamento da fonte do contrato
Busque a especificação real: arquivo OpenAPI/Swagger, JSON Schema, ou contrato Pact já publicado no broker. Se não houver especificação formal, pergunte ao usuário onde o contrato está documentado.

## 2. Detecção da abordagem
- Projeto com múltiplos consumidores/microsserviços → contrato consumer-driven (Pact, Spring Cloud Contract)
- Projeto com OpenAPI/Swagger publicado → validação de schema de resposta usando a biblioteca de schema validation do stack detectado

Nunca introduza uma ferramenta de contrato nova sem confirmação explícita do usuário.

## 3. Geração dos testes
Para cada endpoint, valide:
- Status code esperado
- Schema do corpo de resposta (tipos, campos obrigatórios, formatos)
- Headers relevantes (ex: `Content-Type`)

Para consumer-driven: gere o contrato do lado consumidor e o teste de verificação correspondente do lado provedor.

## 4. Versionamento de contrato
Sinalize quando uma mudança de contrato é **breaking** (remoção/renomeação de campo obrigatório, mudança de tipo) vs. **não-breaking** (campo novo opcional).

## 5. Saída
Salve em `tests/contract/` (ou convenção do projeto). Publique no broker de contratos se o projeto já usar um (ex: Pact Broker).

## Guardrail
Nunca gere um teste de contrato a partir de suposição sobre o formato da resposta. Se não houver especificação real (OpenAPI, schema, contrato já publicado) nem uma resposta real de exemplo fornecida, pergunte antes de inventar campos, tipos ou estrutura.
