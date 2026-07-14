## Cenário direto — Web
**Cenário:** Um QA na "Lojinha Verde" (e-commerce fictício de plantas, web) gera as regras de QA pela primeira vez, a partir de uma página de wiki já existente.
**Input:** "Gera as regras de QA pra Lojinha Verde. Temos uma página de wiki com nossas convenções de teste."
**Prompt de exemplo:**
```
/swl-skill-qa-generate-rules Gera as regras de QA pra Lojinha Verde. Temos uma página de wiki com nossas convenções de teste.
```
**Saída esperada:** A skill lê o wiki e gera `padroes-teste.md`, `restricoes-teste.md` e `convencoes-teste.md` com as convenções reais documentadas (Playwright, Page Object Model, nomenclatura em português).

## Cenário com ambiguidade — API
**Cenário:** Um QA na "PagaFácil" (fintech de pagamentos fictícia, API) tem só parte do processo documentado.
**Input:** "Não temos wiki, mas o time sabe de cabeça algumas convenções. Vou te contar o que sei."
**Prompt de exemplo:**
```
/swl-skill-qa-generate-rules Não temos wiki, mas o time sabe de cabeça algumas convenções. Vou te contar o que sei.
```
**Saída esperada:** A skill conduz a entrevista curta, documenta o que foi confirmado (ferramentas de automação de API, estrutura de pastas), e para os pontos sem certeza no time (política de dados de teste) deixa marcado como "a definir" em vez de assumir um padrão genérico de mercado.

## Cenário de risco real — Integração
**Cenário:** Um QA herda o sistema legado da "RotaCerta" (logística/entregas fictícia, integração com sistemas de rastreamento de terceiros) sem nenhuma documentação de QA, e o tech lead pede pra "gerar regras baseadas no que costuma ser padrão em projetos de logística", já que ninguém mais lembra as convenções antigas.
**Input:** "Ninguém aqui sabe as convenções antigas desse projeto. Pode gerar baseado no que costuma ser padrão pra sistemas de logística?"
**Prompt de exemplo:**
```
/swl-skill-qa-generate-rules Ninguém aqui sabe as convenções antigas desse projeto. Pode gerar baseado no que costuma ser padrão pra sistemas de logística?
```
**Saída esperada:** Em vez de recorrer a um "padrão de mercado" genérico, a skill examina a estrutura real de testes já existente no código (pastas, nomenclatura usada nos arquivos) como fonte concreta. Para o que não consegue confirmar nem pela estrutura nem pela entrevista, marca "a definir" explicitamente — uma regra errada aqui não fica só registrada, ela vira instrução que a IA vai seguir automaticamente em toda tarefa futura nesse projeto.
