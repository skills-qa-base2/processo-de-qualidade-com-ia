---
name: swl-skill-qa-check-security
description: Verificação de segurança stack-agnóstica (Node, Python, Java, mobile — qualquer stack fora de .NET Web API), do ponto de vista de QA funcional/dinâmico, não revisão estática de código. Complementa (não duplica) a `swl-skill-check-security` do pacote `org-skills`, que cobre especificamente APIs .NET.
argument-hint: <URL, endpoint ou fluxo a verificar>
metadata:
  version: 1.0.0
  validated: false
---

## Passos

## 1. Levantamento do alvo e do que já existe
Identifique o stack do projeto (Node, Python, Java, mobile, etc.) via CLAUDE.md/config. Se o projeto for .NET Web API, esta skill não deve ser usada — use `swl-skill-check-security` do pacote `org-skills`, que já cobre esse caso em profundidade. Verifique também se o projeto já tem ferramenta de teste de segurança configurada (ex: OWASP ZAP, Burp Suite, sqlmap, ferramenta de scan de dependências) — nunca introduza uma ferramenta nova sem confirmação explícita do usuário.

## 2. Verificação funcional/dinâmica
A partir de um fluxo, tela ou endpoint real informado, verifique como QA funcional (exercitando o sistema em execução, não lendo o código-fonte):
- **Autenticação/autorização**: acessar recurso protegido sem token, com token expirado, ou com token de outro usuário — deve ser rejeitado
- **Injeção**: enviar payload de SQL injection/NoSQL injection/XSS em campos de entrada e observar o comportamento real da resposta (não apenas inspecionar o código)
- **Exposição de dados sensíveis**: verificar se respostas de erro expõem stack trace, versão de framework ou dados de outros usuários
- **CORS/headers**: verificar headers de segurança presentes na resposta real (`Content-Type`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Access-Control-Allow-Origin`)
- **Mobile (quando aplicável)**: certificado pinning, armazenamento local de dados sensíveis (keychain/keystore vs. armazenamento não criptografado), permissões excessivas

## 3. Classificação
Classifique cada achado como Crítico (dado sensível exposto, autenticação contornável) / Alto / Médio / Baixo, com a evidência real observada (request/response, não suposição).

## 4. Saída
Relatório com um achado por linha: endpoint/fluxo testado, payload/ação usada, resposta real observada, severidade. Se nada for encontrado, diga isso claramente — não invente achado para parecer útil.

## Guardrail
Todo achado reportado precisa ter uma evidência real de execução (request/response observado, não uma suposição de como o sistema "provavelmente" se comporta). Nunca reporte "aprovado em segurança" com base em ausência de teste — se um item da lista do passo 2 não foi de fato exercitado, diga explicitamente que ficou fora do escopo desta execução, em vez de presumir que passaria.
