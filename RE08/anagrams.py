# -*- coding: utf-8 -*-

import string

def anagrams(alist):
    slist = []
    anagrams = []
    anagram = []
    
    for i in range(len(alist)):
        slist.append(alist[i].replace(" ","").lower())
        
    abc = list(string.ascii_lowercase)
    anagbool = False
    slist = sorted(slist)
    alist = sorted(alist, key = lambda s: s.lower())
    print("slist: ", slist )
    print("alist: ", alist)

    for firstword in slist:
        if firstword == "":
            continue
        for secword in slist:
            anagbool = True
            if firstword == secword:
                continue
            elif len(firstword) != len(secword):
                continue
            else: 
                for letter in abc:
                    if firstword.count(letter) != secword.count(letter):
                        anagbool = False
            if anagbool == True:
                anagram.append(alist[slist.index(secword)])
                alist[slist.index(secword)] = ""
                slist[slist.index(secword)] = ""
        
        if anagbool == True:
            anagram.append(alist[slist.index(firstword)])
            anagram.sort()
            anagrams.append(anagram)
            
        anagram = []
        
    return anagrams

print(anagrams(["they see", "eat", "The eyes", "car has", "ate", "acrash", "tea"]))
#  [['a crash', 'car has'], ['ate','eat', 'tea'], ['The eyes', 'they see']]
