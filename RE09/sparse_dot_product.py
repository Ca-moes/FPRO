#sparse_dot_product.py
def sparse_dot_product(dict1, dict2):
    result = 0
    for key1 in dict1:
        for key2 in dict2:
            if key1 == key2:
                 result += dict1[key1] * dict2[key2]
    return result
    
print(sparse_dot_product({2: 90, 9: 80, 1: -5, 8: 7}, {2: -4, 9: 1, 1: 6}))
