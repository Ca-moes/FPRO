
def flatten(alist):   
    result = []
    for element in alist:
        if type(element) is list:
            result += flatten(element)
        else:
            result.append(element)
    return result
    
    
    
print(flatten(['Hello', [2, [[], False]], [True]]))
# =============================================================================
# ['Hello',2, False, True]
# =============================================================================
