# import click
#
# choices = {'apple', 'orange', 'peach'}
# choice = click.prompt('Provide a fruit', type=click.Choice(choices, case_sensitive=False))
# print(choice)

import click
from itertools import chain, repeat


fruits = 'apple', 'orange', 'peach'
fruit = input('enter a fruit: ')
prompts = chain([fruit], repeat(f"Error: your input is not one of {fruits}! Try again: "))
replies = map(input, prompts)
lowercased_replies = map(str.lower, replies)
stripped_replies = map(str.strip, lowercased_replies)
valid_response = next(filter(fruits.__contains__, stripped_replies))
print(valid_response)