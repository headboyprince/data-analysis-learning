import random

'''TODO: Step 1 - open file and read lines as words and select a random choice'''
file_name = open(f'3000words.txt', 'r') #the name of the file with the words
words = file_name.read()
file_name.close()
words = words.split()
print(words)
'''TODO: Step 2 - select a random choice'''
select_random_word = random.choice(words)
print(select_random_word)


#
# def read_file(file):
#
#     file_name = open(f'{file}.txt', 'r')
#     words = file_name.read()
#     file_name.close()
#     words = words.split()
#     print(words)
#     select_random_word = random.choice(words)
#     print(select_random_word)
#
# read_file("3000words")

print(select_random_word)

# def read_file(file_name):
#     '''TODO: Step 1 - open file and read lines as words and select a random choice'''
#     with open (file_name, 'r') as f:
#         word_list = f.readlines()
#     print(word_list)

# def select_random_word(words):
#     '''TODO: Step2 - Select random word from list of file'''
#
#
# word_index = random.randint(0,len(words) - 1)
# word = words[word_index]
# print("Guess the word: "+ word[1:])
#
#
#
# read_file('3000words.txt')

