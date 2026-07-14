## Cenário direto — Mobile
**Cenário:** QA júnior no app mobile "PetAmigo" (adoção de pets fictícia) recebe uma user story simples de favoritar um pet.
**Input:** "User story: como usuário, quero favoritar um pet pra ver depois na minha lista."
**Saída esperada:** A skill gera casos de happy path (favoritar e ver na lista), edge case (favoritar o mesmo pet duas vezes) e negativo (favoritar sem estar logado).

## Cenário com ambiguidade — Integração
**Cenário:** QA pleno na "SaúdeJá" (telemedicina fictícia, integração com serviço externo de videochamada) recebe uma user story de agendamento com regra de cancelamento incompleta.
**Input:** "User story: paciente agenda consulta e pode cancelar até X horas antes." (sem definir o valor de X)
**Saída esperada:** A skill gera os casos de agendamento normalmente, e no caso de cancelamento marca o prazo como `[REGRA A CONFIRMAR COM PO]`, em vez de assumir "24 horas" como muitos sistemas fazem por padrão.

## Cenário de risco real — API
**Cenário:** Na "BancoDigitalX" (banco digital fictício, API), a user story de bloqueio de cartão após tentativas de senha erradas chega sem o número oficial de tentativas, e o time de produto, sem tempo, sugere "usar 3, é o mais comum no mercado".
**Input:** pede pra usar "o padrão de mercado" (3 tentativas) já que ninguém confirmou o número oficial do produto.
**Saída esperada:** A skill não trata a sugestão de mercado como regra de negócio confirmada — gera o caso de teste com o número de tentativas marcado como pendência de confirmação. Uma regra de segurança bancária decidida por acordo informal, em vez da especificação real do produto, pode acabar aprovando um comportamento diferente do que o banco de fato pretendia implementar.
