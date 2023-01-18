game = True
while game== True:
    userinput = input("enter a character: ").lower()
    if len(userinput) >= 2:
        print('invald character, please enter only one character')
    else:
        if not userinput.isalpha():
                print("incorrect")
                continue
        else:
                print("Right!")
                print(userinput)
                break