import random
import numpy as np

'''A uefa champions league draw simulator. '''
# Reveices input for 32 teams from 14 different conutries'''
# Randomly distribute the teams into groups of 4 without putting teams from same countries in same group
teams = []
teams2 = []
teams3 = []
def get_teams(*args, x, y, list):
    for country in (args):
        for n in range(x, y):
            list.append(f'{country}{n}')
    #print(list)
get_teams("eng", "spa", "ita", "fra", "port", "germ", x=1,y = 5, list =teams)
get_teams("dutch", x=1,y = 3, list =teams2)
get_teams("swis", "bel", "turk", 'rus', "pol", "scot", "grec", x=1,y = 2, list =teams3)

country_teams = []
chunk_size = 4
country_teams = [teams[i:i + chunk_size] for i in range(0, len(teams), chunk_size)]
#print(country_teams)
eng, spa, ita, fra, port, germ = country_teams

for tea in get_teams(*args):
    print (tea)
# teams = []
#
#
# def get_teams(*args):
#     count = 0
#     for country in (args):
#         count +=1
#         if count == 7:
#             break
#         for n in range(1, 5):
#             teams.append(f'{country}{n}')
# get_teams("eng", "spa", "ita", "fra", "port", "germ","dutch", "swis", "bel", "turk", 'rus', "pol", "scot", "grec")


# teams2 = []
# def get_teams2(*arg):
#     for country in (arg):
#         for i in range(1,3):
#             teams2.append(f'{country}{i}')
# get_teams2("dutch")
# print(teams2)
#
# teams3 = []
# def get_teams3(*arg):
#     for country in (arg):
#         for i in range(1,2):
#             teams3.append(f'{country}{i}')
# get_teams3("swis", "bel", "turk", 'rus', "pol", "scot", "grec")
# print(teams3)