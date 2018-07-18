#https://projecteuler.net/problem=10


def PrimeSum(number):
    primes = [2,3]
    i = 4
    while(i < number):
        if(isPrime(i)):
            primes.append(i)
        i+=1
        print(i)
    summ = 0
    for i in range(0,len(primes)):
        print(primes[i])
        summ += primes[i]
    print(summ)

def isPrime(n):
        if n == 2:
            return True
        if n == 3: 
            return True
        if n%2 == 0:
            return False
        if n%3 == 0: 
            return False

        i =5
        w = 2

        while i * i <= n:
            if n % i == 0:
                return False
            i +=w
            w = 6 - w
        return True


PrimeSum(2000000)




    
