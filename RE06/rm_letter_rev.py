def rm_letter_rev(l, astr):
    preres = ''
    for char in astr:
        if char != l:
            preres += char 
    res = preres[::-1]
    return res
