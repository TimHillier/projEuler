#https://projecteuler.net/problem=17
from num2words import num2words
words = ""
for i in range(1,1001):
    words = words + num2words(i)
words = words.replace("-","")
words = words.replace(" ","")
print(len(words))