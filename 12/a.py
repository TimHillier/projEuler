divisors = 1
goal = 500
currentN = 1
currentTri = 0
notfound = False
import sys,math
def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(math.sqrt(n))+1)
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1            
    return primes

def condense(L):
  prime,count,factors=0,0,[]
  for x in L:
    if x == prime:
      count = count + 1
    else:
      if prime != 0:
        factors.append(count)
      prime,count=x,1
  factors.append(count)
  return factors

def calcNextTriNumber():
    global currentN
    tri = 0
    for a in range(1,currentN):
        tri += a
    currentN += 1
    global currentTri
    currentTri = tri
    return tri

def calcNumbFactors(primes):
  s = 1
  for i in range(0,len(primes)):
    s *= primes[i]+1
  if(s > goal):
    print("Goal Reached: " + str(currentTri))
  print("factors: " + str(s))
  return s

def main():
  global notfound
  while(not notfound):
    calcNumbFactors(condense(factorize(calcNextTriNumber())))
  
  
  

main()


  

