#concatenate
n1 = float(input("What's the first number: "))
n2 = float(input("What's the second number: "))
n2alt = n2
contador = 0

while n2alt >= 1:
    n2alt = n2alt / 10
    contador += 1

n1 = n1 * 10 ** contador
result = n1 + n2
result = int(result)


    
    
    
#if n2alt % 10 != 0: