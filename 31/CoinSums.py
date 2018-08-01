#https://projecteuler.net/problem=31

coins = [1,2,5,10,20,50,100,200]
goal = 200
def Combo(g):
    A = [0 for k in range(g+1)]
    A[0] = 1

    for i in range(0,len(coins)):
        for j in range(coins[i],g+1):
            A[j] += A[j-coins[i]]
    return A[g]



def main():
    print(Combo(goal))

main()