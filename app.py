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

@app_nick.route('/usuario')
def dados_usuario():
    dados_usu = {"nome": "Nick", "profissao": "Estudante", "disciplina": "Desenvolvimento Web III"}
    return render_template('usuario.html', dados=dados_usu)

@app_nick.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {"nome": p_nome, "profissao": p_profissao, "disciplina": p_disciplina}
    return render_template('usuario.html', dados=dados_usu)

@app_nick.route('/login')
def login():
    return render_template('login.html')

@app_nick.route('/rota2')
def rota2():
    return render_template('rota2.html')


if __name__ == '__main__':
    app_nick.run(port=7000)