#anagrams.py
def anagrams(alist):
    strituple = []
    mainstring = []
    for index,i in enumerate(alist):
        a = i.lower()
        a = ''.join(sorted(a))
        a = a.replace(" ", "")
        newtup = (a, index)
        strituple.append(newtup)
    for index,i in enumerate(alist):
        newtup = (i, index)
        mainstring.append(newtup)
    print(strituple)
    print(mainstring)
    grandlist = []
    for a in range(0, len(strituple)):
        templist = []
        for b in range(a+1, len(strituple)):
            if strituple[a][0] == strituple[b][0]:
                templist.append(strituple[a][1]) 
                templist.append(strituple[b][1])     
        grandlist.append(templist)
    print(grandlist)
    for index,a in enumerate(grandlist):
        print("index ", index, "ele: ",a)
        if a == []:
            del grandlist[index]
    print(grandlist)

    
    
    
    
    
print(anagrams(["they see", "eat", "The eyes", "car has", "ate", "acrash", "tea"]))
# [ ['a crash', 'car has'], ['ate','eat', 'tea'], ['The eyes', 'they see'] ]

#print(anagrams(["sentence", "lives", "ten scene", "bat", "Elvis", "CE sennet"]))
# : [['bat'], ['CE sennet', 'sentence','ten scene'], ['Elvis', 'lives']]
