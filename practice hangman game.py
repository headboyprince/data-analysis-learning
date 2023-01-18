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



    #entering only one valid charater

game = True
while game == True:
        user_input = input("guess a letter: ").lower()
        if len(user_input) >= 2:
            print('invald character, please enter only one character')
            continue
        else:
            if not user_input.isalpha():
                print("invalid alphabet, please enter a valid alaphabet")
                continue
            else:
                print("Right!")
                guessword = []
                guessword.append(user_input)
                break

print(guessword)



        #     user_input = input("guess a letter: ").lower()
        # else:
        #     break
        # print(type(user_input))
