#https://projecteuler.net/problem=18

with open("triangle.txt") as f:
    content = [line.split() for line in f]

numbers =[[int(y) for y in x] for x in content]

def solve(num):
    lastPos = 0
    cost = 0
    path = [numbers[0][0]]
    for i in range(1,len(num)):
        print("comparing: " + str(num[i][lastPos]) + "," + str(num[i][lastPos+1]))
        if(num[i][lastPos] >= num[i][lastPos+1]):
            cost += num[i][lastPos]
            lastPos = lastPos
            path.append(num[i][lastPos])
            print("WINNER: " + str(num[i][lastPos]) + " at Position: " + str(lastPos))
        elif(num[i][lastPos+1] > num[i][lastPos]):
            cost += num[i][lastPos+1]
            lastPos = lastPos + 1
            path.append(num[i][lastPos])
            print("WINNER: " + str(num[i][lastPos]) + " at Position: " + str(lastPos))

    print(sum(path))
    print(path)


def Dijkstra(Graph,Source):
    visited = []
    






print(numbers)
