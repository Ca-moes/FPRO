#triangles
s1 = int(input("What's the size of side 1? "))
s2 = int(input("What's the size of side 2? "))
s3 = int(input("What's the size of side 3? "))
result = ''
bigerside = max(s1, s2, s3)


if bigerside == s1:
    if s2 + s3 < bigerside:
        result = "Not a triangle"
if bigerside == s2:
    if s1 + s3 < bigerside:
        result = "Not a triangle"
if bigerside == s3:
    if s1 + s2 < bigerside:
        result = "Not a triangle"
if (s1 == s2 == s3) and result == '':
    result = "Equilateral"
if (s1 != s2 != s3) and result == '':
    result = "Scalene"
if result == '':
    result = "Isosceles"
    

print(result)






