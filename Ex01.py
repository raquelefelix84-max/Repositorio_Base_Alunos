# Exemplo 1-1: Hello Flask!
# crie um app flask basico que exibe "olá, mundo!" na rota principal(/)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "ola, mundo!"

app.run()