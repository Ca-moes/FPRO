def count_exceptions(f, n1, n2):
    counter = 0
    for i in range(n1, n2+1):
        try:
            f(i)
        except Exception:
            counter += 1
        else:
            continue
    return counter
    
    
print(count_exceptions(lambda x: 1/(abs(x)-2), -5, 5))
# returns the integer 2
print(count_exceptions(lambda x: 1/0 if x > 10 else 0, 0, 50))
# returns the integer 40

