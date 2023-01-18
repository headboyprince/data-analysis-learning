listteam = ['por', 'fra', 'por']
groupA = ['dutch', 'por', 'spa', 'ita']
groupB = ['eng', 'ita', 'fra', 'germ']
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

#check to see common elements
group = [groupA, groupB, groupC]
for i in group:
    check = bool(set(listteam).intersection(i))
    print(check)

#check if any group has matching elements and print group
check = bool(set(listteam).intersection(groupA))
if check == False:
    print(f'groupA is {groupA}')
    for a in groupA:
        for b in listteam:
            a, b = b, a
    print(groupA)
else:
    check = bool(set(listteam).intersection(groupB))
    if check == False:
        print(f'groupB is {groupB}')
    else:
        check = bool(set(listteam).intersection(groupC))
        if check == False:
            #print(f'groupC is {groupC}')

            #swap the duplicated team into groupC
            uni_team.append(groupC[0])
            groupC.pop(0)
            groupC[0:0] = dup_team
            print(uni_team)

            print(listteam)
            print(groupC)
        else:
            ("no group is free")







#loop over multiple list and return true if matches

