#Verificador de Numeros Primos

n1 = int(input('Numero: '))
num_primo = 0

for n in range(1, (n1 + 1)):        
  if n1 % n == 0:
    num_primo += 1
    
if num_primo  == 2 :
  print('primo')
else:
  print('nao primo')