#https://projecteuler.net/problem=11
search = 4
largest = 0
#length = 20
with open("numbers.txt") as f:
    content = [line.split() for line in f]


numbers =[[int(y) for y in x] for x in content]


#down
p = 1
for col in range(0,len(numbers[0])):
    for row in range(0,len(numbers)-search + 1):
        for s in range(0,search):
        #    print(numbers[row+s][col])
            p = p * numbers[row+s][col]
            if(p > largest):
                largest = p
       # print("*****")
        p = 1

#right
p = 1
for col in range(0,len(numbers[0])-search+1):
    for row in range(0,len(numbers)):
        for s in range(0,search):
            #print(numbers[row][col+s])
            p = p * numbers[row][col+s]
            if(p > largest):
                largest = p
        #print("*****")
        p = 1

#diagonal right
p = 1
for col in range(0,len(numbers[0])-search+1):
    for row in range(0,len(numbers)-search+1):
        for s in range(0,search):
            #print(numbers[row+s][col+s])
            p = p * numbers[row+s][col+s]
            if(p > largest):
                largest = p
        #print("*****")
        p =1

#diagonal left
p = 1
for col in range(0+search-1,len(numbers[0])):
    for row in range(0,len(numbers)-search+1):
        for s in range(0,search):
#            print(numbers[row+s][col-s])
            p = p * numbers[row+s][col-s]
            if(p > largest):
                largest = p
#        print("*****")
        p =1

#print(numbers)

print(largest)


