# AGENTS.md

Este repositório mantém uma coleção de skills de QA da Base2 para o Claude Code.

## Objetivo do repositório
- Fornecer skills reutilizáveis para padronizar tarefas de QA: planejamento de estratégia, geração de cenários (BDD e casos de teste), automação, massa de dados fictícia, verificações de qualidade (cobertura, flakiness, integridade de dados gerados por IA) e entrega (PR, documentação, commit).
- As skills devem funcionar como ponto de partida para qualquer projeto da organização, independente de stack ou framework de automação.

## Leia primeiro
- [README.md](README.md) para entender como o repositório é consumido e como as skills são instaladas.
- [MANIFEST.md](MANIFEST.md) para ver a lista oficial de skills, versões e convenções.

## Estrutura esperada
- Cada skill fica em `skills/<nome-da-skill>/SKILL.md`.
- O arquivo principal da skill deve conter metadados no topo (`name`, `description`, `argument-hint`, `metadata.version`) e instruções claras para o agente.
- Cada skill também deve ter um `EXAMPLES.md` na mesma pasta, com 3 exemplos no formato
  `Cenário`/`Input`/`Prompt de exemplo`/`Saída esperada`, mesmo padrão já usado nas
  skills existentes.
- O conteúdo deve ser conciso, acionável e alinhado com os padrões já usados nas skills existentes.

## Convenções importantes
- Mantenha a documentação em português, como no restante do repositório.
- Ao alterar ou adicionar uma skill, confira se o comportamento e a descrição continuam consistentes com [README.md](README.md) e [MANIFEST.md](MANIFEST.md).
- Evite duplicar documentação já existente; prefira linkar para os arquivos relevantes.
- Não introduza dependências específicas de stack se a skill for destinada a uso genérico.
- Referências a outras skills desta coleção devem usar o nome completo com prefixo (ex: `swl-skill-qa-check-coverage`), nunca a forma curta — o nome no frontmatter deve ser idêntico ao nome da pasta.
- Toda skill que envolve geração de conteúdo (dados, respostas, relatórios) deve ter uma seção `## Guardrail` explícita contra fabricação/invenção quando a informação de origem não estiver disponível.

## Quando editar arquivos
- Se a mudança afetar o uso da skill, atualize também a documentação pública e o manifest.
- Se a mudança for apenas de formato ou clareza da instrução, mantenha o restante do repositório consistente com o estilo atual.

## Duplicação intencional entre skills (não extrair)
- `swl-skill-qa-new-automation` e `swl-skill-qa-new-mobile-automation` compartilham, de propósito, texto quase idêntico em 4 pontos: a seção `Origem do cenário`, a seção `Registro no pipeline`, o bullet de dados de teste via `swl-skill-qa-new-test-data`, e o núcleo do guardrail sobre o marcador `generated-by-ai: reviewed`/`pending-review`.
- Essa duplicação foi analisada e a decisão foi **não extrair** para um arquivo compartilhado — o custo de token por chamada seria igual ou pior (a skill precisaria referenciar e ler um arquivo externo, sem redução real de conteúdo carregado), então a duplicação foi mantida por ser pequena (~85 palavras) e o custo de extração superar o ganho.
- **Se editar um desses 4 trechos em uma das duas skills, confira e replique a mudança na outra** — é o único ponto de manutenção manual que essa decisão deixou em aberto.

## Comandos e validação
- Este repositório é principalmente documentação/instruções; não há uma aplicação de runtime principal a ser executada para validar a maioria das mudanças.
- Sempre revise o diff para garantir que a mudança esteja coerente com a intenção da skill e com os arquivos de referência.
- Antes de publicar uma skill nova ou alterada, teste-a com pelo menos um cenário real e um cenário adversarial (dado ambíguo, informação faltante, entrada inválida) para confirmar que o guardrail resiste — não apenas que a saída "parece boa".
