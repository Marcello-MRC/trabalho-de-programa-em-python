# Pegando o valor do produto e do desconto
V_produto = float(input("Me de o valor do produto sem o desconto: "))
Desconto = float(input("Me de a porcentagem do desconto:" ))

#calculando o valor descontado
V_descontado  = V_produto * Desconto/100

#calculando o valor final
V_final = V_produto - V_descontado

# resultado
print(" o valor descontado e: R$ ",V_descontado)
print("o valor a pagar  é de: R$ ",V_final)