---
name: swl-skill-qa-diagnose-failure
description: Recebe log, stack trace ou descrição de falha de teste e rastreia até a causa raiz, distinguindo bug de produto, teste mal escrito ou instabilidade de ambiente.
argument-hint: "<descrição ou log da falha>"
metadata:
  version: 1.0.0
---

## Passos

## 1. Classificação inicial
A partir do log/descrição fornecido, classifique a falha em uma das categorias:
- **Bug de produto**: comportamento real da aplicação diverge do esperado
- **Teste mal escrito**: assert incorreto, dado de teste inválido, expectativa desatualizada
- **Ambiente/infraestrutura**: timeout de rede, serviço externo indisponível, dado de ambiente inconsistente
- **Flakiness**: falha intermitente sem mudança de código (encaminhar para `swl-skill-qa-check-flakiness`)

## 2. Rastreamento
Para bug de produto ou teste mal escrito, rastreie até a causa raiz usando o stack trace, logs e o código relevante.

## 3. Proposta de ação
- Bug de produto → gerar relatório com `swl-skill-qa-report-bug`
- Teste mal escrito → sugerir a correção do teste
- Ambiente → sinalizar ao responsável por infraestrutura, não tentar mascarar no teste

## Guardrail
Nunca classifique uma falha como "flaky" ou "ambiente" só para evitar investigar mais a fundo — essa é a saída mais fácil e também a mais perigosa quando esconde um bug real.
