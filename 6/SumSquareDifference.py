#https://projecteuler.net/problem=6
def sumofSquares():
    sum = 0
    for i in range(1,101):
        sum = (i * i) + sum
    return sum

def squareofSum():
    sum = 0
    for i in range(1,101):
        sum +=i
    return sum * sum

def diff():
    S1 = sumofSquares()
    S2 = squareofSum()
    print(" sum of squares: " + str(S1))
    print("square of Sum: " + str(S2))
    print(S2 - S1)

diff()
