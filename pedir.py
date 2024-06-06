#pedir numeros ate que o usuario digite 0
soma = 0 
while True:
    user = int(input("Digite um numero: "))
    soma = user + soma
    if user == 0:
        print(soma)
        break