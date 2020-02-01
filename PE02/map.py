def map(pos, steps):
    pos=list(pos)
    steps = steps.split("-")
    for step in steps:
        if step == "up":
            pos[1] = pos[1]+1
        elif step == "down":
            pos[1] = pos[1]-1
        elif step == "right":
            pos[0] = pos[0]+1
        elif step == "left":
            pos[0] = pos[0]-1
    pos = tuple(pos)
    return pos
    
    
    
 
    
    
print(map((0,4),"up-up-left-right-up-up"))
#map((0,0), "up-up-left-right-up-up") returns the tuple: (0,4)