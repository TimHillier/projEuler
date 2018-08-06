#https://projecteuler.net/problem=44
import math

currentNumbers = [1,5]
lowestD = 999999999999999
def GenPentagonNumbers(N):
    A= int(N * (3 * N - 1) / 2)
    print("put " + str(A) + " into the List")
    return A

def FindLowest(j,k):
    global lowestD
    addition = currentNumbers[j] + currentNumbers[k]
    subtraction = abs(currentNumbers[j] - currentNumbers[k])


    if(Compare(addition)):
        print("A " + str(addition))
        if(Compare(subtraction)):
            print("B " + str(currentNumbers[j] - currentNumbers[k]))
            if(subtraction < lowestD):
                print("C " + str(currentNumbers[j] - currentNumbers[k]))
                lowestD = subtraction
                print("&***********************" + str(lowestD))



def Compare(n):
    print("Looking for:" + str(n))
    if(n in currentNumbers):
        print(str(n) + " Is in the List")
        return True
    elif(n < currentNumbers[0]):
        print(str(n) + " Is to low")
        return False
    elif(n < currentNumbers[len(currentNumbers)-1]):
        print(str(n) + " is not in the list")
        return False
    elif(n > currentNumbers[len(currentNumbers)-1]):
        print(str(n) + " is bigger than list, need to look at bigger numbers")
        currentNumbers.append(GenPentagonNumbers(len(currentNumbers)+1))
        return Compare(n)
    else:
        print(str(n) + "does not work in the list")
        return False





def Main():
    for j in range(0,10000):
        for k in range(j+1,10000):
            FindLowest(j,k)
    print(lowestD)

#    for i in range(1,100):
#        print(GenPentagonNumbers(i))

Main()
#the answer is 5482660