def compatible(A, B):
#    assert (len(B) == len(A[0])) or (len(A) == len(B[0])), "A and B cannot be multiplied"
#    return "A and B can be multiplied"  
    
    
    if len(B) == len(A[0]):
        return "A and B can be multiplied"
    else:
        my_error = AssertionError("A and B cannot be multiplied")
        return my_error
#        return "A and B cannot be multiplied"
#    
    
    
    
#print(compatible([[2, 2], [1, 1]], [[5, 5, 5, 5], [5, 5, 5, 5]]))
# returns the string "A and B can be multiplied"
print(compatible([[1,2,2], [1,2,2]], [[1,2,3,4], [1,2,3,4]]))
# returns the string "A and B cannot be multiplied"