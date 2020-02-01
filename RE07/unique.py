#unique.py
#atuple=(8, 8, 1, 3, 1, 3, 5)  -> tuple (1, 3, 5, 8)
#atuple=(1, 1, 1, 1)  -> (1,)
# sort first tupple
# run one on one
# check, run one on one result tupple - if value is not on result tuple, add
def unique(atuple):


    temptuple = ()
    count = 0
    for a in atuple:
        for b in temptuple:
            if a == b:
                count += 1
        if count == 0:
            temptuple += (a,)
        count = 0 
    return tuple(sorted(temptuple))
print(unique((8, 8, 1, 3, 1, 3, 5)))            