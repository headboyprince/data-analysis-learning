import random

#get random word
a = open('3000words.txt', 'r')
words = a.read()
a.close()
wordlist = words.split()
word= random.choice(wordlist)
print(word)

#print missed letters
print
