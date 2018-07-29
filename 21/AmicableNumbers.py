#https://projecteuler.net/problem=21
Total = []
def d(n):
    s = 0
    for i in range(1,n):
        if(n % i == 0):
            s += i
    return(s)



def isAmicable(a):
    global Total
    B = d(a)
    A = d(B)
    if(A == a and A != B):
        Total.append(a)

def main():
    global Total
    for i in range(1,10001):
        isAmicable(i)
    print(sum(Total))

main()