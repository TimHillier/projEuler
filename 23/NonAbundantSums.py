#https://projecteuler.net/problem=23


def Abundant(n):
    #will return true if is abundant
    s = 0
    for i in range(1,int(n/2)+1):
        if(n % i == 0):
            s += i
    if(s > n):
        return True # is abundent
    else:
        return False # is not abundent


def Main():
    Numbers = [False] * 28123
    Total = [True] * 28123
    S = 0
    for i in range(0,len(Numbers)):
        Numbers[i] = Abundant(i)
    for i in range(0,len(Numbers)):
        if(Numbers[i]):
            for j in range(i,len(Numbers)):
                if(Numbers[j] and i+j <28123):
                    Total[i+j] = False
    for i in range(0,len(Total)):
        if(Total[i]):
            S += i
    print(S)

Main()

