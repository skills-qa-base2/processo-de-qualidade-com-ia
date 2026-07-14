---
name: swl-skill-qa-report-bug
description: Gera relatório de bug estruturado (passos para reproduzir, evidência, severidade) pronto para abrir no sistema de gestão do projeto.
argument-hint: "<descrição do problema encontrado>"
metadata:
  version: 1.0.0
  validated: true
---

## Passos

## 1. Coleta de informações
A partir da descrição ou do diagnóstico de `swl-skill-qa-diagnose-failure`, reúna:
- Passos exatos para reproduzir
- Ambiente (versão, navegador/dispositivo, dados usados)
- Resultado esperado vs. resultado obtido
- Evidência disponível (log, print, vídeo — referenciar o arquivo, não inventar conteúdo)

## 2. Classificação de severidade
Classifique como Crítica / Alta / Média / Baixa, com o critério explícito (ex: bloqueia fluxo principal = Crítica; afeta fluxo secundário com contorno disponível = Média).

## 3. Geração do relatório
```
Título: <resumo objetivo do problema>
Severidade: <Crítica/Alta/Média/Baixa>
Ambiente: <onde foi encontrado>
Passos para reproduzir: <numerados>
Resultado esperado: <...>
Resultado obtido: <...>
Evidência: <referência ao arquivo/print/log>
```

## Guardrail
Nunca preencha "resultado esperado" ou "passos para reproduzir" com suposições quando a informação não foi fornecida — pergunte ao invés de inventar. Um bug reportado com informação incorreta atrapalha mais do que ajuda.
