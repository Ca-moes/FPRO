def listit(t):
    return list(map(listit, t)) if isinstance(t, (list, tuple)) else t

def calculator(expr):   
    if type(expr) is int:
        return expr
    
    expr = listit(expr)
    
    if type(expr[0]) is list:
        expr[0] = calculator(expr[0])
    if type(expr[2]) is list:
        expr[2] = calculator(expr[2])
        
    if expr[1] == '+':
        result = expr[0] + expr[2]
    if expr[1] == '-':
        result = expr[0] - expr[2]
    if expr[1] == '*':
        result = expr[0] * expr[2]
    return result
    

print(calculator(10))
# =============================================================================
# 9
# =============================================================================
# (tuple/integer, operator, tuple/integer)
# valid operators are: addition (+), subtraction (-) and multiplication (*)