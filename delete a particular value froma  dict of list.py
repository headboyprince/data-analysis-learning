
dict = {"PES": ["pes 2022", "pes 2023"],
        "FIFA": ["fifa 2022", "fifa 2023"], "call_of_duty": [], "empty_group": []}


del dict["call_of_duty"]
print(dict)
#loop over a dict and delete the empty dict
dict = {key: value for key, value in dict.items() if len(value) != 0}



#delete a particular element from the dict
for i in range(0, len(dict) - 1):
        if dict['PES'][i] == 'pes 2022':
                del dict['PES'][i]
                break

print(dict)