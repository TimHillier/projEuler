#https://projecteuler.net/problem=33

def FracEqual(N1,D1,N2,D2):
    if(D1 ==0 or D2 == 0):
        return False
    if(N1/D1 == N2/D2):
        return True
    else:
        return False

def FracSimp(N1,D1):
    N = [int(x) for x in str(N1)]
    D = [int(x) for x in str(D1)]
    Temp = N + D
    RemoveDupe(Temp)
    FracSet = list(set(Temp))
    #del FracSet[1]
   # FracSet.reverse()
    if(len(FracSet) == 2):
        return FracSet
    else:
        return []


def FracGen():
    for N in range(10,99):
        for D in range(10,99):
            if(N/D >= 1 or N%10 ==0 and D%10==0):
                #do nothing
                a = 0
            else:
                CurrentFraction = FracSimp(N,D)
                if(len(CurrentFraction) > 0):
                    if(FracEqual(N,D,CurrentFraction[0],CurrentFraction[1])):
                        print(str(CurrentFraction[0]) + "/" + str(CurrentFraction[1]) + " = " + str(N) + "/" + str(D))

def RemoveDupe(L):
   for i in range(0,len(L)-1):
       for j in range(i+1,len(L)):
           if(L[i] == L[j]):
               del L[j]
               del L[i]
               break


def Main():
    FracGen()

Main()
