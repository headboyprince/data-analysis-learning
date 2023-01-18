import random
import string

'''class of living things'''

mammals = ["humans", "cat", "dog", "horse", "monkeys", "donkey", "lion"]
bird = ["owl", "eagle", "pigeon", "cock"]
insects = ["bettle", "roaches", "ants","flies"]
amphibians = ["frog", "toad"]
reptiles = ["lizard"]
fish = ["whale", "shark", "crabs", "shrimps", "crocodile", "turtle"]
#animals put into different bucket
land_animals = [insects, mammals, reptiles]
non_land_animals = [fish, bird, amphibians]
#select 2 random type of list of animal from the land and non land animals
for group in range(6):
    random_land=(random.sample(land_animals, 2))
    random_non_land = (random.sample(non_land_animals, 2))

    figure1, figure2 = random_land
    figure3, figure4 = random_non_land

    pick_animal1 = random.choice(figure1)
    pick_animal2 = random.choice(figure2)
    pick_animal3 = random.choice(figure3)
    pick_animal4 = random.choice(figure4)

    # for i in range(0, len(land_animals) - 1):
    #     if land_animals[f'{figure1}'][i] == f'{pick_animal1}':
    #         del land_animals[f'{figure1}'][i]
    #         break
#lete an empty list from the dict
    print(f'group'f'{group+1}')
    group = []
    group.append([pick_animal1, pick_animal2, pick_animal3, pick_animal4])

    print(group)
print(land_animals[insects])





