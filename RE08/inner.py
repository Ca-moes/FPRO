def inner(u, v):
    result = 0
    for a in range(0, len(u)):
        result += u[a] * v[a]
    return result


print(inner([], []))
