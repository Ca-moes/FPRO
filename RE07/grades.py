def sort_grades(records):
    from statistics import mean
    aa = sorted(records, key = lambda x : x[1])
    bb = sorted(aa, key = lambda y : y[0])
    cc = sorted(bb, key = lambda z : mean(z[2]), reverse = True)
    result = tuple(cc)
    return result

print(sort_grades((('Maria', 'up20190001', (60, 70, 80)),
                   ('Maria', 'up20190002', (60, 70, 80)),
                   ('Mario', 'up20190003', (100, 10, 80)),
                   ('Rui', 'up20190004', (90, 100, 90)),
                   ('Ana', 'up20190005', (90, 100, 90)))))