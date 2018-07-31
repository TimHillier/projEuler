#import intertools
#https://projecteuler.net/problem=26
#https://oeis.org/A051626
#https://oeis.org/A003592
from heapq import heappush,heappop

sequence = []
A003592_list = []
def A003592():
    pq = [1]
    seen = set(pq)
    while True:
        value = heappop(pq)
        yield value
        seen.remove(value)
        for x in 2*value,5*value:
            if x not in seen:
                heappush(pq,x)
                seen.add(x)



def A051626(n):
    global A003592_list
    if(n in A003592_list):
        return 0
    else:
        lpow = 1
        while True:
            for mpow in range(lpow-1,-1,-1):
                if((10**lpow-10**mpow)%n==0):
                    return lpow-mpow
            lpow +=1


def main():
    global sequence, A003592_list
    sequence = A003592()
    A003592_list = [next(sequence) for _ in range(100)]
    #print(A003592_list)'
    largest = -1
    num = -1
    for i in range(1,1000):
        if(A051626(i) > largest):
            largest = A051626(i)
            num = i
    print("The largest D" + str(num) + ", with repeating length of " + str(largest))



main()