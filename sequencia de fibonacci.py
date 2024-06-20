num_termos = int(input("quantos termos voce quer: "))
n1 = 0 
n2 = 1 
contador = 0  

while contador < num_termos:
    print(n1)
    n = n1 + n2
    n1 = n2 
    n2 = n
    contador += 1