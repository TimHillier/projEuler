#https://projecteuler.net/problem=16
import math

def digiSum(power):
    s = math.pow(2,power)
    numberString = [int(d) for d in '{0:.10f}'.format(s) if d.isdigit()]
    finalSum = 0
    for d in range(0,len(numberString)):
        finalSum += numberString[d]
    print(finalSum)

digiSum(1000)