#https://projecteuler.net/problem=7
#trying to Algo from http://m-hikari.com/ams/ams-2012/ams-73-76-2012/kaddouraAMS73-76-2012.pdf
#all this fancy stuff is cool but in the end I just brute forced it. 
#im leaving it for curioty sake
import math

def S(x):
    A =  ((S1(x) + S2(x)) / 2)
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

def pi(x):
   sum = 0
   for i in range(7,x):
       sum = sum +math.floor(S(i))

   return sum + 4

def FindPrime(num):
    k = int(2*(math.floor(num * math.log(num))+1))
    #do sum
    sum = 0
    for x in range(7,k):
        sum = sum + math.floor((2 * num) / (pi(x) + num + 1))


    return sum + 7

#i gave up and just forced it.
def ForceFindPrime(number):
    primes = [2,3]
    i = 4
    count = len(primes)
    while(count < number):
        if(isPrime(i,primes)):
            primes.append(i)
            count += 1
        i+=1
    print(primes[len(primes)-1])

def isPrime(a,l):
    for x in range(0,len(l)):
        if(a > l[x]):
            if(a % l[x] == 0):
                return False
    return True
ForceFindPrime(10001)
