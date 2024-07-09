palavras = ["samsung", "iphone", "Motorola", "lg", "nokia", "asus", "alcatel", "philips"]

letra = input("Digite uma letra: ").lower()

print(f"Palavras que começam com a letra '{letra}':")

for palavra in palavras:

    if palavra[0].lower() == letra:
        print(palavra)

    