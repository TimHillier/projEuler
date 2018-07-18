#https://projecteuler.net/problem=8


#put all the digits into an arrayi

with open("number.txt") as f:
    content = f.read()



list(content).remove('\n')

number = list(content)
new = [s for s in number if s.isdigit()]
n = [int(s) for s in number if s.isdigit()]
new = n
biggest = 0
for a in range(0,len(new)-13):
    s = 1
    for x in range(0,13):
        s = s *int(new[a+x])
        
    if(s > biggest):
        biggest = s
    s = 1

print(biggest)
