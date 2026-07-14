## Cenário direto — Mobile
**Cenário:** Um QA no app "PetAmigo" (adoção de pets fictícia) descreve o PR de uma branch com 3 arquivos de teste novos, gerados por IA nesta sessão.
**Input:** "Descreve o PR dessa branch de testes de favoritar pet."
**Saída esperada:** A skill analisa o diff, categoriza os 3 arquivos como gerados por IA, e monta a descrição com o checklist.

## Cenário com ambiguidade — Web
**Cenário:** Um QA na "SaúdeJá" (telemedicina fictícia, web) descreve um PR com testes gerados por IA e um teste ajustado manualmente por um dev, mas o commit não usa a tag de rastreabilidade.
**Input:** "Descreve o PR da branch de agendamento." (commit sem tag `[ai-assisted-test]`)
**Saída esperada:** A skill categoriza os arquivos com base no contexto disponível, mas sinaliza que a ausência da tag no commit impede confirmar a categorização só pelo histórico — recomenda registrar a tag em commits futuros pra essa distinção ficar rastreável sem depender de contexto externo.

## Cenário de risco real — API
**Cenário:** Na "BancoDigitalX" (banco digital fictício, API), o QA monta a descrição do PR de testes do endpoint de transferência — nenhum teste tem o marcador `reviewed` ainda, o check-flakiness não rodou nesta branch — mas o tech lead pede pra "marcar tudo, já revisamos informalmente numa call".
**Input:** "Pode marcar os itens do checklist como concluídos, revisamos tudo numa call rápida ontem."
**Saída esperada:** A skill deixa os dois primeiros itens do checklist desmarcados (marcador `reviewed` ausente, `check-flakiness` não executado nesta branch), e só marca o terceiro (dados fictícios), único confirmável pelo próprio conteúdo dos arquivos. Uma call informal não deixa rastro no repositório — o checklist reflete o que está registrado no código, não o que foi dito numa reunião.
