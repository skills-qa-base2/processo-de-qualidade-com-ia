---
name: swl-skill-qa-review-requirements
description: Revisa uma user story ou requisito sob a ótica de QA antes do desenvolvimento — testabilidade, ambiguidade, critérios de aceite verificáveis e lacunas de regra. Use no refinamento, para levar perguntas ao PO em vez de descobrir o gap na hora de testar.
argument-hint: <UserStoryOuCaminhoDoCard>
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Leitura da story
Leia a descrição, os critérios de aceite, as regras de negócio e os anexos referenciados. Anexo referenciado e inacessível é lacuna a registrar, não conteúdo a supor.

## 2. Verificabilidade de cada critério
Para cada critério de aceite pergunte: é possível escrever um teste que dê inequivocamente passa ou falha? Sinalize os que não passam nesse teste — termo subjetivo sem número ("rápido", "amigável", "de forma adequada"), critério sem gatilho claro ("o sistema deve validar" — validar o quê, quando, e o que acontece se falhar), critério que descreve implementação em vez de comportamento observável, e critério que só descreve o caminho feliz.

## 3. Lacunas clássicas
Liste as que a story não responde: permissão (quem pode e quem não pode), estado (recurso inexistente, inativo ou já processado), limites (tamanho, faixa, obrigatoriedade de cada campo), concorrência (dois usuários sobre o mesmo recurso), falha de dependência externa, retroatividade sobre registros criados antes desta regra, requisitos não-funcionais associados, e observabilidade (o comportamento é verificável por quem testa).

## 4. Testabilidade técnica
Aponte o que precisa ser combinado com o dev ainda no refinamento: falta de `data-testid` nos elementos novos, ausência de endpoint ou seed para preparar o estado, dependência externa sem ambiente de sandbox, ação sem retorno observável.

## 5. Saída
Veredito de prontidão (pronta para dev / pronta com ressalvas / não pronta), critérios não verificáveis com reescrita sugerida, perguntas objetivas para o PO, riscos de testabilidade para o dev, e os cenários que já dá para antecipar — insumo para `swl-skill-qa-new-test-cases`.

## Guardrail
Nunca responda por conta própria as perguntas destinadas ao PO, nem transforme uma suposição razoável em critério de aceite. O valor desta skill é produzir a lista de perguntas certas antes de o código existir — uma lacuna preenchida por adivinhação vira um teste que valida o comportamento errado com toda a confiança, e o erro só aparece em produção. Reescrita de critério é sugestão apresentada ao time; não edite a story na ferramenta de gestão sem pedido explícito.
