

## Histórico de versões

- **v1**: rotas simples com Flask (`/`, `/ola`, `/contato`, `/rota2`), retornando texto puro.
- **v2**: passa a usar `render_template` com páginas HTML na pasta `templates/`.
- **v3**: adiciona rotas com parametros na URL.
- **v4**: inicia heranca de templates, os outros htmls agora usam o base de base :p. Aqui inicia as branches também.
- **v5**: adiciona rota `/login` com formulario e configura flash (SECRET_KEY)
- **v6**: adiciona rota `/autenticar` tratando POST com flash

# Projeto Flask - Controle de Versões com GitHub

Atividade da disciplina Desenvolvimento Web III (IFRO) — versionamento de uma 
aplicação Flask usando commits e branches no Git, em vez de arquivos separados 
por versão.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
```

Acesse `http://127.0.0.1:7000` no navegador.

## Branches

- **master**: versões iniciais do projeto (v1 a v3), com rotas simples e uso 
  básico de `render_template`.
- **t-template**: a partir da versão que introduz herança de templates 
  (aula 6), continuando com login, autenticação e JavaScript.

## Histórico de versões (commits)

### Branch `master`

1. **v1 — Rotas simples**: rotas `/`, `/ola`, `/contato` e `/rota2` retornando 
   texto/HTML puro, sem uso de templates.
2. **v2 — Uso de `render_template`**: as rotas passam a retornar páginas HTML 
   da pasta `templates/` (`homepage.html`, `index.html`, `contato.html`, 
   `usuario.html`, `rota2.html`).
3. **v3 — Parâmetros de rota**: adiciona `/ola/<id>` (parâmetro simples na 
   URL) e `/usuario/<p_nome>/<p_profissao>/<p_disciplina>` (múltiplos 
   parâmetros).

### Branch `t-template`

4. **v4 — Herança de templates**: usando o base de base :p com o {% extends 'base.html' %}.
5. **v5 — Login**: adiciona a rota `/login` com formulário.
6. **v6 — Autenticação com flash**: adiciona a rota `/autenticar` tratando o 
   POST do formulário, validando usuário/senha e exibindo mensagens de erro 
   com `flash`.
7. **v7 —JavaScript**: a rota `/usuario` passa a aceitar valores 
   padrão; a página de login passa a usar JavaScript (`forms.js`).

