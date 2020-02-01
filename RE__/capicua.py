#palindrome integers
num = int(input("Write a number: "))
counternum = num
worknum = num
result0 = 0
counter = 0


#contador de tamanho
while counternum >= 1:
    counternum = counternum / 10
    counter += 1
#escreve numero reverse
for i in range(counter,0,-1):
    digit = worknum % 10
    result0 += digit * (10**i)
    worknum = worknum // 10
result0 = int(result0 / 10)

if result0 == num:
    result = "%d is a palindrome" %num
else:
    result = "%d is not a palindrome" %num



