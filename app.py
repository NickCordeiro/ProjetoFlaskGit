from flask import Flask, render_template

app_nick = Flask(__name__)

@app_nick.route('/')
@app_nick.route('/ola')
def raiz():   #esta função está vinculada a rota raiz e a rota /ola
    #return 'Olá, Turma 2025!'
    return render_template('homepage.html')  #retorna o arquivo index.html que está na pasta templates

@app_nick.route('/index')
def index():   #esta função está vinculada a rota /index
    return render_template('index.html')  #retorna o arquivo index.html que está na pasta templates

@app_nick.route('/contato')
def contato():
    #return 'e-mail:mariela@ifro.edu.br'
    return render_template('contato.html')  #retorna o arquivo contato.html que está na pasta templates

@app_nick.route('/usuario')
def dados_usuario():
    #nome_usuario="Mariela"
    dados_usu = {"nome": "Nick", "profissao": "Estudante", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar


#esta função não está vinculado a rota, mas pode ser usada dentro de uma rota ou outra função ou invocada de fora
def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estão no AVA.
if __name__ == '__main__':  #verifica se o arquivo está sendo executado diretamente, e não importado
    app_nick.run(port=7000)

app_nick.run( port=6000)    #executa caso o o arquivo seja importado, mas não é uma boa prática, pois pode gerar conflito de portas