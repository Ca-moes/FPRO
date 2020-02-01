#formal.py


def formal(name):
    sname = name.split()
    listtest = sname
    count = -1
    for i in sname:
        count += 1
        if i == "de" or i == "e" or i == "da" or i == "do":
            del listtest[count]
    #countava = len(listtest) - 1
    result = listtest[-1] + ", "
    del listtest[-1]
    for c in listtest:
        result += c[0] + ". "
    return(result)
    
    
print(formal("Raquel Filipa Sepúlveda Figueiredo"))