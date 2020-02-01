def override(l1, l2):
    return sorted(list(x for x in l1 if x[0] not in (y[0] for y in l2)) + l2)     
    
print(override([('c','d'),('c','e'),('a','b'),('a', 'd')],[('a','c'),('b','d')]))
#  returns the list [('a', 'c'), ('b', 'd'), ('c','d'), ('c', 'e')]
print(override([('a','b','c','e'),('f', 'p', 'r', 'o')],[('a','c'),('b','d')]))
#  returns the list [('a', 'c'), ('b', 'd'), ('f','p', 'r', 'o')]
print(override([('a','b'),('c','d')], [('b','a'),('d','c')])) 
#  returns the list [('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c')]
