def raise_exception(alist, value):
    result = []
    for i in alist:
        if i > value:
            continue
        else:
            my_error = ValueError('{0} is not greater than {1}'.format(i, value)) 
            result.append(my_error)
    return result
    
    
    
    
    
    
    
    
    
    
print(raise_exception([1, -2, 3, 0], 3))
"""
returns the list [ValueError('1 is not greater than 3',), ValueError('-2 is not greater than 3',),
ValueError('3 is not greater than 3',), ValueError('0 is not
greater than 3',)]
"""
print(raise_exception([3], 2))
#  returns the list []

    
    
    
    
    