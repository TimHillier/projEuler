#https://projecteuler.net/problem=4
def isPal(num):
    return str(num) == str(num)[::-1]
    
def Pal():
    A = 999
    B = 999
    max = 0

    while(A >= 100):
        if(isPal(A * B)):
            if(A * B > max):
                max = A * B
                print(max)
                B-= 1
        if(B <= 100):
            A -=1
            B = 999
        B-=1
    print(max)

Pal()
