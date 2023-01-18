my_list = []

for i in range(11):
    complex_list = f'{i} + {i}i'
    my_list.append(complex_list)
print(complex_list)
print(my_list)

list_comprehension_complex = [f'{i} + {i}i' for i in range(11)]
print(list_comprehension_complex)
