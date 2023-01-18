from itertools import chain, repeat

start = 'yes', 'no'
experience = 'beginner', 'intermediate', 'advanced'
level = 'level 1', 'level 2', 'level 3', 'level 4'

all_replies_by_user = []

def ask_question(input_terminal, question):
    prompts = chain([question], repeat(f"Sorry: your input is not one of {input_terminal}! Try again: "))
    replies = map(input, prompts)
    lowercased_replies = map(str.lower, replies)
    stripped_replies = map(str.strip, lowercased_replies)
    print_question = next(filter(input_terminal.__contains__, stripped_replies))
    all_replies_by_user.append(print_question)
    print(print_question)



[ask_question(*item) for item in ((start, "what is your answer? Yes, No: "),
                                  (experience, "which experience level are you? beginner, intermediate, advanced: "),
                                  (level, "which level do you want to play? level 1, level 2, level 3, level 4: "))]
game_start = all_replies_by_user[0]
game_experience = all_replies_by_user[1]
game_level = all_replies_by_user[2]

#ask_question(start, "what is your answer? Yes, No: ", game_start)
#ask_question(experience, "which experience level are you? beginner, intermediate, advanced: ", game_experience)
#ask_question(level, "which level do you want to play? level 1, level 2, level 3, level 4: ", game_level)