#uppercase.py


def uppercase(astring):
    cond1 = astring[0].isupper()
    cond2 = astring[1].isupper()
    cond3 = astring[2].isupper()
    if cond1 or cond2 or cond3:
        astring = astring.upper()
    return astring
