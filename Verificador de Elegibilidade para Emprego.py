#Verificador de Elegibilidade para emprego

idade = int(input("Digite sua idade: "))
nacionalidade = str(input("Digite sua nacionalidade: "))
experiencia = int(input("Digite seus anos de experiencia: "))

if idade >=18 and experiencia >=2:
    if nacionalidade == "Brasileiro" or "Brasileria":
        print("Você e legivel para esse trabalho aguarde ser chamado")

else:
    print("Infelizmente você não é legivel para esse trabalho")