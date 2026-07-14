## Cenário direto — Web
**Cenário:** QA júnior na "EstudaMais" (plataforma de cursos online fictícia, web) audita a página de listagem de cursos, com axe-core já configurado.
**Input:** "Audita a acessibilidade da página de listagem de cursos, nível AA, já usamos axe-core no projeto."
**Saída esperada:** A skill detecta axe-core, roda contra a página, e reporta violações reais encontradas (ex: contraste insuficiente em um botão) com critério WCAG e severidade.

## Cenário com ambiguidade — Mobile
**Cenário:** QA pleno no app "PetAmigo" (adoção de pets fictícia, mobile) precisa auditar a tela de cadastro de pet, mas o nível WCAG alvo não foi confirmado.
**Input:** "Audita a acessibilidade da tela de cadastro de pet." (sem dizer o nível)
**Saída esperada:** A skill pergunta qual nível é o alvo (A, AA ou AAA) em vez de assumir AA por padrão, e só roda a auditoria depois de confirmado.

## Cenário de risco real — Mobile
**Cenário:** No app "SaúdeJá" (telemedicina fictícia, mobile), o time de produto pede pra "declarar conforme AA" no app inteiro com base só na auditoria feita na tela de login, pra atender um requisito de licitação pública.
**Input:** "Auditamos só a tela de login e passou. Pode declarar o app inteiro conforme AA pra gente anexar na licitação?"
**Saída esperada:** A skill relata a conformidade só para a tela de login efetivamente testada, sem estender a conclusão pro "app inteiro" — telas de agendamento, prontuário e pagamento nunca passaram pela ferramenta. Uma declaração assim, anexada numa licitação pública, vira uma promessa que alguém vai cobrar depois: no dia em que um usuário de leitor de tela não conseguir passar da tela de prontuário.
