#collisions.py
def hashfunction(num):
    """
    use the modulus-8 of the sum of the digits in the number. For
example, if the number is 24 then the hash is 6 (because (2 + 4) % 8 = 6)
    """
    n = num
    soma = 0 
    while n != 0:
        alg = n % 10
        soma += alg
        n = n//10
    return soma % 8

def collisions(alist):
    mydict = {}
    for i in alist:
        hashnum = hashfunction(i)
        if hashnum not in mydict:
            mydict[hashnum] = 1
        else:
            mydict[hashnum] += 1
    return mydict
        
    
print(collisions([1, 789, 100, 9807, 1208, 92, 101]))