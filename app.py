from flask import Flask

app_Nick = Flask(__name__)

@app_Nick.route('/')
@app_Nick.route('/ola')
def raiz():   #esta função está vinculada a rota raiz e a rota /ola
    return 'Olá, Turma 2026!'

@app_Nick.route('/contato')
def contato():
    return 'e-mail:nick.cordeirop@gmail.com'

@app_Nick.route('/rota2')
def rota2():
    resposta = "<H3>Olá, Turma 2025! </H3>" 
    resposta += "<H4> sou a rota 2 </H4>"  #concatena string com o operador += montando uma resposta em HTML
    return resposta


#esta função não está vinculado a rota, mas pode ser usada dentro de uma rota ou outra função ou invocada de fora
def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estão no AVA.
if __name__ == '__main__':  #verifica se o arquivo está sendo executado diretamente, e não importado
    app_Nick.run(port=7000)