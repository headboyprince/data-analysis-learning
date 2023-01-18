import random

# List of Words
a = open('3000words.txt', 'r')
words = a.read()
a.close()
words = words.split()
easyWords = []
mediumWords = []
hardWords = []



for i in words:
    i = i.lower()
    if len(i) > 7:
        hardWords.append(i)
    elif len(i) >= 5:
        mediumWords.append(i)
    elif len(i) > 2:
        easyWords.append(i)

# Select Word
guessNum = 0
error = 0
while True:
    print('1: Easy')
    print('2: Medium')
    print('3: Hard')
    difficulty = input('Choose a Difficulty Level:')

    if difficulty == "1":
        index = random.randint(0, easyWords.index(easyWords[-1]))
        word = easyWords[index]
        break
    elif difficulty == "2":
        index = random.randint(0, mediumWords.index(mediumWords[-1]))
        word = mediumWords[index]

        break
    elif difficulty == "3":
        index = random.randint(0, hardWords.index(hardWords[-1]))
        word = hardWords[index]
        break
    else:
        print('Choose 1 ,2 ,or 3:')
print(word)

splitWord = []
for i in word:
    guessNum += 1
    splitWord.append(i)

guessWord = []
while guessNum > 0:
    guessWord.append("_")
    guessNum -= 1

game = True
while game == True:
    # Man Status Check
    if error < 1:
        a = " "
    else:
        a = "O"
    if error < 2:
        b = " ";
        d = " ";
        f = " "
    else:
        b = "|";
        d = "|";
        f = "|"
    if error < 3:
        c = " "
    else:
        c = "/"
    if error < 4:
        e = " "
    else:
        e = "\ "
    if error < 5:
        g = " ";
        i = " "
    else:
        g = "/";
        i = "|"
    if error < 6:
        h = " ";
        j = " "
    else:
        h = "\ ";
        j = "|"

    # Draw Board
    print('   __________   ')
    print('   |        |   ')
    print('   |       ', a)
    print('   |       ', b)
    print('   |     ', c, d, e)
    print('   |       ', f)
    print('   |      ', g, h)
    print('   |      ', i, j)
    print('   |       ')
    print('___|______________')
    print("")
    print('The Word is:', ' '.join(i for i in guessWord))

    # game over checker
    if error == 6:
        print('Game Over You Lose')
        print('The Word was:', ' '.join(i for i in splitWord))
        game = False
        break
    if splitWord == guessWord:
        print('You Win')
        game = False
        break

    # User Input/Analysis
    userLetter = input('What letter do you guess:').lower()
    found = False
    index = splitWord.index(splitWord[-1])

    while index >= 0:
        if splitWord[index] == userLetter:
            guessWord[index] = userLetter
            found = True
        index -= 1

    if found == False:
        error += 1