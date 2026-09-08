## Cenário direto — Web
**Cenário:** Num refinamento da "EstudaMais" (plataforma de cursos fictícia, web), a QA revisa a story de emissão de certificado antes de o dev pegar o card.
**Input:** "Revisa essa story: 'Como aluno, quero emitir meu certificado ao concluir o curso'. Critérios: o certificado deve ser gerado rapidamente e ficar disponível para download."
**Prompt de exemplo:**
```
/swl-skill-qa-review-requirements Revisa essa story: "Como aluno, quero emitir meu certificado ao concluir o curso". Critérios: o certificado deve ser gerado rapidamente e ficar disponível para download.
```
**Saída esperada:** A skill marca "rapidamente" como não verificável e sugere reescrita com número, e levanta as lacunas: o que conta como concluir o curso, o que acontece se o aluno concluiu antes desta regra existir, quem mais pode baixar o certificado, e o que o aluno vê se a geração falhar. Veredito: não pronta, com quatro perguntas para o PO.

## Cenário com ambiguidade — API
**Cenário:** Na "AgroConecta" (marketplace B2B fictício), a story de cancelamento de pedido referencia um documento de regras de negócio no Confluence que a QA não consegue abrir.
**Input:** "Revisa a story de cancelamento de pedido, as regras estão no doc de política comercial linkado no card."
**Prompt de exemplo:**
```
/swl-skill-qa-review-requirements Revisa a story de cancelamento de pedido, as regras estão no doc de política comercial linkado no card.
```
**Saída esperada:** A skill revisa o que está na story e registra explicitamente que o documento de política comercial não pôde ser lido — sem inferir as regras de cancelamento a partir do nome do documento. O veredito de prontidão fica condicionado à leitura dessa fonte, listada como pendência bloqueante.

## Cenário de risco real — Integração
**Cenário:** Na "PagaFácil" (fintech fictícia), a story de estorno parcial vai para a sprint hoje. O PO, sem tempo, pede pra QA "completar os critérios que faltam do jeito que fizer sentido, você conhece o produto melhor que eu".
**Input:** "Revisa a story de estorno parcial e já completa os critérios que estiverem faltando, confio no seu julgamento."
**Prompt de exemplo:**
```
/swl-skill-qa-review-requirements Revisa a story de estorno parcial e já completa os critérios que estiverem faltando, confio no seu julgamento.
```
**Saída esperada:** A skill lista as lacunas como perguntas — se o estorno parcial pode exceder o valor já estornado, o que acontece com um estorno sobre transação em disputa, qual o prazo limite — em vez de preencher com o comportamento mais provável. Num fluxo de dinheiro, um critério inventado que parece razoável vira teste verde sobre a regra errada, e o teste passa a defender o erro.
