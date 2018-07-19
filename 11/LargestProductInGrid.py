#https://projecteuler.net/problem=11
search = 4
largest = 0
#length = 20
with open("numbers.txt") as f:
    content = [line.split() for line in f]


numbers =[[int(y) for y in x] for x in content]


#do left and right
for a in range(0,len(numbers)):
    for x in range(0,len(numbers[0])-search):
        s = 1
        for y in range(0,search):
            s = s * numbers[a][x+y]
        if(s > largest):
            largest = s
        s = 1
#do diagonal to right
    for x in range(0,len(numbers[0])):
        s = 1
        for y in range(0,search):
            if(a+search < len(numbers[0]) and y + search < len(numbers[0])):
                s = s * numbers[a+search][y+search]
        if(s > largest):
            largest = s
        s = 1

# do diagonal to left
    for x in range(0,len(numbers[0])):
        s = 1
        for y in range(0,search):
            if(a + search < len(numbers[0]) and y - search > 0):
                s = s * numbers[a+search][y-search]
            if(s > largest):
                largest = s
            s = 1

# do down
    for x in range(0,len(numbers[0])):
        s = 1
        for y in range(0,search):
            if(a > len(numbers[0]) + search):
                s = s * numbers[a][y + search]
            if(s > largest):
                largest = s
            s = 1

print(largest)


