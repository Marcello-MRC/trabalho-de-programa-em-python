lado1 = input("Primeiro lado: ")
lado2 = input("Segundo lado: ")
lado3 = input("Terceiro lado: ")

#Verificando se é um triangulo

if (lado1 + lado2 <lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print("Não e um triangulo")

elif (lado1==lado2) and (lado1==lado3):
    print("É um triangulo equilatero")

elif (lado1==lado2) or (lado1==lado3) or (lado2==lado3):
    print("É um triangulo isósceles")

else:
    print("É um triangulo escaleno")