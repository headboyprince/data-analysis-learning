from itertools import chain, repeat

start = 'yes', 'no'
experience = 'beginner', 'intermediate', 'advanced'
level = 'level 1', 'level 2', 'level 3', 'level 4'

game_start = ""
game_experience = ""
game_level = ""


prompts = chain(["what is your answer? Yes, No: "], repeat(f"Sorry: your input is not one of {start}! Try again: "))
replies = map(input, prompts)
lowercased_replies = map(str.lower, replies)
stripped_replies = map(str.strip, lowercased_replies)
game_start = next(filter(start.__contains__, stripped_replies))
print(game_start)

prompts = chain(["which experience level are you? beginner, intermediate, advanced: "], repeat(f"Sorry: your input is not one of {experience}! Try again: "))
replies = map(input, prompts)
lowercased_replies = map(str.lower, replies)
stripped_replies = map(str.strip, lowercased_replies)
game_experience = next(filter(experience.__contains__, stripped_replies))
print(game_experience)

prompts = chain(["which level do you want to play? level 1, level 2, level 3, level 4: "], repeat(f"Sorry: your input is not one of {level}! Try again: "))
replies = map(input, prompts)
lowercased_replies = map(str.lower, replies)
stripped_replies = map(str.strip, lowercased_replies)
game_level = next(filter(level.__contains__, stripped_replies))
print(game_level)





















from itertools import chain, repeat

start = 'yes', 'no'
experience = 'beginner', 'intermediate', 'advanced'
level = 'level 1', 'level 2', 'level 3', 'level 4'

game_start = ""
game_experience = ""
game_level = ""

def ask_question(input_terminal, question, print_question):
    prompts = chain([question], repeat(f"Sorry: your input is not one of {input_terminal}! Try again: "))
    replies = map(input, prompts)
    lowercased_replies = map(str.lower, replies)
    stripped_replies = map(str.strip, lowercased_replies)
    print_question = next(filter(input_terminal.__contains__, stripped_replies))
    print(print_question)



ask_question[(start, "what is your answer? Yes, No: ", game_start), \
(experience, "which experience level are you? beginner, intermediate, advanced: ", game_experience)\
    (level, "which level do you want to play? level 1, level 2, level 3, level 4: ", game_level)]



