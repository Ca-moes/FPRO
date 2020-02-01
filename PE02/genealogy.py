def genealogy(l):
    l = sorted(l)
    newlist = []
    for tup in l:
        ordem = tup[1]
        if ordem == "sibling": 
            newlist.append(tup)
    for tup in l:
        ordem = tup[1]
        if ordem == "parent": 
            newlist.append(tup)
    for tup in l:
        ordem = tup[1]
        if ordem == "cousin": 
            newlist.append(tup)
    for tup in l:
        ordem = tup[1]
        if ordem == "grandparent": 
            newlist.append(tup)
    return newlist
    
    
    
    
    
    
print(genealogy([("maria", "parent"), ("matilde", "grandparent"),
("geraldes", "grandparent"), ("carlos", "sibling"),
("paulo", "sibling"), ("artur", "grandparent"),
("pedro", "parent"), ("alfredo", "cousin"), ("carla", "cousin")]))
    # sibling < parent < cousin < grandparent