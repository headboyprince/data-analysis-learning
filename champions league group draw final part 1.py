import random
import string
'''A uefa champions league draw simulator. '''
# Reveices input for 32 teams from 14 different conutries'''
# Randomly distribute the teams into groups of 4 without putting teams from same countries in same group

'''TODO: Step 1 - create all the Global variables'''

teams1 = []
teams2 = []
teams3 = []
teams4= []
country = []


#print(group_list)



'''TODO: Step 2 - create all the various 32 teams'''

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

'''TODO: Step 3 - seperate all the 32 teams into 2 different buckets'''
bucket1 = []
bucket1.extend([teams1[6]])
bucket1.extend(teams3)
bucket1.extend(teams4)
#print(bucket1)

bucket2 = []
bucket2.extend(teams2)
bucket2.extend(teams1)

for x in bucket1:
    for y in bucket2:
        if x == y:
            bucket2.remove(x)
#print(bucket2)
bucket1_2 = []
for x in bucket1:
    bucket1_2.append(x)
#print(bucket1)
#print(bucket1_2)
'''TODO: Step 4 - classify all the 32 teams into into various countries, inside the buckets '''
def convert2Dict(teamslist):
    resultdict = {}
    for team in teamslist:
        country = team[:-1]
        if country not in resultdict.keys():
            resultdict[country] = []
        resultdict[country].append(team)
    return resultdict
bucket1 = convert2Dict(bucket1)
bucket2 = convert2Dict(bucket2)
bucket1_2 = convert2Dict(bucket1_2)
print(bucket1)
print(bucket1_2)


# for key in bucket1:
#     if por1 in key:
#         print("yes")
#     else:
#         print("no")


'''TODO: Step 5 - classify all the 32 teams into into various countries, inside the buckets '''
#print(bucket1)
# groups = []
# group_list = []
# for i in (string.ascii_uppercase):
#     group_list.append(f'Group{i}')
#     if len(group_list) == 8:
#         break
for group in range(8):


    figure1, figure2, figure3 = random.sample(bucket1.keys(), 3)  # select three random countries
    #     #print(figure1)
    #
    '''select 1st random number'''
    select_random_team = (bucket1[f'{figure1}'])
    select_random_team1 = random.choice(select_random_team) #select the 1st random team
        #print(select_random_team1


        # delete a value from the dict after picking

            # delete an empty list from the dict
    '''select 2nd random number'''
    select_random_team = (bucket1[f'{figure2}'])
    select_random_team2 = random.choice(select_random_team) #select the 2nd random team
    # delete a value from the dict after picking


    '''select 3rd random number'''
    select_random_team = (bucket1[f'{figure3}'])
    select_random_team3 = random.choice(select_random_team)  # select the 3rd random team



#print(random_number1)
    print(f'group'f'{group + 1}')
    group = []
    group.append([select_random_team1, select_random_team2, select_random_team3])
    for i in range(0, len(bucket1) - 1):
        if bucket1[f'{figure3}'][i] == f'{select_random_team3}':
            del bucket1[f'{figure3}'][i]
        if bucket1[f'{figure2}'][i] == f'{select_random_team2}':
            del bucket1[f'{figure2}'][i]
        if bucket1[f'{figure1}'][i] == f'{select_random_team1}':
            del bucket1[f'{figure1}'][i]
            break
    bucket1 = {key: value for key, value in bucket1.items() if len(value) != 0}

    print(group)
    if len(bucket1) < 3:

        break
print(bucket1)
    #print(random_number2)

    # print(group_list[count])
    # groups = group_list
    # groups[count] = []
    # #print(groups)
    # groups[count].extend([select_random_team1, select_random_team2, select_random_team3, random_number2])
    # print(groups[count])


#
#for count in range(8):
#
#
#     if len(bucket1) < 3:
#         break
#
#     '''BUCKET1'''  # Select random team and delete the team.
#     # check if the dict the randomteam was selected from is empty, and delete it
#     figure1, figure2, figure3 = random.sample(bucket1.keys(), 3) #select three random countries
#     #print(figure1)
#
#     '''select 1st random number'''
#     select_random_team = (bucket1[f'{figure1}'])
#     select_random_team1 = random.choice(select_random_team) #select the 1st random team
#     #print(select_random_team1)
#
#
#     # delete a value from the dict after picking
#     for i in range(0, len(bucket1) - 1):
#         if bucket1[f'{figure1}'][i] == f'{select_random_team1}':
#             groups[count].extend([select_random_team1])
#             del bucket1[f'{figure1}'][i]
#             break
#         # delete an empty list from the dict
#
#
#     '''select 2nd random number'''
#     select_random_team = (bucket1[f'{figure2}'])
#     select_random_team2 = random.choice(select_random_team) #select the 2nd random team
#     # delete a value from the dict after picking
#     for i in range(0, len(bucket1) - 1):
#         if bucket1[f'{figure2}'][i] == f'{select_random_team2}':
#             groups[count].extend([select_random_team2])
#             del bucket1[f'{figure2}'][i]
#             break
#
#
# #
#     '''select 3rd random number'''
#     select_random_team = (bucket1[f'{figure3}'])
#     select_random_team3 = random.choice(select_random_team)  # select the 3rd random team
#
#     for i in range(0, len(bucket1) - 1):
#         if bucket1[f'{figure3}'][i] == f'{select_random_team3}':
#             groups[count].extend([select_random_team3])
#             del bucket1[f'{figure3}'][i]
#             break
#     bucket1 = {key: value for key, value in bucket1.items() if len(value) != 0}
    # append the random team to the group
    #groups = group_list


    # print(group_list[count])
    #print(f'{group_list}{count}')
    #print(group_list[count])
    #print(group_list)
    # groups[count].extend([select_random_team1])
    # groups[count].extend([select_random_team2])
    # groups[count].extend([select_random_team3])
    #     #groups[count].extend([select_random_team4])
    #
    #print(groups[count])



#     # delete a value from the dict after picking
#

# #
#     '''BUCKET2''' #Select random team and delete the team.
#     #check if the dict the randomteam was selected from is empty, and delete it
#     figure4 = random.sample(bucket2.keys(), 1)
#     print(figure4)
#     select_random_team = (bucket2[f'{figure4}'])
#     select_random_team4 = random.choice(select_random_team)  # select the 4th random team
#     # delete a value from the dict after picking
#     for i in range(0, len(bucket2) - 1):
#         if bucket2[f'{figure4}'][i] == f'{select_random_team4}':
#             del bucket2[f'{figure4}'][i]
#             break
#     # delete an empty list from the dict
#     bucket2 = {key: value for key, value in bucket2.items() if len(value) != 0}
#



#
#
#
# # print(teams4)
# print(bucket1)




