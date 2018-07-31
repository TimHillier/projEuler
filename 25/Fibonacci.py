#https://projecteuler.net/problem=25

oldfib = [-1] * 3
oldfib[0] = 0
oldfib[1] = oldfib[2] = 1


def fib(n):
    while len(oldfib) < n + 1:
        oldfib.append(0)
    if(n <= 1):
        return n
    else:
        if(oldfib[n-1]==0):
            oldfib[n-1] = fib(n-1)

        if(oldfib[n-2]==0):
            oldfib[n-2] = fib(n-2)

        oldfib[n] = oldfib[n-2] + oldfib[n-1]
    return oldfib[n]


def Solve(length):
    a = 9
    while(len(str(fib(a))) < length):
        a+=1
    print(a)


Solve(1000)
