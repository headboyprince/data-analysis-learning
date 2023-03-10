import random
import math
num_teams = 32

country_list  = {"england": ["english", 4], "france": ["french", 4],
                 "spain": ["spainish", 4], "germany": ["germany", 4],
                 "italy": ["italian", 4], "portugal": ["portuguese", 3],
                 "russia": ["russia", 2], "dutch": ["dutchese", 1], "turkey": ["turkish", 1],
                 "scotland": ["scottish", 1], "greece": ["greek", 1], "poland": ["polish", 1],
                 "belgium": ["belgian", 1]}

group_and_teams = {"groupA": {}, "groupB": {}, "groupC": {}, "groupD": {},
                   "groupE": {}, "groupF": {}, "groupG": {}, "groupH": {}}

print('\tUEFA champions league draw simulator\n')
print('enter teams to make your very own UEFA champions league')
print('press the enter key to begin')

x = 0
for country in country_list:
    x += country_list[country][1]
x = math.ceil(x/len(group_and_teams))

list_teams = {}
for country in country_list:
    for x in range(country_list[country][1]):
        list_teams[input("please nter an {} team: ".format(country_list[country][0]))] = country

def find_open_slot(new_team):
    good = True
    group_chosen = False
    rand = random.sample(list(group_and_teams), 1)[0]
    while group_chosen==False:
        if len(group_and_teams[rand]) > 0:
            for listed_team in group_and_teams[rand]:
                if new_team == listed_team or list_teams[new_team][1] == group_and_teams[rand][listed_team]:
                    good = False
        else:
            group_chosen = True
            return rand

        if good == False:
            rand = random.sample(list(group_and_teams), 1)[0]
        else:
            group_chosen = True
            return rand

for team in list_teams:
    group = find_open_slot(team)
    teams = group_and_teams[group]
    teams[team] = list_teams[team]

print('\n Assembling groups... \n')
input('groups complete. Press the enter key to view.')

for group in group_and_teams:
    for teams in group_and_teams[group]:
        print("{}: team: {}, country: {}". format(group, teams, group_and_teams[group][teams]))
