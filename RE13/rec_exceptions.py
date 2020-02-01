def rec_exceptions(l):
    result=[]
    
    for x in l:
        try:
            x()
        except Exception as ex:
            result.append(ex)
        else:
            result+=rec_exceptions(x())
    return result
    
    
    
    
    
    
print(rec_exceptions([lambda: 1/0]))
#   returns the list [ZeroDivisionError('division by zero',)]
print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), lambda:''[2]], lambda: [1,2,3][4], lambda: [lambda: [lambda: 1/0]]]))
"""
returns the list [ValueError('-1 is not in list',), IndexError('string
index out of range',), IndexError('list index out of range',),
ZeroDivisionError('division by zero',)]
"""