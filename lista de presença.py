presenca = []

for lista_presenca in range(1,25):
    nomes = str(input("Digite o nome de  quem veio: "))
    presenca.append(nomes)
    if nomes == "Pronto":
        presenca.remove("Pronto")
        print(presenca)
        break