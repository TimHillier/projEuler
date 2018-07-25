#https://projecteuler.net/problem=15
import math



def choose(n,k):
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial((n-k))

    d = b*c

    e = a / d

    print('{0:.10f}'.format(e))


    return str(a/(b*c))


print(choose(40,20))