#Question4
#1.5 km of swimming, 40 km of cycling and, finally,
#10 km of running

tS = float(input("Enter Swimming time of completion: "))
tC = float(input("Enter Cycling time of completion: "))
tR = float(input("Enter Running time of completion: "))

#Máx time allowed (t = d / vmin)
mtS = 10/8
mtC = 40/20
mtR = 1.5/2


if (tS > mtS):
    outp = "Swimming"
elif (tC > mtC):
    outp = "Cycling"
elif (tR > mtR):
    outp = "Running"
elif ((tS + tC + tR) > 4.0):
    outp = "Time"
else:
    outp = tS + tC + tR

print(outp)