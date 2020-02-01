# palindrome.py
#    >>> line = '1234567890'
#    >>> n = 2
#    >>> [line[i:i+n] for i in range(0, len(line), n)]
# ['12', '34', '56', '78', '90']
#
# [0:2] [n,n+2] até [n+2 = len(astring)]
# [0:3] [n,n+3] até [n+3 = len(astring)]
        

def palindrome(astring):
    counter = 0
    for i in range(len(astring) - 1):  #avalia de comprimento 2 até comprimento string
        i += 2
        for n in range(len(astring) - (i-1)):  #dentro de um comprimento, pega sucessivamente numa string desse comp e avalia
            test = astring[n:n+i]
            if test[::-1] == test:
                counter += 1
    return "For string " + """'""" + astring + """': """ + str(counter) + " palindrome substrings" 
    
print(palindrome("geek"))