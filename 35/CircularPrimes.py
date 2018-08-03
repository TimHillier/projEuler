#https://projecteuler.net/problem=35
CircPrimes = []
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False

    for i in range(3, int(n ** .5) + 1, 2):
        if (n % i == 0):
            return False
    return True

def RotateNum(N):
    digits = len(str(N))
    return int((N%10) * pow(10,digits-1) + (N/10))

def CheckPrimes(N):
    current = N
    for i in range(0,len(str(current))):
        if(isPrime(current)):
            current = RotateNum(current)
        else:
            return False
    return True

def FindNum(UpBound):
    for i in range(1,UpBound + 1):
        for j in range(0,len(str(i))):
            if(CheckPrimes(i)):
                CircPrimes.append(i)


def Main():
    global  CircPrimes
    FindNum(1000000)
    CircPrimes = list(set(CircPrimes))
    print(len(CircPrimes))

Main()


#note
#You can save the generated primes in a list and check those first
