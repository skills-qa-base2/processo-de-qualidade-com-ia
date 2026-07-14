---
name: swl-skill-qa-new-performance-test
description: Gera scripts de teste de performance (carga, stress, spike, soak) detectando a ferramenta do projeto (k6, JMeter, Gatling, Artillery) e define a estratégia — tipo de teste e thresholds — a partir dos requisitos reais informados.
argument-hint: <NomeDoFluxoOuEndpointACarregar>
metadata:
  version: 1.0.1
  validated: true
---

## Passos

## 1. Detecção da ferramenta
Leia o CLAUDE.md e os arquivos de configuração do projeto para identificar a ferramenta de performance já em uso (k6, JMeter, Gatling, Artillery). Nunca introduza uma ferramenta nova sem confirmação explícita do usuário.

## 2. Definição do tipo de teste
Esclareça com o usuário qual tipo de teste é necessário:
- **Smoke**: poucos usuários virtuais, valida que o script funciona
- **Load**: carga esperada em produção
- **Stress**: acima da carga esperada, até achar o ponto de ruptura
- **Spike**: pico repentino de usuários
- **Soak**: carga sustentada por tempo longo, detecta degradação/memory leak

## 3. Definição de thresholds
Pergunte e registre os limites aceitáveis: latência p95/p99, taxa de erro máxima, RPS mínimo esperado. Marque como "a confirmar com o responsável pelo SLA" se não fornecido.

## 4. Geração do script
Gere o script seguindo a ferramenta detectada, parametrizando usuários virtuais/duração conforme o tipo de teste definido no passo 2. Use massa de dados fictícia (via `swl-skill-qa-new-test-data`) para variar o payload entre requisições, nunca dado hardcoded repetido.

## 5. Saída
Salve em `tests/performance/` (ou convenção do projeto).

## Guardrail
Nunca defina o tipo de teste (load/stress/spike/soak) ou os thresholds de aceite por conta própria — são decisões de negócio/SRE que devem ser confirmadas, não assumidas. Um teste de carga com threshold errado aprova em produção um sistema que não aguenta o tráfego real.
