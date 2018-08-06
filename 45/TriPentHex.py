#https://projecteuler.net/problem=45

T = []
P = []
H = []

def TriangleNumber(n):
    return int((n*(n+1))/2)

def PentNumber(n):
    return int((n*(3*n-1))/2)

def HexNumber(n):
    return int((n*(2*n-1)))

def IsIn(n):
    print("testing: " + str(n))
    if(n in T and n in P and n in H):
        return True
    elif(n < T[len(T)-1] and n < P[len(P)-1] and n < H[len(H)-1]):
        return False
    elif(n >T[len(T)-1]):
        T.append(TriangleNumber(len(T)+1))
        return IsIn(n)
    elif(n > P[len(P)-1]):
        P.append(PentNumber(len(P)+1))
        return IsIn(n)
    elif(n > H[len(H)-1]):
        H.append(HexNumber(len(H)+1))
        return(IsIn(n))
    else:
        return False




def Main():
    global T,P,H
    #calc up to the numbers in the question
    for i in range(1,286):
        T.append(TriangleNumber(i))
    for i in range(1,166):
        P.append(PentNumber(i))
    for i in range(1,145):
        H.append(HexNumber(i))

    n = 144
    while(not IsIn(H[len(H)-1])):
        H.append(HexNumber(len(H)+1))
    print(H[len(H)-1])




    #Find the next one

Main()
