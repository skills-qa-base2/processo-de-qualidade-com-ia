---
name: swl-skill-qa-check-ci-history
description: Analisa o histórico real de execuções do CI para identificar testes flaky por evidência, testes cronicamente quebrados e tendência de duração da suíte. Use quando precisar provar, e não supor, que um teste é instável.
argument-hint: [caminho ou nome do teste — vazio analisa a suíte inteira]
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Fonte do histórico
Busque nesta ordem e diga qual foi usada: API do CI (`gh run list`/`gh api`, Azure DevOps, GitLab CI, Jenkins), arquivos de resultado acumulados em `test-results/` ou artefatos de build, ou o relatório de retry do próprio runner. Se nenhuma fonte estiver acessível, pare e diga isso — sem histórico não há análise, e leitura estática do código é papel de `swl-skill-qa-check-flakiness`.

## 2. Janela
Combine a janela com o usuário (ex: últimos 30 dias ou últimas 50 execuções) e registre-a no relatório. Janela pequena demais transforma coincidência em padrão.

## 3. Classificação por evidência
Cruze resultado com revisão de código:
- **Flaky confirmado**: passou e falhou na mesma revisão (mesmo commit), ou passou em retry sem mudança de código
- **Quebrado**: falha em todas as execuções desde uma revisão identificável — é bug ou teste desatualizado, não flakiness
- **Degradando**: taxa de falha crescente ao longo da janela
- **Estável**: sem falhas na janela

Separar "flaky" de "quebrado" é a distinção mais importante do relatório: quebrado exige correção, flaky exige investigação de causa. Tratar quebrado como flaky é como um time começa a ignorar o CI.

## 4. Duração
Reporte os testes mais lentos e a tendência de duração total da suíte na janela — crescimento contínuo é o que faz o time parar de rodar a suíte.

## 5. Saída
Fonte, janela e número de execuções analisadas; taxa de sucesso da suíte; e as quatro listas com a evidência de cada classificação. Encaminhe os flaky confirmados para `swl-skill-qa-check-flakiness`, que identifica a causa no código, e os quebrados para `swl-skill-qa-diagnose-failure`.

## Guardrail
Toda classificação precisa vir de execução registrada. Nunca estime uma taxa de falha, nunca extrapole tendência a partir de duas execuções, e nunca chame de flaky um teste que apenas falhou algumas vezes em revisões diferentes — isso pode ser regressão real do produto, e é exatamente o caso em que o rótulo "flaky" faz o time ignorar um bug verdadeiro. Se a janela tiver poucas execuções para sustentar a conclusão, diga que a amostra é insuficiente em vez de concluir mesmo assim.
