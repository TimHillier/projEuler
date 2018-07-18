#https://projecteuler.net/problem=9
import math
find = 25
su = []

def Triplet(Max):
    a = 1
    b = 2
    c = 3
    for i in range(a,Max):
        for j in range(i+1,Max):
            for k in range(j+1,Max):
                if(i + j + k == Max):
                    if(i*i + j*j == k*k):
                        print(i*j*k)

Triplet(1000)
        
