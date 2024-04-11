#Conversor de notas em conceito
nota = float(input("Digite sua nota: "))

if nota >=9:
    print("Sua nota e A")
elif nota >=7.5:
    print("Sua nota e B")
elif nota >=6:
    print("Sua nota e C")
elif nota >=4:
    print("Sua nota e D")
else:
    print("Sua nota e F")