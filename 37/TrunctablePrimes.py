#https://projecteuler.net/problem=37

TrucPrimes = []
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

def TrucNum(N):
    #deletes the end digit
    N = [str(x) for x in str(N)]
    del N[-1]
    N = ''.join(N)
    return N

def RevTrucNum(N):
    #deletes the First Digit
    N = [str(x) for x in str(N)]
    del N[0]
    N = ''.join(N)
    return N

def CheckPrimes(N):
    current = N
    for i in range(0,len(str(current))):
        if(isPrime(int(current))):
            current = TrucNum(current)
        else:
            return False
    current = N
    for i in range(0,len(str(current))):
        if(isPrime(int(current))):
            current = RevTrucNum(current)
        else:
            return False

    return True

def FindNum(UpBound):
    for i in range(10,UpBound + 1):
        for j in range(0,len(str(i))):
            if(CheckPrimes(i)):
                TrucPrimes.append(i)


def Main():
    global TrucPrimes
    FindNum(1000000)
    TrucPrimes = list(set(TrucPrimes))
    print(len(TrucPrimes))
    print(sum(TrucPrimes))

Main()