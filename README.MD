# Projeto Flask - Controle de Versões com GitHub

Atividade da disciplina Desenvolvimento Web III (IFRO) - versionamento 
de uma aplicação Flask usando commits e branches no Git.

## Como rodar

\`\`\`bash
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
\`\`\`

## Histórico de versões

- **v1**: rotas simples com Flask (`/`, `/ola`, `/contato`, `/rota2`), retornando texto puro.
- **v2**: passa a usar `render_template` com páginas HTML na pasta `templates/`.
- **v3**: adiciona rotas com parametros na URL.
- **v4**: inicia heranca de templates, os outros htmls agora usam o base de base :p. Aqui inicia as branches também.
- **v5**: adiciona rota /login com formulario e configura flash (SECRET_KEY)