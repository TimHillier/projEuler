#https://projecteuler.net/problem=28
#https://en.wikipedia.org/wiki/Ulam_spiral



def EveryN(n):
    Corners = [1]
    counter = 0
    inc = 0
    numbersInRow = 3
    for i in range(2,n*n+1):
        inc +=1
        if (counter == 4):
            numbersInRow += 2
            counter = 0
        if(inc == numbersInRow - 1):
            Corners.append(i)
            counter+=1
            inc = 0
    print(sum(Corners))

def main():
    EveryN(1001)

main()

