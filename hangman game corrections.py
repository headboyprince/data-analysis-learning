import random


# List of Words
a = open('3000words.txt', 'r')
words = a.read()
a.close()
words = words.split()
hardWords = []
mediumWords = []
easyWords = []

def appending(list, x, y):
    for i in words:
        if x >=  len(i) >= y:
            list.append(i)

appending(easyWords, 4, 2)
appending(mediumWords, 7, 5)
appending(hardWords, 20, 7)

guessNum = 0
error = 0

word_level = {"1": easyWords, "2": mediumWords, "3": hardWords}
while True:
    def print_code(*x):
        print(*x)
    print_code('1: Easy',
               '2: Medium',
               '3: Hard')

    difficulty = input('Choose a Difficulty Level:').strip()
    word = random.choice(word_level[difficulty])
    print(word)
    break
else:
    print('Choose 1 ,2 ,or 3:')

for i in word:
    guessNum += 1
    splitWord = [i for i in word]
    guessWord = ["_" for j in range(0, guessNum)]

game = True
while game == True:
    userLetter = input('What letter do you guess:').lower()
    found = False
    #ind = splitWord.index(splitWord[-1])
    index = splitWord.index(splitWord[-1])
    print(index)

    while index>= 0:
        if splitWord[index] == userLetter:
            guessWord[index] = userLetter
            found = True
        index -= 1
    print('The Word is:', ' '.join(i for i in guessWord))


    if found == False:
        error += 1
        print(f'you have {6 - error} lives remaining')

    if error == 6:
        print('Game Over You Lose')
        print('The Word was:', ' '.join(i for i in splitWord))
        game = False
        break
    if splitWord == guessWord:
        print('You Win')
        game = False
        break