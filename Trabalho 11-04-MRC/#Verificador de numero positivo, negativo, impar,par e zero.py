#Verificador de numero positivo, negativo, impar,par e zero 
numero = int(input("Digite um numero: "))

if numero > 0 and numero % 2==0:
    print("O numero",numero, "e Positivo e par.")

elif numero > 0 and numero % 3==0:
    print("O numero",numero, "e multiplo de três e Positivo.")

elif numero < 0  and numero % 2!=0:
    print("O numero",numero, "e negativo e Impar.")

elif numero == 0:
    print("Seu numero e zero.")

else:
    print("Seu numero não se encaixa no sistema, por favor refaça.")