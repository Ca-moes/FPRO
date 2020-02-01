# int n
# result = TRUE or FALSE

n = int(input("Integer n: "))
result = True

if n < 2:
    result = False
else:
    for i in range(2,n):
        if n % i == 0:
            result = False
            break

print(result)