#local_minima.py
# n = 5 --- n = 2
# analisa 2 á esquerda e 2 á direita
# pos = 0 -> analisa [1] e [2]
# pos = 1 -> analisa [0] [2] e [3]
"""
# index = numero de posiçoes que checa antes
"""
### pos = 2 -> analisa pos 0 pos 1 pos 3 pos 4

# n = 3 --- n = 1
# analisa 1 á esquerda e 1 á direita
# pos = 0 -> analisa [1]
# pos = 1 -> analisa [0] e [2]


def local_minima(alist, n):
    n = int((n-1)/2) 
    index = -1
    result = []
    for a in alist:
        temp =[]
        index += 1
        if index < n:
            for i in range(0,index):
                if a < alist[i]:
                    checkback = True
                else:
                    checkback = False
            for i in range(n):
                if a < alist[index + i]:
                    checkfront = True
                else:
                    checkfront = False
            if checkfront and checkback:
                temp.append(a)
                temp.append(index)
                result.append(temp)
            
            
    return result
    
    
print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))