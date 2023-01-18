lis = ['Date', 'product', 'price']

dict = {'Date': 'today', 'salary': 'five thousand', 'product': 'toys', 'price': '10 dollars', 'saleman': 'smith'}

dict1 = {"PES": ["pes 2022", "pes 2023"],
        "FIFA": ["fifa 2022", "fifa 2023"], "call_of_duty": [], "empty_group": []}

#compare list with dict keys, if it match create a new dict with dict keys and list as values
n = {}
for k, v in dict.items():
    for i in lis:
        if i == k:
            n[k] = v

print(n)

#compare list with dict keys, if it match create a new dict with list as values and dictkeys as keys
new_dict = {}
lis_value = ['today', 'toys', 'smith']
for v, k in dict.items():
    for i in lis:
        if i == v:
            new_dict[k]= v

#compare list with dict values, if it match create a new dict with list as values and dictkeys as keys
new_dict1 = {}
lis_value1 = ['pes 2022', 'fifa 2023']
for k, v in dict1.items():
    for i in lis_value1:
        if i in v:
            new_dict1[k]= i
    # for i in lis_value:
    #     if i in v:
    #         new_dict[k]= v
print(new_dict1)

#get the keys of a dict as a list
dictkeys = list(new_dict1.keys())
print(dictkeys)