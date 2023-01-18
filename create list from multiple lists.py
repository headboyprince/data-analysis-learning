#generate a new dict oor from each country(eng, spa etc)
# and add all country elements to it
#the new dict or list will be the name of teh country

teams1 =['eng1', 'eng2', 'eng3', 'eng4', #a list with 4 elements
         'spa1', 'spa2', 'spa3', 'spa4',
         'ita1', 'ita2', 'ita3', 'ita4',
         'fra1', 'fra2', 'fra3', 'fra4',
         'port1', 'port2', 'port3', 'port4',
         'germ1', 'germ2', 'germ3', 'germ4']

teams2 = ['dutch1', #a list wih 2 elements
          'dutch2']

teams3 = ['swis1', #a list with 1 element
          'bel1',
          'turk1',
          'rus1',
          'pol1',
          'scot1',
          'grec1']

countryteams = ''
con = []
for country in teams1:
    for i in country:
        if i not in "1234":
            countryteams+=i

    if countryteams not in con:
        con[countryteams].append(country)

print(con)

print(con)

