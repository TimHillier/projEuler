#https://projecteuler.net/problem=22
from string import ascii_uppercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
score = []
with open("names.txt") as f:
    content = f.read().split(',')
for i in range(0,len(content)):
   content[i] = content[i].replace('"','')

content.sort()

for i in range(0,len(content)):
    list(content[i])
    numbers = [LETTERS[character] for character in content[i] if character in LETTERS]
    results = [int(i) for i in numbers]
    score.append(sum(results)* (i+1))

print(sum(score))
