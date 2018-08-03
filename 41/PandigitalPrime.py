#https://projecteuler.net/problem=41

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

def IsPandigital(L):
    #print(L)
    M = set(L)
    if(0 in M):
        return False
    if(len(M) == len(L)):
        for i in range(1,len(L)+1):
            if(i not in L):
                return False
        return True
    else:
        return False


def LargestPanPrime():
    Largest = -1
    running = True
    #for i in range(123456789,98765431):
    i = 9876541
    while(running):
        #print(i)
        a = [int(x) for x in str(i)]
        if(IsPandigital(a)):
            if(isPrime(i)):
                if(i > Largest):
                    Largest = i
                    running = False
        i -=1
    return Largest


def Main():
   print("Largest: "+ str(LargestPanPrime()))


Main()