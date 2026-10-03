from flask import Flask, render_template, request, flash, redirect

app_nick = Flask(__name__)
app_nick.config['SECRET_KEY'] = "palavra-secreta-IFRO"

@app_nick.route('/')
@app_nick.route('/index')
def index():
    return render_template('index.html', nome="Turma 2025")

@app_nick.route('/ola/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', campoNome=id)

@app_nick.route('/contato')
def contato():
    return render_template('contato.html')

# rota /usuario COM passagem de argumentos
@app_nick.route("/usuario/<nome_usuario>;<nome_profissao>")
# rota /usuario SEM passagem de argumentos --> define valor padrão com defaults
@app_nick.route("/usuario", defaults={"nome_usuario": "usuário?", "nome_profissao": ""})
def dados_usuario(nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina": "Desenvolvimento Web III"}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usu)

@app_nick.route('/login')
def login():
    return render_template('login.html')

@app_nick.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')

    if usuario == "admin" and senha == "ifro":
        return f"Usuário {usuario} autenticado com sucesso!"
    else:
        flash("Usuário ou senha inválidos!")
        return redirect('/login')

@app_nick.route('/rota2')
def rota2():
    return render_template('rota2.html')


if __name__ == '__main__':
    app_nick.run(port=7000)