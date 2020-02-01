mx = (('J', 'D', 'C', 'P', 'C', 'P', 'X', 'O', 'A', 'A'), 
      ('Z', 'X', 'V', 'O', 'V', 'X', 'F', 'R', 'V', 'V'), 
      ('N', 'D', 'L', 'E', 'I', 'R', 'B', 'I', 'E', 'A'), 
      ('Y', 'T', 'R', 'Q', 'O', 'M', 'O', 'I', 'I', 'O'), 
      ('F', 'Z', 'Z', 'A', 'P', 'Z', 'E', 'R', 'T', 'Q'), 
      ('X', 'A', 'U', 'E', 'O', 'E', 'O', 'O', 'T', 'O'), 
      ('P', 'O', 'R', 'T', 'U', 'O', 'A', 'Z', 'L', 'Z'), 
      ('C', 'Z', 'N', 'O', 'Q', 'U', 'P', 'U', 'O', 'P'))

def soup(matrix, word):
    for index,i in enumerate(matrix):
        for inde,j in enumerate(i):
            if j == word[0]:
                matrix[index][inde] == ""
                if check_soup(matrix,word[1:],index,inde):
                    return "{}{}".format(chr(ord("A")+index), inde+1)
                    

def check_soup(matrix,word,line,column):
    if word == "":
        return True
    else:
        for k in range(line-1,line+2):
            for l in range(column-1,column+2):
                if k>=0 and l>=0 and k<len(matrix) and l<len(matrix[0]) and word[0] == matrix[k][l]:
                    matrix[k][l] == ""
                    if check_soup(matrix,word[1:],k,l):
                        return check_soup(matrix,word[1:],k,l)
                    else:
                        continue
      
        
    
    
print(soup(mx, "AVEIRO"))
    
