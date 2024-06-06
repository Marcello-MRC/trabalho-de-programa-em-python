#repetição de enquanto nao digitar 10 numeros em repetição
numero1 = 0
soma = 0
while numero1 < 10:
    n = int(input("Digite um numero: "))
    soma = n + soma
    numero1 = numero1 + 1
print(soma)
