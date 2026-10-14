# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


produto= input("produto:")
preco= float(input("preco:"))
desconto_porcentagem = float(input("porcentagem de desconto:"))


valor_desconto= preco * (desconto_porcentagem / 100)
preco_final= preco - valor_desconto

print(f"o {produto} com {desconto_porcentagem}% de deconto custara R$ {preco_final:1f}")

