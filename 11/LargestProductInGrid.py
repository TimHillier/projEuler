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



for a in range(0,len(numbers)-search):
    s = 1
    #sum of left, right
    for x in range(0,search):
        s = s * numbers[a+x]
        
        if(s>largest):
            largest = s
        s = 1

print(largest)


