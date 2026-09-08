---
name: swl-skill-qa-release-signoff
description: Consolida as evidências reais de uma release (execução de testes, cobertura de cenários, bugs abertos, requisitos não-funcionais) num parecer de qualidade go/no-go rastreável. Use na véspera de um deploy, quando alguém precisa decidir se libera.
argument-hint: <versão ou tag da release>
metadata:
  version: 1.0.0
  validated: false
---

## Passos

## 1. Coleta de evidências
Reúna apenas evidência com origem verificável, registrando fonte e data de cada item: execução funcional (`swl-skill-qa-run-tests` / `swl-skill-qa-generate-test-report`), escopo executado (suíte completa ou recorte de `swl-skill-qa-select-regression-suite`), cobertura de cenários (`swl-skill-qa-check-coverage`), bugs em aberto com severidade, não-funcionais aplicáveis à release (`swl-skill-qa-check-performance-results`, `swl-skill-qa-check-accessibility`, `swl-skill-qa-check-security`) e estabilidade da suíte (`swl-skill-qa-check-ci-history`).

Evidência ausente entra no parecer como "não verificado", com o impacto que isso tem na decisão — não é omitida nem substituída por estimativa.

## 2. Critérios de liberação
Use os critérios de `.claude/rules/qa/` se existirem. Se o projeto não os define, proponha e peça confirmação antes de aplicar. Padrão sugerido: nenhum bug de severidade Crítica em aberto nas funcionalidades da release; regressão obrigatória executada e verde; critérios de aceite das features da release cobertos e executados; não-funcionais aplicáveis dentro do threshold definido.

## 3. Parecer
Recomendação (LIBERAR / LIBERAR COM RESSALVAS / NÃO LIBERAR / EVIDÊNCIA INSUFICIENTE) seguida da tabela de evidências com item, resultado, fonte e data; a lista do que não foi verificado e o risco de cada item; as ressalvas com plano de mitigação acordado; e os riscos residuais em termos de impacto no usuário.

## 4. Registro
Salve em `docs/qa/releases/<versão>-signoff.md` e informe o caminho. O parecer precisa continuar consultável depois do deploy — é o que permite entender, num incidente, o que se sabia no momento da decisão.

## Guardrail
Este parecer é uma recomendação técnica de QA baseada em evidência, não a aprovação de negócio: a decisão de subir é de quem tem essa responsabilidade no time. Nunca recomende LIBERAR com evidência faltando — nesse caso o veredito é EVIDÊNCIA INSUFICIENTE, com a lista do que precisa ser verificado. Ausência de bug reportado não é evidência de qualidade, é ausência de teste até que se prove o contrário. Nunca preencha uma célula da tabela com número que não veio de arquivo, relatório ou board real, e nunca ajuste o veredito por pressão de prazo: um parecer que diz "libera" porque a data chegou não protege ninguém.
