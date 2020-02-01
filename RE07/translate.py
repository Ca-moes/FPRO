#translate.py

def translate(astring, table):
    restring = ""
    letter = ""
    for i in astring:
        for a in table:
            if i == a[0]:
                letter = a[1]
        if letter != "":
            restring += str(letter)
        else:
            restring += i 
        letter = ""
    
    return restring


    
