import random

'''A uefa champions league draw simulator. '''
# Reveices input for 32 teams from 14 different conutries'''
# Randomly distribute the teams into groups of 4 without putting teams from same countries in same group

'''global variables '''
num_teams = 32
england = []
france= []
spain = []
germany = []
italy = []
portugal = []
russia = []
dutch = []
turkey = []
swiss = []
scotland = []
greece= []
poland = []
belguim = []

groupA = []
groupB = []
groupC= []
groupD = []
groupE= []
groupF = []
groupG = []
groupH = []

groups = [groupA, groupB, groupC, groupD, groupE, groupF, groupG, groupH]
countries1 = [england, france, spain, germany, italy, portugal, russia]
countries2 =[dutch, turkey, swiss, scotland, greece, poland, belguim]

used = []
loading = 0
tens = 10

print('\tUEFA champions league draw simulator\n')
print('enter teams to make your very own UEFA champions league')
print('press the enter key to begin')

#ask for teams

england += [input('\n Please enter an English team: ')]
england += [input('\n Please enter an English team: ')]
england += [input('\n Please enter an English team: ')]
england += [input('\n Please enter an English team: ')]

spain += [input('\n Please enter an spainish team: ')]
spain += [input('\n Please enter an spainish team: ')]
spain += [input('\n Please enter an spainish team: ')]
spain += [input('\n Please enter an spainish team: ')]

germany += [input('\n Please enter an germany team: ')]
germany += [input('\n Please enter an germany team: ')]
germany += [input('\n Please enter an germany team: ')]
germany += [input('\n Please enter an germany team: ')]

italy += [input('\n Please enter an italy: ')]
italy += [input('\n Please enter an italy: ')]
italy += [input('\n Please enter an italy: ')]
italy += [input('\n Please enter an italy: ')]

france += [input('\n Please enter a french team: ')]
france += [input('\n Please enter a french team: ')]
france += [input('\n Please enter a french team: ')]
france += [input('\n Please enter a french team: ')]

portugal += [input('\n Please enter an portugal team: ')]
portugal += [input('\n Please enter an portugal team: ')]
portugal += [input('\n Please enter an portugal team: ')]

russia += [input('\n Please enter an russia team: ')]
russia += [input('\n Please enter an russia team: ')]

dutch += [input('\n Please enter an dutch team: ')]
turkey += [input('\n Please enter an turkey team: ')]
swiss += [input('\n Please enter an swiss team: ')]
scotland += [input('\n Please enter an scotland team: ')]
greece += [input('\n Please enter an greece team: ')]
poland += [input('\n Please enter an poland team: ')]
belguim += [input('\n Please enter an belguim team: ')]

#make copies
england1 = england[:]
france1 = france[:]
spain1 = spain[:]
germany1 = germany[:]
italy1 = italy[:]
portugal1 = portugal[:]
russia1 = russia[:]
dutch1 = dutch[:]
turkey1 = turkey[:]
swiss1 = swiss[:]
scotland1 = scotland[:]
greece1 = greece[:]
poland1 = poland[:]
belguim1 = belguim[:]

countries3 = [england1, france1, spain1, germany1, italy1, portugal1, russia1]

countries4 = [dutch1, turkey1, swiss1, scotland1, greece1, poland1, belguim1]




while num_teams != 7:
    x = 0
    position = random.randrange(len(countries1))
    country = countries1[position]
    country1 = countries3[position]
    if country:
        team = random.choice(country1)
        if team not in used:
            group = random.choice(groups)
            if len(group) < 4:
                for i in group:
                    if i not in country:
                        x += 0
                    else:
                        x += 1
                if x == 0:
                    group += [team]
                    num_teams -= 1
                    used += [team]
                    country1.remove(team)
                    loading += 1
                    if loading == tens:
                        print("\n loading... \n")
                        tens += 10
while num_teams != 0:
    x = 0
    position = random.randrange(len(countries2))
    country = countries2[position]
    country1 = countries4[position]
    if country1:
        team = random.choice(country1)
        if team not in used:
            group = random.choice(groups)
            if len(group) < 4:
                for i in group:
                    if i not in country:
                        x +=0
                    else:
                        x += 1
                if x == 0:
                    group += [team]
                    num_teams -= 1
                    used += [team]
                    country1.remove(team)
                    loading+=1
                    if loading == tens:
                        print("\n loading... \n")
                        tens += 10

#display groups
print('\n Assembling groups... \n')
input('groups complete. Press the enter key to view.')
print("\n GroupA")
print(groupA[0])
print(groupA[1])
print(groupA[2])
print(groupA[3])