import random
movies = {
"happy": ["happy 1", "happy 2", "happy 3", "series 1", "new movies"],
"sad" : ["sad 1", "sad 2", "sad 3"],
"neutral" : ["neutral 1", "neutral 2", "neutral 3"],
"standalone":  ["standalone 1", "standalone 2", "standalone 3"],
"series" : ["series 1", "series 2", "series 3", "happy 1", "new movies"],
"action" : ["action 1", "action 2", "action 3", "series 2", "happy 1", "new movies"],
"adventure" : ["adventure 1", "adventure 2", "adventure 3"],
"drama": ["drama 1", "drama 2", "drama 3"]}

Your_mood = input(" Your mood (sad, happy or neutral): ")
movie_type = input("movie type (series or standalone): ")
interested_category = input("category (action, adventure, or drama): ")

import numpy as np
from functools import reduce

#finding the intersection of all three lists
#using for loop
selected_movies=[]
for movie in movies[Your_mood]:
    if movie in movies[movie_type]:
        if movie in movies[interested_category]:
            selected_movies.append(movie)

# using numpy, np
import numpy as np
new_array = np.intersect1d(movies[Your_mood], movies[movie_type])
numpy_movies = np.intersect1d(new_array, movies[interested_category])

#using the reduce function from functools
from functools import reduce
functools_movies = reduce(np.intersect1d, (movies[Your_mood], movies[movie_type], movies[interested_category]))

#using set functions
set_movies=set(movies[Your_mood]).intersection(movies[movie_type], movies[interested_category])

#using list comprehensions
list_comprehesion_movies = [x for x in movies[Your_mood] if x in movies[movie_type] and x in movies[interested_category]]

#using set intersection functions
reduce_movies = set(movies[Your_mood]) & set(movies[movie_type]) & set(movies[interested_category])

watch_movie = random.choice(list_comprehesion_movies)
print(selected_movies)
print(numpy_movies)
print(functools_movies)
print(set_movies)
print(list_comprehesion_movies)
print(reduce_movies)
print(f"You should watch {watch_movie}")

