---
name: swl-skill-qa-check-environment
description: Valida que um ambiente está de fato pronto para rodar a suíte antes da execução — health check dos serviços, seed de dados presente, feature flags no estado esperado — nunca assume que um ambiente está pronto sem checar.
argument-hint: <NomeDoAmbiente>
metadata:
  version: 1.0.0
  validated: false
---

## Passos

## 1. Levantamento do que "pronto" significa neste projeto
Leia o CLAUDE.md e `.claude/rules/qa/` (se existirem, especialmente `convencoes-teste.md` gerado por `swl-skill-qa-generate-rules`) para identificar quais serviços, dados de seed e feature flags o ambiente precisa ter. Se não houver essa definição registrada, pergunte ao usuário — nunca assuma um critério de "ambiente pronto" genérico sem confirmação.

## 2. Health check dos serviços
Verifique, com uma chamada real (não suposição), que cada serviço/dependência necessário está de fato respondendo: API principal, banco de dados, filas, serviços externos mockados/stubados (ex: WireMock/MockServer, se o projeto usar).

## 3. Verificação de seed de dados
Confirme que a massa de dados esperada (gerada via `swl-skill-qa-new-test-data`, se aplicável) está de fato presente no ambiente — não apenas que o script de seed existe, mas que os dados resultantes estão lá.

## 4. Verificação de feature flags
Se o projeto usa feature flags, confirme o estado real de cada flag relevante para a suíte que vai rodar, comparando com o estado esperado informado pelo usuário.

## 5. Saída
```
Ambiente: <nome>
Serviços verificados: <lista com status real: UP / DOWN / não verificado>
Seed de dados: <presente / ausente / não verificado>
Feature flags: <flag: estado real vs. esperado>

Veredito: AMBIENTE PRONTO / AMBIENTE NÃO PRONTO (motivo) / VERIFICAÇÃO PARCIAL (o que não pôde ser checado)
```

## Guardrail
Nunca assuma que um ambiente está pronto sem checar de fato — um "ambiente pronto" presumido é a mesma classe de erro que os guardrails de "nunca inferir" já usados nas demais skills (nunca inferir schema sem especificação real, nunca inferir threshold sem confirmação), aplicada a ambiente em vez de dado/contrato/performance. Se um item do passo 2, 3 ou 4 não puder ser verificado (ex: sem acesso à infraestrutura), diga isso explicitamente como "não verificado" — nunca reporte como "OK" por omissão.
