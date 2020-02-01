#isomorphic.py
#se value 1 = value 2 <--- dá "erro
#se key 1 = key 2, value 1 tem de ser igual a value 2, senão dá "erro

def isomorphic(astring1, astring2):
    keydict = {}
#    keydict[astring1[0]] = astring2[0]
#    print(keydict)
    if len(astring1) == 2:
        keydict[astring1[0]] = astring2[0]        
        keydict[astring1[1]] = astring2[0]
        if keydict[astring1[0]] == keydict[astring1[1]]:
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
    for index1, char1 in enumerate(astring1):
#        print(char1)
        if char1 in keydict and keydict[char1] != "" and keydict[char1] != astring2[index1]:
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
        keydict[char1] = astring2[index1]
    result = list(keydict.items())   
#    print(keydict.items())
#    print(keydict)
#    print(keydict.values())
#    print(set(keydict.values()))
    if len(keydict.values()) != len(set(keydict.values())):
        return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
    return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1, astring2, result)
        
    
    
    
    
print(isomorphic("foo", "bar"))
print(isomorphic("bar", "foo")) 