def ask_question(question, valid_answers):
    valid_answers_display = ', '.join(valid_answers)
    question_display = f"{question}  Valid answers are {valid_answers_display}: "

    while True:
        answer = input(question_display).lower().strip()
        if answer not in valid_answers:
            question_display = f'please enter one of the valid answers -- {valid_answers_display}: '
        else:
            break

    return answer

start_question = "what is your answer?"
start_valid_answers = ["yes", "no"]
start_answer = ask_question(start_question, start_valid_answers)

experience_question = "what experience level are you?"
experience_valid_answers = ["beginner", "intermediate", "advanced"]
experience_answer = ask_question(experience_question, experience_valid_answers)

level_question = "what level do you want to play?"
level_valid_answers = ['level 1', 'level 2', 'level 3', 'level 4']
level_answers = ask_question(level_question, level_valid_answers)

print(f"start question asnwer: {start_answer}.")
print(f"Experience question answer: {experience_answer}.")
print(f"Level question answer: {level_answers}.")