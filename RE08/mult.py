#number of sub-list = num of lines
#lengh of one sublist  = num of columns
#Ncolumns M = Nlines N
#lengh of M = Num of sub list of N       -  to have multiplication

def mult(M, N):
    rndmlist = []
    if len(M[0]) != len(N):
        return []
    else:
        for vector in M:
            sss = []
            for i in range(0, len(N[0])):
                sum = 0
                a = 0
                for element in vector:
                    sum += element * N[a][i]
                    a += 1
                sss.append(sum)            
            rndmlist.append(sss)
            
        return rndmlist        
    
print(mult([[7, 8, 9, 10]], [[5], [3], [2], [7]]))
