#QUESTION2

d = int(input("What's the integer d: "))
num = input("What's the integer num: ")
numtemp = int(num)
sizenum = len(num)
sum = 0

dig3 = numtemp % 10 
dig2 = (numtemp//10) % 10
dig1 = (numtemp//100) % 10


if dig1 > d:
    sum += (dig1*2)
if dig2 > d:
    sum += (dig2*2)
if dig3 > d:
    sum += (dig3*2)
    
print(sum)
