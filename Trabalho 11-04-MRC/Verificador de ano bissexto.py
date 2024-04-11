#Verificador de ano bissexto

ano = int(input("Digite um ano: "))

if ano % 4==0:
    print("O ano",ano, "e bissexto")
else:
    print("O ano",ano, "não e bissexto")