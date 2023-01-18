word = ['r', 'i', 'g', 'h', 't']
word_validate = "right"
game = True
while game== True:

    userinput = input("enter a character: ").lower()
    if len(userinput) >= 2:
        print('invald character, please enter only one character')
        continue
    else:
        if not userinput.isalpha():
                print("invalid aplphabet, please enter a valid aplhabet")
                continue
        else:
            if userinput not in word:
                print("alphabet not in word, please enter another alphabet")
                continue
            else:
                #accepting multiple values from user and adding to a list
                guessword = []
                guessword.append(userinput)
                print(guessword)






                #print("Right!")
                #print(userinput)
                #break
