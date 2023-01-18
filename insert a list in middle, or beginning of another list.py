listteam = ['por', 'fra', 'por']
groupC = ['eng', 'spa', 'ita', 'germ']

#create unique objects from listteam
uni_team = set()
dup_team = []
for x in listteam:
    if x in uni_team:
        dup_team.append(x)
    else:
        uni_team.add(x)
#print(dup_team)
uni_team = (list(uni_team))


uni_team.append(groupC[0])
groupC.pop(0)
groupC[0:0] = dup_team
print(uni_team)
#print(listteam)
print(groupC)