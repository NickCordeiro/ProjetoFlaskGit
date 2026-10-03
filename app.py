from flask import Flask, render_template, request

app_nick = Flask(__name__)  #cria o objeto Flask, que é a aplicação web, e define a pasta templates como pasta de templates

@app_nick.route('/')
@app_nick.route('/ola')
def raiz():   #esta função está vinculada a rota raiz e a rota /ola
              # essa função é chamada quando o usuário acessa a rota raiz ou a rota /ola e é chamada de endpoint

    #return 'Olá, Turma 2025!'
    return render_template('homepage.html')  #retorna o arquivo index.html que está na pasta templates

#veja que o id é um parâmetro da rota e faz parte da URL, e não vai confundir com a rota /ola
@app_nick.route('/ola/<id>') 
def saudacao(id):
    return render_template('homepage.html', campoNome=id)
   #retorna o arquivo homepage.html que está na pasta templates. No .html tem o campo {{campoNome}} que vai receber o valor do parâmetro id da rota


#@meu_site.route('/ola/<id>')
#def saudacao():
#    nome = request.args.get("id")
#    return render_template('homepage_nome.html', campoNome= nome) #retorna o arquivo homepage.html que está na pasta templates

@app_nick.route('/')
@app_nick.route('/index')
def index():   #esta função está vinculada a rota /index
    return render_template('index.html', nome="Turma 2025")  #retorna o arquivo index.html que está na pasta templates

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

@app_nick.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {"nome": p_nome, "profissao": p_profissao, "disciplina": p_disciplina}
    return render_template("usuario.html", dados = dados_usu)

#esta função não está vinculado a rota, mas pode ser usada dentro de uma rota ou outra função ou invocada de fora
def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estão no AVA.
if __name__ == '__main__':  #verifica se o arquivo está sendo executado diretamente, e não importado
    app_nick.run(port=7000)

   #executa caso o o arquivo seja importado, mas não é uma boa prática, pois pode gerar conflito de portas