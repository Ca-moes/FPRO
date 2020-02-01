# mastermind.py
def mastermind(g1,g2,g3,c1,c2,c3):
    points = 0
    if g1 == c1:
        c1 = ''
        points += 3
    else:
        if g1 == c2:
            points += 1
        else:
            if g1 == c3:
                points += 1            
    if g2 == c2:
        c2 = ''
        points += 3
    else:
        if g2 == c1:
            points += 1
        else:
            if g2 == c3:
                points += 1                   
    if g3 == c3:
        c3 = ''
        points += 3
    else:
        if g3 == c1:
            points += 1
        else:
            if g3 == c2:
                points += 1           
    return points

print(mastermind("w", "y", "w", "b", "b", "b"))