#count.py



def capitalize_nth(s, n):
        return s[:n].lower() + s[n:].capitalize()
    
def count(word, phrase):
    
    counter = 0
    phraselist = phrase.split()
    word = word.lower()
    for palavra in phraselist:
        if palavra == word:
            counter += 1
    
    for i in range(len(word)):
        i += 1
        for n in range(len(word) - (i - 1)):
            test = word[n:i].capitalize()
            for palavra in phraselist:
                if test == palavra:
                    counter += 1
    return counter
"""
    counter = 0
    wordupper = word.upper()
    wordlower = word.lower()
    
    
    
    words = phrase.split()
    for palavra in words:
        if palavra == word or palavra == wordupper or palavra == wordlower:
            counter += 1
"""

    

print(count("can", "He can can a can better than a canner can can a can"))
"""

for i in range(len(astring) - 1):  #avalia de comprimento 2 até comprimento string
        i += 2
        for n in range(len(astring) - (i-1)):  #dentro de um comprimento, pega sucessivamente numa string desse comp e avalia
            test = astring[n:n+i]
            if test[::-1] == test:
                counter += 1
                
"""