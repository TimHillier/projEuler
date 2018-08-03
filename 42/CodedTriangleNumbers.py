#https://projecteuler.net/problem=42
from string import ascii_uppercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
score = []
TriangleNums = [1,3,6]
with open("words.txt") as f:
    content = f.read().split(',')
for i in range(0,len(content)):
   content[i] = content[i].replace('"','')


def WordsToSum():
    for i in range(0, len(content)):
        # list(content[i])
        numbers = [LETTERS[character] for character in content[i] if character in LETTERS]
        results = [int(i) for i in numbers]
        score.append(sum(results))

def GenerateTriangleNums(n):
    return int(((n*(n+1))/2))

def Compare(n):
    if(n in TriangleNums):
        return True
    elif(n < TriangleNums[len(TriangleNums)-1]):
        return False
    elif(n > TriangleNums[len(TriangleNums)-1]):
        TriangleNums.append(GenerateTriangleNums(len(TriangleNums)+1)) #is this dynamic Programming?
        return Compare(n)
    else:
        return False

def Main():
    s = 0
    WordsToSum()
    for i in range(0,len(content)):
        if(Compare(int(score[i]))):
           s += 1
    print(s)
Main()