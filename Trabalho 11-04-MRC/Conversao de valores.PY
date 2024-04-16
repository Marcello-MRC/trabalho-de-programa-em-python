#Conversão de valores

num1 = float(input("Digite seu numero:"))
distancia =int(input("Digite sua distancia,1 para milhas,2 para polegadas,3 para pés,4 para centímetros,5 para metros,6 para quilômetros. "))
conversao = int(input("Digite a distancia para converter,1 para milhas,2 para polegadas,3 para pés,4 para centímetros,5 para metros,6 para quilômetros."))

if distancia== 1 and conversao == 2:
    print("O calculo de milhas para polegadas e", num1*63360)

elif distancia == 1 and conversao == 1:
    print("Você nao pode calcular milha por milha")

elif distancia == 1 and conversao == 3:
    print("O calculo de milhas para pés é", num1*5280)

elif distancia == 1 and conversao == 4:
    print("O calculo de milhas para centimetros é", num1*160900)

elif distancia == 1 and conversao == 5:
    print("O calculo de milhas para metros é", num1*1609)

elif distancia == 1 and conversao == 6:
    print("O calculo de milhas para quilometros é", num1*1.609)

elif distancia == 2 and conversao == 1:
    print("O calculo de polegadas para milhas é", num1/63360)

elif distancia == 2 and conversao == 2:
    print("Você nao pode calcular polegada para polegada")

elif distancia == 2 and conversao == 3:
    print("O calculo de polegadas para pés é", num1/12)

elif distancia == 2 and conversao == 4:
    print("O calulo de polegadas para centimetros é", num1*2.54)

elif distancia == 2 and conversao == 5:
    print("O calculo de polegadas para metros é", num1/39.37)

elif distancia == 2 and conversao == 6:
    print("O calculode de polegadas para quilometros e", num1/39370)

elif distancia == 3 and conversao == 1:
    print("O calculo de pés para milhas é", num1/5280)

elif distancia == 3 and conversao == 2:
    print("O calculo de pés para polegadas é", num1*12)

elif distancia == 3 and conversao == 3:
    print("Você nao pode calcula pés para pés")

elif distancia == 3 and conversao == 4:
    print("O seu calculo de pés para centimetros é", num1*30.48)

elif distancia == 3 and conversao == 5:
    print("O seu calculo de pés para metros é", num1/3.281)

elif distancia == 3 and conversao == 6:
    print("O seu calculo de pés para quilometros", num1/3281)

elif distancia == 4 and conversao == 1:
    print("O seu calculo de centimetros para milhas é", num1/160900)

elif distancia == 4 and conversao == 2:
    print("O seu calculo de  centimetros para polegadas é", num1/2.54)

elif distancia == 4 and conversao == 3:
    print("O seu calculo de centimetros para pés", num1/30.48)

elif distancia == 4 and conversao == 4:
    print("Não pode calcular centimetros para centimetros")

elif distancia == 4 and conversao == 5:
    print("O seu calculo de centimetros para metros", num1/100)

elif distancia == 4 and conversao == 6:
    print('O seu calculo de centimetros para quilometros é', num1/100000)

elif distancia == 5 and conversao == 1:
    print("O seu calculo de metros para milhas é", num1/1609)

elif distancia == 5 and conversao == 2:
    print("O seu calculo de metro para polegadas é", num1*39.37)

elif distancia == 5 and conversao == 3:
    print("O seu calculo de metro para pés é", num1*3.281)

elif distancia == 5 and conversao == 4:
    print("O seu calculo de metro para centimetros é", num1*100)

elif distancia == 5 and conversao == 5:
    print("Não pode calcular metro por metro")

elif distancia == 5 and conversao == 6:
    print("O seu calculo de metro para quilometros é", num1/1000)

elif distancia == 6 and conversao == 1:
    print("O seu calculo de quilometros para milhas é",num1/1.609)

elif distancia == 6 and conversao == 2:
    print("O seu calculo de quiometros para polegadas é", num1*39370)

elif distancia == 6 and conversao == 3:
    print("O se calculo de quilometros para pés é", num1*3281)

elif distancia == 6 and conversao == 4:
    print("O seu calculo de quilometros para centimetros é", num1*100000)

elif distancia == 6 and conversao == 5:
    print("O seu calculo de quilometro para metro é", num1*1000)

elif distancia == 6 and conversao == 6:
    print("Você nao pode calcular quilometro para quilometro")

else:
    print("Refaça,pois você fez algo de errado")
