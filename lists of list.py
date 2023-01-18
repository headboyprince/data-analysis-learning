import random
import string
'''A uefa champions league draw simulator. '''
# Reveices input for 32 teams from 14 different conutries'''
# Randomly distribute the teams into groups of 4 without putting teams from same countries in same group
teams1 = []
teams2 = []
teams3 = []
teams4= []
country = []
groups = []
group_list = []
for i in (string.ascii_uppercase):
    group_list.append(f'Group{i}')
    if len(group_list) == 8:
        break

def get_teams(*args, x, y, list):
    for country in (args):
        for n in range(x, y):
            list.append(f'{country}{n}')
            #country.append(f'{country}{n}')
    #print(country)
get_teams("eng", "spa", "ita", "fra", "germ", x=1,y = 5, list =teams4)
get_teams("rus", x=1,y = 3, list =teams2)
get_teams("por", x=1,y = 4, list =teams3)
get_teams("swis", "bel", "turk", "greece", "pol", "scot", "dutch", x=1,y = 2, list =teams1)
print(teams4)



teams4
resultdict = {}
def convert2Dict(teamslist):

    for team in teamslist:
        country = team[:-1]
        if country not in resultdict.keys():
            resultdict[country] = []
        resultdict[country].append(team)
    return resultdict

# teams1 =convert2Dict(teams1)
# teams2 = convert2Dict(teams2)
# teams3 = convert2Dict(teams3)
teams4 = convert2Dict(teams4)

print(teams4)
#print(teams1, teams2, teams3, teams4)

for count in range(8):
    figure1, figure2 = random.sample(teams4.keys(), 2)
    #print(random_team)
    #print(figure1)

    select_random_team = (teams4[f'{figure1}'])
    #print(select_random_team)
    select_random_team1 = random.choice(select_random_team)
    #print(select_random_team1)
# delete a value from the dict after picking
    for i in range(0, len(teams4) - 1):
        if teams4[f'{figure1}'][i] == f'{select_random_team1}':
            del teams4[f'{figure1}'][i]
            break
    select_random_team = (teams4[f'{figure2}'])
    # print(select_random_team)
    select_random_team2 = random.choice(select_random_team)
    # print(select_random_team1)
    # delete a value from the dict after picking
    for i in range(0, len(teams4) - 1):
        if teams4[f'{figure2}'][i] == f'{select_random_team2}':
            del teams4[f'{figure2}'][i]
            break
#delete an empty list from the dict
    teams4 = {key: value for key, value in teams4.items() if len(value) != 0}

#append the random team to the group
    print(group_list[count])
    groups = group_list
    groups[count] = []
    # print(groups)
    groups[count].extend([select_random_team1])
    groups[count].extend([select_random_team2])
    print(groups[count])

print(teams4)


# print(resultdict)



