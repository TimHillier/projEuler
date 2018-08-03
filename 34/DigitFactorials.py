#https://projecteuler.net/problem=34
import math

Factorials = []

def Fac(N):
    global Factorials
    L = [int(x) for x in str(N)]
    s = 0
    for i in range(0,len(L)):
        s += math.factorial(L[i])
    if(s == N):
        Factorials.append(N)


def Main():
    for i in range (3,999999):
        Fac(i)
    print(sum(Factorials))



Main()
