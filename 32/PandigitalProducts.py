#https://projecteuler.net/problem=32
products = []



def IsPandigital(A,B,C):
    L = intsToString(A,B,C)
    M = set(L)
    if(0 in M):
        return False
    if(len(M) == 9):
        return True
    else:
        return False


def intsToString(A,B,C):
    L = [int(x) for x in str(A)]
    M = [int(x) for x in str(B)]
    N = [int(x) for x in str(C)]
    O = L+M+N
    return O


for a in range(1,2000):
    for b in range(1,2000):
        D = intsToString(a,b,(a*b))
        if(IsPandigital(a,b,(a*b)) and len(D) == 9):
            products.append(a*b)


Prod_Set = set(products)
print("total: " + str(sum(Prod_Set)))





