#https://projecteuler.net/problem=20
import math

def facSum(n):
    a = math.factorial(n)
    b = [int(i) for i in str(a)]
    print(sum(b))

facSum(100)