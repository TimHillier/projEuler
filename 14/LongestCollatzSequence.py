#https://projecteuler.net/problem=14

def main():
    longestsequence = 0
    bestStart = 0
    for x in range(2,1000000):
        print("current Start: " + str(x))
        n = x
        sequence = 0
        while(n > 1):
            if(n%2 == 0):
                n = n/2
                sequence += 1
            else:
                n = 3 * n + 1
                sequence += 1
        if sequence > longestsequence:
            longestsequence = sequence
            bestStart = x

    print(bestStart)

main()