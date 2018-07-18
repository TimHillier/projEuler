#https://projecteuler.net/problem=7
# trying to implement this paper:
# http://m-hikari.com/ams/ams-2012/ams-73-76-2012/kaddouraAMS73-76-2012.pdf
import math
def findPrime(num):
    
    #step 1
    k = (num -1) / 6
    run = True 
    while(run):

        #step 2
        m = (6 * k) + 1
        #step 3
        if(S(m) == 1):
        #go to step 8
            run = False
        #step 4
        m = 6*k+5
        #step 5
        if(S(m) == 1):
        #go to step 8
            run = False
        #step 6
        k = k + 1

        #step 7
        #go to step 2

    #step 8
    print(m)


def S(x):
    A =  ((S1(x) + S2(x)) / 2)
    print(A)
    return A

def S1(x):
    A = int((math.floor(math.floor(math.sqrt(x))/6)))
    sum = 0
    for k in range(1,A+1):
        sum += math.floor(math.floor(x/(6*k+1))-(x/(6*k+1)))

    return ((-1) /(A + 1)) * sum
    
    
def S2(x):
    A = int((math.floor(math.floor(math.sqrt(x))/6)))
    sum = 0
    for k in range(1,A+1):
        sum += math.floor(math.floor(x/(6*k-1))-(x/(6*k-1)))


    return ((-1) /(A + 1)) * sum
    
findPrime(3)
