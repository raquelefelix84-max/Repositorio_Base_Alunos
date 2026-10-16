# Exercicio 1-2:Rota personalizada
# Adicione uma nova rota /

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "ola mundo!"

@app.route('sobre')
def sobre():
    return "oii sou eu sendo eu"

@app.route("ola/<nome>")
def ola(nome):
    return f"ola{nome}seja bem vindo(a)"

@app.route("/dobro/numero <int:numero")
def dobro{numero}:
    return f"o dobro de {numero} é {numero*2}"

if __name__=="__main__":
     app.run(debug=True)