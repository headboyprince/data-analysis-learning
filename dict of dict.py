import random

'''class of living things'''

animals = {
    "land_animals":{

        "mammals":["humans", "cat", "dog", "horse", "monkeys", "donkey", "lion"],
           "reptiles":["lizard"],
           "insects":["bettle", "roaches", "ants","flies"]},

"non_land_animals":{
    "bird":["owl", "eagle", "pigeon", "cock"],
    "amphibians":["frog", "toad"],
"fish":["whale", "shark", "crabs", "shrimps", "crocodile", "turtle"]
}
}


print_animal = (animals["land_animals"].keys())
print_animal_key = [key for key in print_animal]
print_animal_key = random.sample(print_animal_key, 2)
print(print_animal_key)

figure1= print_animal_key

print(figure1)

select_random_animal = (animals["land_animals"][f'{figure1}'])
select_random_animals = random.choice(select_random_animal)
print(select_random_animals)

#function for accepting values and chaning the

# def nested_dict(element, value, *keys):
    # if type(element) is not dict:
    #     raise AttributeError('nested_set() expects dict as first argument')
    # if len(keys) <2:
    #     raise AttributeError           ('nested_set() expects at least three arguments, not enough given')
    #
    # _keys = keys[:-1]
    # _element = element
    # for key in keys:
    #     _element = _element[key]
    # _element[keys[-1]] = value

