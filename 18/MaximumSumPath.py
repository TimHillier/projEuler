#https://projecteuler.net/problem=18

with open("triangle.txt") as f:
    content = [line.split() for line in f]

numbers =[[int(y) for y in x] for x in content]
with open("67Triangle.txt") as f:
    content = [line.split() for line in f]
numbers2 = [[int(y) for y in x] for x in content]

def solve(tri):
    m = n = len(tri) - 1
    for i in range(m-1,-1,-1):
        for j in range(i+1):
            if(tri[i+1][j]>tri[i+1][j+1]):
                tri[i][j]+=tri[i+1][j]
            else:
                tri[i][j]+=tri[i+1][j+1]
    return tri[0][0]
print("Problem 18")
print(solve(numbers))


#this is number 67
#https://projecteuler.net/problem=67
print("Problem 67")



print(solve(numbers2))
