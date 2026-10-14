# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome= input("dgite seu nome:")
idade=input("digite a sua idade:")
email=input("digite o seu email:")
senha=input("digite a sua senha")


print(f"nome:{nome}")
print("f idade:{idade}")
print("f senha:{senha}")
print("-" * 30)


print(f"n\"--- usuaruio cadatrado ---")
print(f" seja bem vindo(a) {nome}!")
print(f"email: {email}")
print("-" *26)