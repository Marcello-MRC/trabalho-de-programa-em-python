#Numeros perfeitos

for n1 in range(2, 10000):  
    divisor = 0
    
    
    for n in range(1, n1):
        if n1 % n == 0:
            divisor += n
            
    
    if divisor == n1:
        print(n1)