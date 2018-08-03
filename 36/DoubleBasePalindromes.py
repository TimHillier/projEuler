#https://projecteuler.net/problem=36

def IsPal(N):
    X = list(str(N))
    Y = X[::-1] #this syntax is so weird
    if(X[0] == "0" or Y[0] == "0"):
        return False
    if(X == Y):
        return True
    return False

def ToBinary(N):
    return int("{0:b}".format(N))

def Main():
    Pals = []
    for i in range(0,1000000):
        if(IsPal(i) and IsPal(ToBinary(i))):
            Pals.append(i)
    print(sum(Pals))


Main()
