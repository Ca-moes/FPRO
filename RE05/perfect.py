#perfect.py
#a perfect number is a positive integer 
#that is equal to the sum of its proper 
#positive divisors, that is, the sum of 
#its positive divisors excluding the number 
#itself.

def is_perfect(n):
    div=[]
    sum = 0
    result = False
    if(n == 0) or (n < 0):
        result = False
    else:
        for i in range(1,n):
            if n % i == 0:
                i = int(i)
                div.append(i)
        
        for x in div:
            sum += x
        result = (sum == n)
    return result

print(is_perfect(28))