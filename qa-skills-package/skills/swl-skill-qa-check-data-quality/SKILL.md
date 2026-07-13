---
name: swl-skill-qa-check-data-quality
description: Audita documentos, relatórios e diagnósticos de QA gerados por IA em busca de dados fabricados ou não rastreáveis a uma fonte real — guardrail anti-invenção.
argument-hint: <CaminhoDoDocumentoOuRelatório>
metadata:
  version: 1.0.0
---

## Passos

## 1. Varredura do documento
Leia o documento gerado (diagnóstico, relatório de execução, proposta) linha a linha.

## 2. Identificação de afirmações factuais
Para cada número, percentual, citação ou afirmação atribuída a uma pessoa/entrevista/execução, verifique se há uma fonte rastreável (entrevista registrada, planilha, log de execução, evidência anexada).

## 3. Sinalização
Marque como suspeito:
- Números redondos demais sem fonte (ex: "90% de satisfação" sem survey)
- Citações atribuídas sem transcrição de origem
- Métricas de teste (cobertura, taxa de sucesso) sem arquivo de resultado correspondente

## 4. Saída
Lista de trechos sinalizados com a pergunta "qual é a fonte disso?" — não corrija automaticamente, apenas aponte para revisão humana.

## Guardrail
Esta skill nunca gera dados para "completar" o que está faltando. Seu único papel é apontar o que não pode ser confirmado, para que o QA busque a fonte real ou remova a afirmação.
