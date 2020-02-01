#sumNumbers.py
def sum_numbers(n):
   #if n <= 0:
        
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(sum_numbers(3))
    
    