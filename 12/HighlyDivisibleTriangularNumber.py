#https://projecteuler.net/problem=12

divisors = 1
goal = 500
currentN = 1
notfound = False
primes = []
max = 1000001
def calcFactors(triNumber):
    i = 1
    global divisors
    while(i <= (triNumber / 2)):
        if(triNumber % i == 0):
            divisors += 1
        i+= 1
    if(divisors > goal):
        global notfound
        print("Goal Reached: " + str(triNumber))

        notfound = True
    else:
        print("for: " + str(triNumber) + " : There are : " + str(divisors) + ": Factors : ")
        divisors = 1

def calcNextTriNumber():
    global currentN
    tri = 0
    for a in range(1,currentN):
        tri += a
    currentN += 1
    return tri


def calcFactors(tri):
    if(tri == 1):
        return 1
    listofPrimes = seive(tri)
    ans = 1
    dup = listofPrimes


def seive(tri):
    prime = [True for i in range(tri+1)]
    p = 2
    while(p * p <= tri):
        if(prime[p] == True):
            for i in range(p * 2, tri+1,p):
                prime[i] = False
        p +=1
    return prime




































#get number of primes

def main():
    global notfound
    while(not notfound):
        calcFactors(calcNextTriNumber())
main()
