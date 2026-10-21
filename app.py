from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Rota de exemplo retornando texto simples
@app.route("/sobre")
def sobre():
    return "Esta é a página Sobre do nosso site em Flask!"

if __name__ == "__main__":
    # Roda o servidor no modo de depuração (atualiza automaticamente ao salvar)
    app.run(debug=True)


