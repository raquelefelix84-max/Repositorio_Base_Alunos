# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------



#definir a funcao que calcule o desconto
def calcular_deconto(preco,porcentagem):
 return preco * (porcentagem / 100)
    
preco_produto = float(input("qual o preco do produto "))
porcentagem_desconto = float(input("qual a porcentagem de desconto"))

valor_desconto =calcular_deconto(preco_produto, porcentagem_desconto)

print(f"preco original:R${preco_produto:.2f} | desconto aplicado: R${desconto_produto:.2f}")

      
      
      
      
      
      