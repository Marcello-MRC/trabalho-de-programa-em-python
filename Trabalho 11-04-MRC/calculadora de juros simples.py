#Calculadora de juros simples

V_principal = float(input("Digite o valor principal: "))
taxa_de_juros = float(input("Digite a sua taxa de juros: "))
periodo = int(input("Digite em quanto tempo precisa pagar: "))

juros = V_principal * taxa_de_juros * periodo /100 

print ("O juros a pagar e R$",juros)
