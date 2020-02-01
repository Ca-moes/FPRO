#  grades.py
# tupulo principal
# tupulos com info de 1 estudante
# 1 tupulo com 2 notas
# take second element for sort
"""

"""

def sort_grades(records):
    def takeThird(elem):
        return elem[2]

    records = list(records)
    #add index
    newlist = []
    ind = -1
    for tup in records:
        ind += 1
        tup += (ind,)
        newlist.append(tup)
    records = []
    for a in newlist:
        total = 0
        cont = 0
        for grade in a[2]:
            total += grade
            cont += 1
        media = round(total/cont,3)                
        a = a[:2] + (media,) + a[3:]
        records.append(a)
    records = sorted(records, key=takeThird, reverse=True)
    print(records)
    #organizado por notas
    #organizar por ordem alfabética caso média seja igual
    #começa avaliar primeiro, vê resto da lista 1 a 1, se a nota for igual (ver posição []) 
    #check nome
    for tup in records:
        for tup2 in records[]:


    
    """
    tsortedgrades = ()
    i=0
    for times in len(records):
        for bigtuple in records:
            i+=1
            mediabigtuple = (bigtuple[2][0] + bigtuple[2][1])/2
            for num in range(i,len(records)):
                mediaanalisys = (records[num][2][0] + records[num][2][1])/2
                if mediaanalisys > mediabituple:
     """               
                
                
        
     

print(sort_grades((('Maria', 'up20190001', (60, 70, 80)),
                   ('Maria', 'up20190002', (60, 70, 80)),
                   ('Mario', 'up20190003', (100, 10, 80)),
                   ('Rui', 'up20190004', (90, 100, 90)),
                   ('Ana', 'up20190005', (90, 100, 90)))))
    
"""
print(sort_grades((('João', 'up20186042', (90, 87)),
                   ('Ana', 'up20186040', (90, 90)),
                   ('José', 'up20186063', (70, 90)),
                   ('Ana', 'up20186061', (90, 90)),
                   ('Tiago', 'up20186070', (100, 90)))))
"""