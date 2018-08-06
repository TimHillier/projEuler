#https://projecteuler.net/problem=43
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


def GeneratePandigital(Arr):
    if(Arr[0] == 0):
        while(Arr[0] == 0):
            perm(Arr)
    elif(Arr[0] != 0):
        perm(Arr)
    return Arr


def divis(current):
    if(int(''.join(map(str,current[1:4]))) % 2 == 0):
        if(int(''.join(map(str,current[2:5]))) % 3 == 0):
            if(int(''.join(map(str,current[3:6]))) % 5 == 0):
                if(int(''.join(map(str,current[4:7]))) % 7 == 0):
                    if(int(''.join(map(str,current[5:8]))) % 11 == 0):
                        if(int(''.join(map(str,current[6:9]))) % 13 == 0):
                            if(int(''.join(map(str,current[7:10])))%17 == 0):
                                return True
    return False

def solve(array):
    Correct = []
    Tested = []
    for i in range(0,1632960):
        if(divis(array)):
            Correct.append(int(''.join(map(str,array))))
        array = GeneratePandigital(array)
    print(sum(Correct))


def Main():
    start = [0,1,2,3,4,5,6,7,8,9]
    solve(start)


Main()
