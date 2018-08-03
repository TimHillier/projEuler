#https://projecteuler.net/problem=38

def IsPandigital(L):
    #print(L)
    M = set(L)
    if(len(L) > 9):
        return False
    if(0 in M):
        return False
    if(len(M) == 9):
        return True
    else:
        return False

def intToString(A):
    return [int(x) for x in str(A)]

def listToInt(L):
    #print(L)
    L = map(str,L)
    A = ''.join(L)
    return int(A)


def Main():
    CurrentTotal = []
    largest = -1
    for i in range(1,30000):
        for j in range(1,1000):
            CurrentTotal += intToString(i*j)
            if(len(CurrentTotal) > 9):
                break
            if(IsPandigital(CurrentTotal)):
                if(listToInt(CurrentTotal) > largest):
                    largest = listToInt(CurrentTotal)
        CurrentTotal = []
    print(largest)


Main()
