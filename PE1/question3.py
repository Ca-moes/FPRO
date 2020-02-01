#Question3

#names = ["bart", "marie", "jo"]
#ages = [23, 75, 19]
names = ["mary", "john"]
ages = [13, 95]
string = ''

for i in range(len(names)):
    string += names[i] + "-" + str(ages[i]) + ' '

print(string)
