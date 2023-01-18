import random
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




# hardWords = [i for i in words if len(i) > 7]
# mediumWords = [i for i in words if 7 >= len(i) >= 5]
# easyWords = [i for i in words if 4 >= len(i) >= 2]


#Select Word
guessNum = 0
error = 0

word_level = {"1": easyWords, "2": mediumWords, "3":hardWords}
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


splitWord = [i for i in word]
guessNum= len(word)


    # squares = []
    # for i in range(10):
    #     squares.append(i * i)
    #
    # squares = [i * i for i in range(10)]
print(splitWord)
print(guessNum)

# for word in range(0, guessNum):
#     guessWord.append("_")
for i in word:
    guessNum += 1
    guessWord = ["_" for j in range(0, guessNum)]
    print(guessWord)

game = True
while game == True:
    userLetter = input('What letter do you guess:').lower()
    found = False
    index = splitWord.index(splitWord[-1])
    y = 0

output = []

for x in splitWord:
    if x == UserLetter:
        output.append(y)
    y = y + 1

print (output)





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