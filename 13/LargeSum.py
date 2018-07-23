#https://projecteuler.net/problem=13

with open("numbers.txt") as f:
    content = [line.split() for line in f]


numbers =[[int(y) for y in x] for x in content]



s=0
for x in range(0,len(numbers)):
    s = s + numbers[x][0]


print(s)
#print(numbers)