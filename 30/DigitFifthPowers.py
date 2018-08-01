#https://projecteuler.net/problem=30


def Solve(n):
    yes = []
    for i in range(2,1000000):
        s = 0
        a = [int(x) for x in str(i)]
        for c in range(0,len(a)):
            s +=a[c]**n
        if(s == i):
          yes.append(s)
    print(yes)
    print(sum(yes))
def Main():
    Solve(5)

Main()