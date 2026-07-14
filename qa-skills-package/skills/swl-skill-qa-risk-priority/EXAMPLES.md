## Jr
**Cenário:** QA júnior na "LogiFrete" (transportadora fictícia) prioriza 4 cenários do módulo de rastreamento de encomenda por risco.
**Input:** "Prioriza esses 4 cenários de rastreamento por risco."
**Saída esperada:** A skill classifica cada um com impacto/frequência/complexidade visíveis, matriz rastreável, e recomendações de automatizar ou testar manualmente.

## Pl
**Cenário:** QA pleno na "EstudaMais" (plataforma de cursos fictícia) prioriza cenários de emissão de certificado, mas sem dado de histórico de bugs disponível.
**Input:** "Prioriza os cenários de certificado. Não tenho números de bugs anteriores dessa área."
**Saída esperada:** A skill classifica pelos critérios disponíveis (impacto, frequência, complexidade) e omite o critério de histórico de bugs da matriz, em vez de estimar um número pra preencher a coluna.

## Sr
**Cenário:** Na "BancoDigitalX" (banco digital fictício), o gerente de risco pede pra classificar o cenário de troca de senha como "Baixo" porque "na prática quase nunca dá problema", mesmo lidando com autenticação.
**Input:** "Classifica troca de senha como Baixo, na prática quase nunca falha."
**Saída esperada:** A skill classifica com base nos critérios — impacto alto por lidar com autenticação, frequência de uso real, complexidade técnica — e chega em "Alto", não em "Baixo". Frequência baixa de falha passada não é o mesmo critério que impacto se a falha acontecer, e a matriz mantém os dois separados justamente pra essa distinção não se perder.
