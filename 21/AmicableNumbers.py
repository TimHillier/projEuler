#https://projecteuler.net/problem=21
Total = []
def d(n):
    s = 0
    for i in range(1,n):
        if(n % i == 0):
            s += i
    return(s)



def isAmicable(n):
    global Total
    A = d(n)
    B = d(A)
    if(B == A and B == n):
        Total.append(n)
        #Total.append(d(n))

def main():
    global Total
    for i in range(1,10001):
        isAmicable(i)
   # isAmicable(220)
    print(sum(Total))
    print(Total)
main()