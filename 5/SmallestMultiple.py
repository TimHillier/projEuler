#https://projecteuler.net/problem=5

def Check(num):
    for a in range(1,20):
        if(num % a > 0):
            return False
    return True

def Generate():
    num = 1
    while(not Check(num)):
        num += 1

    print(num)

Generate()
