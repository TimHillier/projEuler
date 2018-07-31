#https://projecteuler.net/problem=24


def swap(Array,i,j):
    Array[i],Array[j] = Array[j],Array[i]

def Reverse(Array,i,j):
    for offset in range((j-i+1)//2):
        swap(Array,i+offset,j-offset)

def perm(Array):
    LastI = len(Array) - 1
    if(LastI < 1):
        return
    i = LastI - 1
    while i >= 0 and not Array[i]<Array[i+1]:
        i -=1

    if(i < 0):
        reversed(Array,0,LastI)
    else:
        j = LastI
        while j > i+1 and not Array[j]>Array[i]:
            j -=1
        swap(Array,i,j)
        Reverse(Array,i+1,LastI)




def Main():
    A = [0,1,2,3,4,5,6,7,8,9]
    for i in range(0,1000000-1):
        perm(A)
    print(A)

Main()
