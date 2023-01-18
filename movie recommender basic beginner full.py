import random
from itertools import chain, repeat
import numpy as np

#create  a list of movies
movies ={
"happy": ["The Shawshank Redemption -1994", "Schindler's List -1993",
                "The Godfather -1972", "Schindler's List -1993","12 Angry Men -1957",
                "The Lord of the Rings: The Return of the King -2003","Casablanca -1942",
                "The Godfather: Part II -1974","Star Wars -1977"],
"sad": ["The Godfather -1972", "The Godfather: Part II -1974", "The Dark Knight -2008",
               "One Flew Over the Cuckoo's Nest -1975","Shichinin no samurai -1954","Fight Club -1999",
               "Cidade de Deus -2002"],

"neutral":  ["Il buono il brutto il cattivo. -1966 ", "Pulp Fiction -1994",
                  "Star Wars: Episode V - The Empire Strikes Back -1980 ","Goodfellas -1990",
                  "Il buono il brutto il cattivo. -1966"],

"series": ["The Godfather: Part II -1974", "Schindler's List -1993", "Pulp Fiction -1994",
                 "The Godfather -1972", "One Flew Over the Cuckoo's Nest -1975",
                 "Star Wars: Episode V - The Empire Strikes Back -1980 ",
                 "Shichinin no samurai -1954","Goodfellas -1990","Fight Club -1999",
                 "The Lord of the Rings: The Fellowship of the Ring -2001"],

"standalone": ['The Shawshank Redemption -1994', 'Il buono il brutto il cattivo. -1966',
                     "12 Angry Men -1957","The Dark Knight -2008",
                     "The Lord of the Rings: The Return of the King -2003",
                     "Star Wars -1977","Casablanca -1942","Cidade de Deus -2002",
                     "Rear Window -1954"],

"action": ["The Lord of the Rings: The Fellowship of the Ring -2001","Star Wars -1977 ",
                "Star Wars: Episode V - The Empire Strikes Back -1980 ","Rear Window -1954"
                "The Dark Knight -2008","The Shawshank Redemption -1994",
                "The Lord of the Rings: The Return of the King -2003",
                "Pulp Fiction -1994"],
"adventure": ["One Flew Over the Cuckoo's Nest -1975","Casablanca -1942",
                   "Shichinin no samurai -1954","The Godfather -1972",
                   "The Godfather: Part II -1974",
                   "Inception -2010"],

"drama": ["Goodfellas -1990","Fight Club -1999","Schindler's List -1993",
               "12 Angry Men -1957","Cidade de Deus -2002",
               "Il buono il brutto il cattivo. -1966 "]
}

mood = 'sad', 'happy', 'neutral'
type = 'series', 'standalone'
category = 'adventure', 'action', 'drama'


#ask_question functionhandles input from the user, strips out spaces and make it all lower and then append it to a list
all_replies_by_user= []


def ask_question(input_interest, question):
    prompts = chain([question], repeat(f"Sorry: your input is not one of {input_interest}! Try again: "))
    replies = map(input, prompts)
    lowercased_replies = map(str.lower, replies)
    stripped_replies = map(str.strip, lowercased_replies)
    question_input_cleaned = next(filter(input_interest.__contains__, stripped_replies))
    all_replies_by_user.append(question_input_cleaned)
    print(question_input_cleaned)

#calling the ask_question function and passing the required parameters
[ask_question(*item) for item in ((mood, "what mood are you in? happy, sad, neutral?: "),
                                  (type, "do you want to watch stand-alone or series?: "),
                                  (category, "do you want to watch adventure, action, or drama?: "))]



Your_mood = all_replies_by_user[0]
movie_type = all_replies_by_user[1]
interested_category = all_replies_by_user[2]
#input moood using the intertools function

#
# prompts = chain(["what mood are you in? happy, sad, neutral?: "], repeat(f"Sorry: your input is not one of {mood}! Try again: "))
# replies = map(input, prompts)
# lowercased_replies = map(str.lower, replies)
# stripped_replies = map(str.strip, lowercased_replies)
# Your_mood = next(filter(mood.__contains__, stripped_replies))
# print(Your_mood)


# prompts = chain(["do you want to watch stand-alone or series?: "], repeat(f"Sorry: your input is not one of {type} Try again: "))
# replies = map(input, prompts)
# lowercased_replies = map(str.lower, replies)
# stripped_replies = map(str.strip, lowercased_replies)
# movie_type = next(filter(type.__contains__, stripped_replies))
# print(movie_type)



# prompts = chain(["do you want to watch adventure, action, or drama?: "], repeat(f"Sorry: your input is not one of {category} Try again: "))
# replies = map(input, prompts)
# lowercased_replies = map(str.lower, replies)
# stripped_replies = map(str.strip, lowercased_replies)
# interested_category = next(filter(category.__contains__, stripped_replies))
# print(interested_category)

selected_movies=[]

for movie in movies[Your_mood]:
    if movie in movies[movie_type]:
        if movie in movies[interested_category]:
            selected_movies.append(movie)

#using numpy tool
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

#check if no movie exists that match user input
if len(selected_movies) < 1:
    print("no movie found, choose another movie type, or interested category")
else:
    watch_movie = random.choice(selected_movies)
    print(f"You should watch {watch_movie}")
print(selected_movies)
print(numpy_movies)
print(functools_movies)
print(set_movies)
print(list_comprehesion_movies)
print(reduce_movies)


