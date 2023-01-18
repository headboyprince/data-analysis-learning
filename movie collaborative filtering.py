import pandas as pd

df = pd.read_csv('moviesdata.csv')
split = pd.DataFrame(df['genre'].to_list(), columns = ['genre1', 'genre2', 'genre3'])
print(split)
print(df)