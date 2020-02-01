def exactly(s):
    lista = list(s)
    result = []
    onetimecheck = False
    for ind1,char in enumerate(lista):
        if char != "?" and char != "1" and char != "2" and char != "3" and char != "4" and char != "5" and char != "6" and char != "7" and char != "8" and char != "9":
            continue
        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
            value1 = int(char) 
#            print(value1)
            counter = 0
            for ind2 in range(ind1+1,len(lista)):
                char2 = lista[ind2]
                if char2 == "?":
                    counter += 1
                elif char2 == "1" or char2 == "2" or char2 == "3" or char2 == "4" or char2 == "5" or char2 == "6" or char2 == "7" or char2 == "8" or char2 == "9":
                    value2 = int(char2)
                    value = value1 + value2
                    if value != 10:
                        continue
                    if value == 10 and counter == 3:
                        templist = [value1, value2]
                        onetimecheck = True
                        result.append(templist)
                    elif value == 10 and counter != 3 and onetimecheck == False:
                        templist = [value1, value2] # i.e [1,2]
                        restring = ""
                        for v in templist:
                            restring += str(v)
                        retuple = (restring,)
                        returnresult = "The sequence {} is NOT OK with first violation with pair: {}".format(s, retuple)
                        return returnresult
#            print("value1: ", value1, "value2: ", value2, "n de ?: ", counter) 
            #print(value)
    restring = ""
    result2 = []
    for v in result:
        for t in v:
            restring += str(t)
        result2.append(restring)
        restring = ""
    result2 = tuple(result2)
    
    restring = "The sequence {} is OK with the pairs: {}".format(s,result2)
    
    return restring

print(exactly("htrtr24?h56h56??29004??34"))
#if char != "?" and char != "1" and char != "2" and char != "3" and char != "4" and char != "5" and char != "6" and char != "7" and char != "8" and char != "9":