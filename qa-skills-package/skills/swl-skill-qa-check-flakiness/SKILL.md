---
name: swl-skill-qa-check-flakiness
description: Detecta padrões de instabilidade (flakiness) em testes automatizados — waits fixos, dependência de ordem de execução, dados não isolados, seletores frágeis.
argument-hint: <CaminhoDaSuíteOuArquivoDeTeste>
metadata:
  version: 1.0.0
---

## Passos

## 1. Varredura estática
Analise os arquivos de teste em busca de:
- Espera fixa (`sleep`, `Thread.Sleep`, `setTimeout` sem condição)
- Seletores frágeis (XPath posicional, classes de estilo CSS, índices de array)
- Testes que dependem de estado deixado por outro teste (falta de setup/teardown isolado)
- Asserts sobre horário/data sem controle do relógio (time-dependent flakiness)
- Dados compartilhados entre testes paralelos sem isolamento

## 2. Classificação
Liste cada ocorrência com o arquivo, linha e o tipo de flakiness, sem misturar diferentes causas no mesmo apontamento.

## 3. Sugestão de correção
Para cada ocorrência, sugira a correção específica (ex: trocar `sleep(3000)` por espera condicional ao estado da UI/API).

## Guardrail
Não afirme que um teste é flaky sem evidência de execução real (histórico de falhas intermitentes) quando disponível — combine análise estática com o histórico de execução, se houver, antes de classificar como "provavelmente flaky".
