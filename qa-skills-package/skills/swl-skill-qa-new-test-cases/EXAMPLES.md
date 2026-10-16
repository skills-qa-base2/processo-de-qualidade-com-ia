## Cenário direto — Mobile
**Cenário:** Um QA no app mobile "PetAmigo" (adoção de pets fictícia) recebe uma user story simples de favoritar um pet.
**Input:** "User story: como usuário, quero favoritar um pet pra ver depois na minha lista."
**Prompt de exemplo:**
```
/swl-skill-qa-new-test-cases User story: como usuário, quero favoritar um pet pra ver depois na minha lista.
```
**Saída esperada:** A skill reconhece que favoritar não tem faixa de valor nem combinação de condições, e gera o happy path como caso direto, sem forçar técnica. Nas demais regras aplica a que cabe: favoritar o mesmo pet duas vezes vira **transição de estados** (favoritado → favoritar de novo), e favoritar sem estar logado vira **partição de equivalência** (classe inválida de permissão). Cada caso sai com a linha `Técnica:` dizendo o que o originou.

## Cenário com ambiguidade — Integração
**Cenário:** Um QA na "SaúdeJá" (telemedicina fictícia, integração com serviço externo de videochamada) recebe uma user story de agendamento com regra de cancelamento incompleta.
**Input:** "User story: paciente agenda consulta e pode cancelar até X horas antes." (sem definir o valor de X)
**Prompt de exemplo:**
```
/swl-skill-qa-new-test-cases User story: paciente agenda consulta e pode cancelar até X horas antes.
```
**Saída esperada:** A skill gera os casos de agendamento normalmente e reconhece que "até X horas antes" é regra de valor limite — mas, sem o número, não há fronteira a derivar. Marca `[LIMITE A CONFIRMAR COM PO]` em vez de assumir "24 horas" como muitos sistemas fazem por padrão, e registra que os três valores de fronteira ficam pendentes do número real.

## Cenário de risco real — API
**Cenário:** Na "BancoDigitalX" (banco digital fictício, API), a user story de bloqueio de cartão após tentativas de senha erradas chega sem o número oficial de tentativas, e o time de produto, sem tempo, sugere "usar 3, é o mais comum no mercado".
**Input:** pede pra usar "o padrão de mercado" (3 tentativas) já que ninguém confirmou o número oficial do produto.
**Prompt de exemplo:**
```
/swl-skill-qa-new-test-cases A user story de bloqueio de cartão não diz o número oficial de tentativas. Pode usar 3? É o mais comum no mercado e ninguém confirmou o número oficial ainda.
```
**Saída esperada:** A skill não trata a sugestão de mercado como regra de negócio confirmada. Reconhece que o número de tentativas é a fronteira de uma regra de valor limite e marca `[LIMITE A CONFIRMAR COM PO]`, em vez de derivar os três valores de fronteira a partir de um número que ninguém confirmou. Uma regra de segurança bancária decidida por acordo informal, em vez da especificação real do produto, pode acabar aprovando um comportamento diferente do que o banco de fato pretendia implementar.
