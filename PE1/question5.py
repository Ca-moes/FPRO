#Question5
#base 10 to base 8
dec = int(input("Input decimal number: "))
octal = 0



for _ in range(dec):
    octal = octal + 1
    for n in (range(len(str(octal)))):
        tempoctal = octal / (10 ** n)
        if tempoctal % 10 == 8:
            octal = octal - 8 * (10 **n)
            octal = octal + 10 ** n
    print(octal)


print(octal)



