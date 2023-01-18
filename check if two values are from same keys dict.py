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
groups = []
group_list = []
for i in (string.ascii_uppercase):
    group_list.append(f'Group{i}')
    if len(group_list) == 8:
        break


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

#print(bucket1)
# print(bucket2)

#dict with list, get a key that contains a particular value
# for key in bucket1.keys():
#     if 'eng1' in bucket1[key]:
#         print(key)
rem_dict = {'por': ['por1', 'por2'], 'fra': ['fra1']}

#print the keys of the rem_dict as a list
rem_dictkeys = list(rem_dict.keys())
#print(rem_dictkeys)

groupA = ["ita1", "spa2", "por3", "dutch1"]
groupB = ["ita2", "eng2", "germ1", "fra2"]
groupC = ["ita3", "eng1", 'spa3', 'germ4']

new_groupA = {}
for k, v in bucket1.items():
    for i in groupA:
        if i in v:
            new_groupA[k]= i
    # for i in lis_value:
    #     if i in v:
    #         new_dict[k]= v
#print(new_groupA)
groupA_keys = list(new_groupA.keys())
#print(groupA_keys)

new_groupB = {}
for k, v in bucket1.items():
    for i in groupB:
        if i in v:
            new_groupB[k]= i
    # for i in lis_value:
    #     if i in v:
    #         new_dict[k]= v
#print(new_groupB)
groupB_keys = list(new_groupB.keys())
#print(groupB_keys)

new_groupC = {}
for k, v in bucket1.items():
    for i in groupC:
        if i in v:
            new_groupC[k]= i
    # for i in lis_value:
    #     if i in v:
    #         new_dict[k]= v
groupC_keys = list(new_groupC.keys())
#print(groupC_keys)




#get the country for all the teams in the groups




#extract all teh teams in the rem_dict to a list
teams_in_bucket = []
for key in rem_dict.keys():
    teams_in_bucket.append(rem_dict[key])


#flatten the list of list (2D list) into a single list(1D list)
teams_in_bucket = [item for sublist in teams_in_bucket for item in sublist]
print(teams_in_bucket)

#check if two values are in a dictkey
for key1 in rem_dict.keys():
    if f'{teams_in_bucket[0]}' in rem_dict[key1]:
        #print(key1)
        rem_teams = []
        rem_teams.append(key1)

#compare dict and list and get corresponding value key
#compare list with dict values, if it match create a new dict with list as values and dictkeys as keys




for key2 in rem_dict.keys():
    if f'{teams_in_bucket[1]}' in rem_dict[key2]:
        #print(key2)
        rem_teams.append(key2)

for key3 in rem_dict.keys():
    if f'{teams_in_bucket[2]}' in rem_dict[key3]:
        #print(key3)
        rem_teams.append(key3)
        print(rem_teams)


#check if there are duplicates teams
# if len(rem_teams) > len(set(rem_teams)):
#     print(True)
    # if len(rem_teams) - len(set(rem_teams)) == 1:
    #     print("the length has 1 duplicate")
    # if len(rem_teams) - len(set(rem_teams)) == 2:
    #     print("the length has 2 duplicates")
else:
    print(False)






# for v in bucket1.values():
#     for k in bucket1.keys():
#         print(k, v)

# for v in bucket1.keys():
#     for k in v():
#         print(v, k)



    # if 'eng1' in key.values():
    #     print("yes")
    # else:
    #     print("no")