#https://projecteuler.net/problem=40


def MakeList(length):
    L = []
    counter = 1
    while(len(L) < length):
        L += [str(x) for x in str(counter)]
        counter +=1
    return L

def Main():
    s = []
    A = MakeList(1000000)
    s.append(int(A[1-1]))
    s.append(int(A[10-1]))
    s.append(int(A[100-1]))
    s.append(int(A[1000-1]))
    s.append(int(A[10000-1]))
    s.append(int(A[100000-1]))
    s.append(int(A[1000000-1]))
    print(s)
    print("sum = 210")


Main()
