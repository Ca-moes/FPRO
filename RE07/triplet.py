# triplet.py
def triplet(atuple):
    result = ()
    i = 0
    for a in atuple[0:len(atuple)]:
        i += 1
        for b in atuple[i:len(atuple)]:
            for c in atuple[i+2:len(atuple)]:
                if a + b + c == 0 :
                    result = (a,) + (b,) + (c,)
                    return result
    return ()

print(triplet(((-8, 0, 4, -2, -1, 1, 2))))