#Fizz buzz
# result

result = ''
n = int(input("Integer n: "))
for i in range (1, n+1):
    if (i % 3 == 0) and (i % 5 == 0):
        result += str(i) + ' '
    elif i % 3 == 0:
        result += "Fizz "
    elif i % 5 == 0:
        result += "Buzz "
    else:
        result += str(i) + ' '
        