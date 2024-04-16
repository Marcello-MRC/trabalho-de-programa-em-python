#Calculadora de IMC
print ("Bem vindo a calculador de IMC")

Altura = float(input("Por favor digite sua altura:"))
Peso = float(input("Por favor digite seu peso:"))

imc = (Peso/(Altura*Altura))

if imc <= 16.9:
    print ("Muito abaixo do peso",imc)

elif imc >= 17 and imc <18:    
    print("abaixo do peso",imc)

elif imc >= 19 and imc <25:
    print("Peso normal",imc)  

elif imc >= 25 and imc <29:
    print("Acima do peso",imc)

elif imc >= 30 and imc <34:
    print("Obesidade grau 1",imc)

elif imc >= 35 and imc <40:
    print("Obesidade grau 2",imc)

else:
    print("Obesidade grau 3",imc)
