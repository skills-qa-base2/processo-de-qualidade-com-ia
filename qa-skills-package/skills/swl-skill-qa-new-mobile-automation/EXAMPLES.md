## Cenário direto — Mobile
**Cenário:** Um QA no app "PetAmigo" (adoção de pets fictícia) precisa automatizar a tela de favoritar um pet, com Detox já configurado.
**Input:** "Gera a automação mobile do cenário de favoritar um pet, já temos Detox configurado e o ScreenObject de Listagem pronto."
**Prompt de exemplo:**
```
/swl-skill-qa-new-mobile-automation Gera a automação mobile do cenário de favoritar um pet, já temos Detox configurado e o ScreenObject de Listagem pronto.
```
**Saída esperada:** A skill detecta Detox via `.detoxrc`, reutiliza o Screen Object existente, usa seletores por `testID`, declara "testado no emulador Android 14 (Pixel 7)" e marca `generated-by-ai: pending-review`.

## Cenário com ambiguidade — Mobile
**Cenário:** Um QA na "BancoDigitalX" (banco digital fictício) precisa automatizar a aprovação de transferência via biometria, mas não está claro se o projeto já trata o diálogo nativo de biometria em algum outro teste.
**Input:** "Automatiza a aprovação de transferência via biometria no Appium. Não sei se já lidamos com o diálogo do sistema de biometria em algum outro teste."
**Prompt de exemplo:**
```
/swl-skill-qa-new-mobile-automation Automatiza a aprovação de transferência via biometria no Appium. Não sei se já lidamos com o diálogo do sistema de biometria em algum outro teste.
```
**Saída esperada:** A skill gera o teste cobrindo o fluxo, mas ao chegar no diálogo nativo de biometria do SO, marca que não encontrou tratamento existente pra esse tipo de diálogo no projeto e pergunta se deve ser mockado (comum em CI, já que biometria real não funciona em emulador) antes de assumir uma abordagem.

## Cenário de risco real — Mobile
**Cenário:** Na "RotaCerta" (app do entregador fictício), o QA testou só no emulador Android mais recente, mas o gerente de operações pede pra "confirmar que funciona em todos os celulares dos entregadores" pra aprovar o rollout geral.
**Input:** "Preciso saber se a atualização do app funciona nos celulares dos entregadores em geral, pra liberar pra todo mundo essa semana."
**Prompt de exemplo:**
```
/swl-skill-qa-new-mobile-automation Preciso saber se a atualização do app funciona nos celulares dos entregadores em geral, pra liberar pra todo mundo essa semana.
```
**Saída esperada:** A skill documenta exatamente o que rodou (emulador Android 14, Pixel 7) e não estende essa cobertura pra "os celulares dos entregadores em geral" — a frota real inclui Android 9 a 14 em fabricantes variados, nenhum deles exercitado nesta execução. O rollout geral, aprovado só com base nesse teste, estaria liberando pra um universo de dispositivos nunca tocado.

> Exceção documentada: esta skill é inerentemente mobile — os 3 exemplos ficam no mesmo tipo de projeto de propósito, já que não existe versão web/API/integração de automação mobile.
