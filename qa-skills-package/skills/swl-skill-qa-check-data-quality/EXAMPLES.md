## Cenário direto — Web
**Cenário:** Um QA na "EstudaMais" (plataforma de cursos fictícia, web) audita um relatório simples de execução de testes do módulo de matrícula antes de enviar pro time.
**Input:** "Audita esse relatório de testes do módulo de matrícula antes de eu enviar pro time."
**Saída esperada:** A skill confere as afirmações do relatório — todas rastreáveis ao arquivo de resultado real anexado — e não sinaliza nada, já que não há número ou citação sem fonte.

## Cenário com ambiguidade — API
**Cenário:** Um QA na "AgroConecta" (marketplace B2B fictício, API) audita um relatório de diagnóstico de bug com uma citação de cliente sem transcrição anexada.
**Input:** "Audita esse relatório de bug antes de eu abrir o chamado." (o relatório cita "o cliente disse que trava toda vez" sem anexo)
**Saída esperada:** A skill sinaliza a citação atribuída ao cliente como sem fonte rastreável (nenhuma transcrição, e-mail ou print anexado) e pergunta qual é a origem, sem remover nem confirmar a afirmação por conta própria.

## Cenário de risco real — Mobile
**Cenário:** Na "RotaCerta" (app do entregador fictício, mobile), um analista entrega ao QA um relatório de sessão exploratória com "98% de satisfação dos entregadores testados" pra incluir no relatório trimestral de qualidade da diretoria.
**Input:** "Pode revisar esse relatório antes de eu mandar pra diretoria? Tem um número de satisfação ali."
**Saída esperada:** A skill sinaliza o "98% de satisfação" como número redondo demais sem fonte associada — não há survey, entrevista registrada nem pesquisa anexada — e pergunta de onde veio, em vez de deixar passar por já estar num relatório formatado. Um número assim, uma vez impresso num relatório de diretoria, costuma virar fato citado depois, mesmo que ninguém mais lembre de onde saiu.
