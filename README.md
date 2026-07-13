# Processo de Qualidade com IA — Base2

Documentação das skills de QA da Base2 Tecnologia para uso com Claude Code. Site estático,
sem build step em produção — cada página é um arquivo HTML autocontido (CSS, JS e o banner
já embutidos), pronto para ser publicado em qualquer host estático.

🔗 Publicado em: `https://<seu-usuario>.github.io/<nome-do-repo>/` (após configurar o GitHub Pages, veja abaixo)

---

## Estrutura do repositório

```
.
├── index.html                  → página inicial
├── instalacao.html              → como instalar e usar as skills (com botão de download)
├── skills/
│   └── swl-skill-qa-*.html      → uma página por skill (22 no total)
├── downloads/
│   └── qa-skills-package.zip    → gerado a partir de qa-skills-package/ — não editar na mão
├── assets/
│   ├── style.css                → estilo-fonte (referência/edição)
│   ├── app.js                   → script-fonte (referência/edição)
│   └── banner_base2.png         → banner original da Base2
├── qa-skills-package/
│   └── skills/*/SKILL.md        → fonte real de cada skill (usada para gerar o site e o zip)
└── scripts/
    ├── build_data.py            → lê qa-skills-package/ e gera scripts/skills_data.json
    ├── build_downloads.py       → zipa qa-skills-package/ em downloads/qa-skills-package.zip
    ├── build_skill_pages.py     → gera skills/*.html
    ├── build_home.py            → gera index.html
    └── build_instalacao.py      → gera instalacao.html (inclui o botão de download)
```

**Importante:** os arquivos `.html` na raiz e em `skills/`, e o `downloads/qa-skills-package.zip`,
são todos **gerados** a partir de `qa-skills-package/skills/*/SKILL.md`. Se precisar mudar o
conteúdo de uma skill, edite o `SKILL.md` correspondente e rode os scripts de novo (veja
[Como atualizar o site](#como-atualizar-o-site)) em vez de editar o HTML ou o zip na mão —
a próxima geração sobrescreveria a edição manual. Isso garante que o botão de download da
página de instalação, o `git clone` do repositório e o site nunca fiquem desalinhados entre si.

A pasta `assets/` também é usada como fonte pelos scripts (eles leem `style.css`, `app.js`
e o banner de lá e embutem o conteúdo em cada página gerada). Editar esses três arquivos e
rodar os scripts é o jeito certo de mudar visual ou comportamento do site inteiro de uma vez.

---

## Publicar no GitHub Pages

1. Crie um repositório no GitHub e suba todo o conteúdo desta pasta para a raiz dele
   (branch `main`, por exemplo).
2. No repositório, vá em **Settings → Pages**.
3. Em "Source", selecione a branch `main` e a pasta `/ (root)`.
4. Salve. Em alguns minutos o site fica disponível em:
   `https://<seu-usuario>.github.io/<nome-do-repo>/`

Como cada página é autocontida, não há dependência de build step, roteador client-side
nem servidor: o GitHub Pages serve os arquivos como estão.

### URLs de cada página

- Início: `/index.html` (ou só `/`)
- Instalação: `/instalacao.html`
- Cada skill: `/skills/swl-skill-qa-<nome>.html` — por exemplo,
  `/skills/swl-skill-qa-plan-strategy.html`

---

## Como atualizar o site

Pré-requisitos: Python 3 com `markdown` e `PyYAML` instalados.

```bash
pip install markdown pyyaml
```

Depois de editar algo em `qa-skills-package/skills/*/SKILL.md` (ou em `assets/style.css`
e `assets/app.js`, se for mudar visual/comportamento), rode, a partir da pasta `scripts/`:

```bash
cd scripts
python3 build_data.py          # relê todas as SKILL.md → scripts/skills_data.json
python3 build_downloads.py     # regenera downloads/qa-skills-package.zip
python3 build_skill_pages.py   # regenera skills/*.html
python3 build_home.py          # regenera index.html
python3 build_instalacao.py    # regenera instalacao.html
```

Rode sempre nessa ordem — `build_data.py` primeiro, os demais dependem do
`skills_data.json` gerado por ele (`build_downloads.py` não depende dele, mas é mais fácil
lembrar rodando tudo em sequência).

### Adicionando uma skill nova

1. Crie a pasta `qa-skills-package/skills/swl-skill-qa-<nome>/SKILL.md`, seguindo o
   mesmo formato das demais (frontmatter `name`/`description`/`argument-hint`/
   `metadata.version`, seção `## Passos` e seção `## Guardrail`).
2. Abra `scripts/build_data.py` e adicione o novo nome de pasta em `CATEGORY_MAP`
   (define em qual categoria a skill aparece: Planejamento, Geração, Verificação,
   Diagnóstico ou Entrega) e em `TITLE_MAP` (título amigável exibido no menu e nos cards).
3. Rode os quatro scripts, na ordem acima.

### Renomeando o site

O nome exibido no título das abas, no cabeçalho e no rodapé vem de uma única constante:
`SITE_NAME`, no topo de `scripts/build_skill_pages.py`. Mude ali e rode os scripts de novo.

### Depois de criar o repositório no GitHub

O botão "Ver no GitHub" na página de instalação usa um link provisório. Assim que criar o
repositório de verdade, abra `scripts/build_instalacao.py`, troque o valor de
`GITHUB_REPO_URL` pela URL real e rode `python3 build_instalacao.py` de novo.

---

## Identidade visual

- Verde escuro `#004d3d`, verde médio `#00964f`, lima `#9edc37` — paleta oficial Base2.
- O banner (`assets/banner_base2.png`) é usado sem nenhuma alteração, em largura total.
- Tipografia: Inter (texto) + mono (rótulos, comandos e código), no estilo dos demais
  documentos técnicos da Base2.

---

*Mantido pela equipe de engenharia da Base2 Tecnologia.*
