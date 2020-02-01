def listit(t):
    return list(map(listit, t)) if isinstance(t, (list, tuple)) else t
  
def ctol(coord):
    ctldict1 = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F"}
    ctldict2 = {0:"1", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6"}
    result = "{}{}".format(ctldict1[coord[0]], ctldict2[coord[1]])
    return result

def findword(matrix, line, col, word):
    word = word[1:]
    lettertofind = word[:1]
    if word == "":
        return True
    else:  
        if line-1 >= 0 and line-1 <= 5 and col >= 0 and col <=5:
            """Verifica valor de cima"""
            if matrix[line-1][col] == lettertofind:
                return findword(matrix, line-1, col, word)
            
        if line+1 >= 0 and line+1 <= 5 and col >= 0 and col <=5:        
            if matrix[line+1][col] == lettertofind:
                return findword(matrix, line+1, col, word)
            
        if line >= 0 and line <= 5 and col-1 >= 0 and col-1 <=5:        
            if matrix[line][col-1] == lettertofind:         
                return findword(matrix, line, col-1, word)
            
        if line >= 0 and line <= 5 and col+1 >= 0 and col+1 <=5:        
            if matrix[line][col+1] == lettertofind:
                return findword(matrix, line, col+1, word)
            
        if line-1 >= 0 and line-1 <= 5 and col-1 >= 0 and col-1 <=5:        
            if matrix[line-1][col-1] == lettertofind:
                return findword(matrix, line-1, col-1, word)
            
        if line+1 >= 0 and line+1 <= 5 and col+1 >= 0 and col+1 <=5:        
            if matrix[line+1][col+1] == lettertofind:
                return findword(matrix, line+1, col+1, word)    
            
        if line-1 >= 0 and line-1 <= 5 and col+1 >= 0 and col+1 <=5:        
            if matrix[line-1][col+1] == lettertofind:
                return findword(matrix, line-1, col+1, word)
            
        if line+1 >= 0 and line+1 <= 5 and col-1 >= 0 and col-1 <=5:        
            if matrix[line+1][col-1] == lettertofind:    
                return findword(matrix, line+1, col-1, word)
                

def soup(matrix, word):
    listplaces = []
    matrix = listit(matrix)
    letra = word[0]
    
    for indline, line in enumerate(matrix):
        print(line)
        for indvalue, value in enumerate(line):
            if value == letra:
                newtuple = (indline, indvalue)
                listplaces.append(newtuple)   
    for coord in listplaces:
        if findword(matrix, coord[0], coord[1], word):
            return ctol(coord)

        

    
    
    
mx = (('X', 'A', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'), ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z'))
print(soup(mx, 'PORTO'))
# =============================================================================
# "C2"
# =============================================================================

#def checkround(coord, word):
# =============================================================================
#    my coordenates are (n,n)
#    I need to check 8 spots:
#    sides:
#        - (n-1,n)  up
#        - (n+1,n)  down
#        - (n,n-1)  left
#        - (n,n+1)  right
#    diag:
#        - (n-1,n-1)  top left
#        - (n+1,n+1)  top right
#        - (n-1,n+1)  bottom left
#        - (n+1,n-1)  bottom right
# =============================================================================
    