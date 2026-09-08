---
name: swl-skill-qa-review-tests
description: Revisa testes gerados ou existentes quanto a nomenclatura, clareza de asserts e cobertura real de cenários — evita testes triviais ou redundantes.
argument-hint: <CaminhoDoArquivoOuFeature>
metadata:
  version: 1.1.0
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

## 5. Promoção do marcador
Esta é a única skill do pacote que troca `generated-by-ai: pending-review` por `reviewed`. Só faça a troca com as três condições satisfeitas: as observações dos passos 1 a 3 foram apresentadas; uma pessoa confirmou explicitamente nesta conversa que revisou e aceita o teste; o teste foi executado com sucesso, ou o usuário informou o resultado real da execução. Faltando qualquer uma, mantenha `pending-review` e diga o que falta.

## Guardrail
Esta skill não gera nem corrige o conteúdo do teste — aponta os problemas para o QA decidir; a única edição que ela faz é a do marcador. Nunca promova o marcador na mesma passada em que o teste foi gerado, e nunca trate pressa ou um "pode seguir" genérico como confirmação de revisão.
