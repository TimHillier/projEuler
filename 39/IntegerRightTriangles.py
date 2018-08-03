#https://projecteuler.net/problem=39
import math

def GetPeram(A,B):
    return A + B + math.sqrt(A**2+B**2)





def FindTriangles(P):
    Largest = -1
    LargestI = 0
    Current = 0
    for a in range(1,int(P/2)):
        for b in range(1,int(P/2)):
            C = GetPeram(a,b)
            if(C == P):
                Current +=1

        if(Current > Largest):
            Largest = Current
            Current = 0

    return Largest




def Main():
    Most = 0
    BiggestP = -1
    for P in range(120,1001):
        if(P % 120 ==0):
            A = FindTriangles(P)
            if(A > Most):
                Most = A
                BiggestP = P

    print(BiggestP)



Main()
