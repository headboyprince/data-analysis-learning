import pandas as pd
import random



all_teams = pd.read_csv('UCL_roundof16.csv')
#print(all_teams)

'''Restrictions 

#each seeded teams will play against one of the unseeded teams
#teams from teh same group in teh group satage cannot play againist each other
#teams from  the same country cannot play aganist each other.'''

#initiate new columns

possible_opp = all_teams['Possible Opponents'] = [[]] * 16
num_of_opp  = all_teams ['Number of Possible Opponents'] = [0] * 16
picked_teams = all_teams['Picked'] = [False] * 16


#print(picked_teams)

# #fill in the new columns

for i in range(16):
    possible_opp[i] = []
    print(possible_opp[i])

    for j in range(16):
        seed_i = all_teams['Seeded']
        seed_j = all_teams['Seeded']
        country_i = all_teams['Country']
        country_j = all_teams['Country']
        group_i = all_teams['Group']
        group_j = all_teams['Group']
        abbre = all_teams['Abbreviation']
        pick = all_teams['Picked']
        #print(seed_j)
        if (seed_i[i] != seed_j[j]) & (country_i[i] != country_j[j]) & (group_i[i] != group_j[j]):
            possible_opp[i].append(abbre[j])
#
            num_of_opp[i] = len(possible_opp[i])

'''store the fixtures already drawn'''
first_team = ['']*8
vs = ["vs"]*8
second_team = ['']*8

fixtures= pd.DataFrame({'First Team': first_team, 'vs': vs, 'Second Team': second_team})

#print(fixtures)


'''Pick the first ball'''
m = 0
first_fix = fixtures['First Team'][m]
seeded_teams_left = len(all_teams[(seed_i == True) & (pick == False)])
first = random.randint(0, seeded_teams_left - 1)
fixtures['First Team'][m] = all_teams['Abbreviation'][first]
all_teams['Picked'][all_teams['Abbreviation'] == fixtures['First Team'][m]] = True
#print(fixtures.loc[[m]])

'''Pick the second ball'''
'''remove teams already drawn so it dont get drawn twice'''
second = random.randint(0, num_of_opp[first] - 1)
fixtures['Second Team'][m] = possible_opp[first][second]

#print(fixtures.loc[m])

#remove teams that have been drawn from the dataset.
all_teams['Picked'][all_teams['Abbreviation']== fixtures['Second Team'][m]] = True
all_teams = all_teams[pick == False].reset_index(drop = True)

for i in range(len(all_teams)):
    if fixtures['First Team'][m] in possible_opp[i]:
        possible_opp[i].remove(fixtures['First Team'][m])
    if fixtures['Second Team'][m] in possible_opp[i]:
        possible_opp[i].remove(fixtures['Second Team'][m])
        num_of_opp[i] = len(possible_opp[i])
        m +=1
        print(fixtures.loc[[m-1]])


'''implied fixtures - that is if only 1 team remains after the draw'''

if min(num_of_opp) > 1:
    print('No implied fixtures. continue picking balls for the first time')
else:
    team_index = all_teams[possible_opp == 1].index[0]
if all_teams['Seeded'][team_index] == True:
    first = team_index
    fixtures['First Team'][m]= all_teams['Abbreviation'][first]
    all_teams['Picked'][all_teams['Abbreviation'] == fixtures['First Team'][m]] = True
    second = random.randint(0, all_teams['Number of Possible Opponents'][first] - 1)
    fixtures['Second Team'][m] = all_teams['Possible Opponents'][first][second]
    all_teams['Picked'][all_teams['Abbreviation'] == fixtures['Second Team'][m]] = True
    









