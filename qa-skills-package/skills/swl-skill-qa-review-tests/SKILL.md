---
name: swl-skill-qa-review-tests
description: Revisa testes gerados ou existentes quanto a nomenclatura, clareza de asserts e cobertura real de cenários — evita testes triviais ou redundantes.
argument-hint: <CaminhoDoArquivoOuFeature>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Revisão de nomenclatura
Verifique se o nome do teste descreve o comportamento esperado, não a implementação (ex: `deve_rejeitar_cadastro_com_cpf_invalido`, não `test_1`).

## 2. Revisão de asserts
Verifique se os asserts validam o comportamento relevante (não apenas "não lançou exceção") e se cada teste tem um propósito único e claro.

## 3. Revisão de realismo de cenário
Sinalize testes que cobrem apenas variações triviais dos mesmos dados (ex: trocar só um caractere) sem agregar cobertura real de regra de negócio.

## 4. Saída
Lista de observações por teste: nomenclatura, qualidade de assert, redundância — com recomendação objetiva (manter, ajustar, remover por redundância).

## Guardrail
Esta skill não gera nem corrige o teste automaticamente — aponta os problemas para o QA decidir. Testes gerados por IA revisados aqui só recebem o marcador `generated-by-ai: reviewed` depois que um humano de fato validar as observações.
