import string
import random

# groups = []
# for i in (string.ascii_uppercase):
#     groups.append(f'Group{i}')
#     if len(groups) == 8:
#         break
#
# print(groups)
groups = []
group_list = []
for i in (string.ascii_uppercase):
    group_list.append(f'Group{i}')
    if len(group_list) == 8:
        break
for n in range(8):
    random_number1 = random.randint(0, 100)
    #print(random_number1)
    random_number2 = random.randint(100, 200)
    #print(random_number2)

    print(group_list[n])
    groups = group_list
    groups[n] = []
    #print(groups)
    groups[n].extend([random_number1, random_number2])
    print(groups[n])
