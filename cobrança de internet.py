#cobrança de interne por pulsos

internet = int(input("Digite os minutos: "))
conta = 0

if internet < 200:
    conta = 0,20 * internet 
    print("O preço da sua conta é", conta)

elif internet >= 200 and internet <= 400:
    conta = 0,18 * internet
    print("O preço da sua internet é ",conta)

elif internet > 400:
    conta = 0,15 * internet
    print("O preço da sua internet é ",conta)

