soma = 0

while True:
    n = int(input("digite um número: "))
    soma = n + soma

    if n == 0:
        print(soma)
        break