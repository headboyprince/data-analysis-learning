
import random
'''A uefa champions league draw simulator. '''
# Reveices input for 32 teams from 14 different conutries'''
# Randomly distribute the teams into groups of 4 without putting teams from same countries in same group
teams = []
teams2 = []
teams3 = []
teams4= []
country = []
def get_teams(*args, x, y, list):
    for country in (args):
        for n in range(x, y):
            list.append(f'{country}{n}')
            #country.append(f'{country}{n}')
    #print(country)
get_teams("eng", "spa", "ita", "fra", "germ", x=1,y = 5, list =teams)
get_teams("rus", x=1,y = 3, list =teams2)
get_teams("por", x=1,y = 4, list =teams4)
get_teams("swis", "bel", "turk", "greece", "pol", "scot", "dutch", x=1,y = 2, list =teams3)


# country_teams = []
# chunk_size = 4
# country_teams = [teams[i:i + chunk_size] for i in range(0, len(teams), chunk_size)]
# #print(country_teams)
# eng, spa, ita, fra, germ = country_teams
# rus = teams2
# por = teams4
# swis, bel, turk, greece, pol, scot, dutch = teams3
#print(country_teams1)


bucket1 = []
bucket1.extend([teams3[6]])
bucket1.extend(teams)
bucket1.extend(teams4)
#print(bucket1)

bucket2 = []
bucket2.extend(teams3)
bucket2.extend(teams2)

for x in bucket1:
    for y in bucket2:
        if x == y:
            bucket2.remove(x)
print(bucket2)


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

print(bucket1)
print(bucket2)

# country1 = [eng, spa, ita, fra, germ, dutch, por]
# country2 = [swis, bel, turk, pol, greece, scot,  rus]
#
# # pick_country = random.choice(country1)
# # pick_team1 = random.choice(pick_country)
# #for i in range(8):
# pick_country = (random.sample(country1, 3))
#
#
# random_country1, random_country2, random_country3  = pick_country
#
#
#
#     # random_country_list1 = [item for sublist in random_country1 for item in sublist]
#     # random_country_list2 = [item for sublist in random_country2 for item in sublist]
#     #flat_list = [item for sublist in pick_country for item in sublist]
#     #print(random_country1)
#     #print(random_country2)
#
# if type(random_country1) is str:
#         pick_team1 = random_country1
# else:
#         pick_team1 = (random.choice(random_country1))
# if type(random_country2) is str:
#         pick_team2 = random_country2
# else:
#         pick_team2 = (random.choice(random_country2))
# if type(random_country3) is str:
#         pick_team3 = random_country3
# else:
#         pick_team3 = (random.choice(random_country3))
# #print(pick_country)
#
# pick_country2 = (random.sample(country2, 1))
# #print(pick_country2)
#
#
# if type(pick_country2) is list:
#     pick_team4 = random.choice(pick_country2)
# else:
#     pick_team4 = pick_country2

# print(pick_team1)
# print(pick_team2)
# print(pick_team3)
# print(pick_team4)








