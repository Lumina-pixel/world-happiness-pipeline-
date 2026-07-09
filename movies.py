import pandas as pd

df = pd.DataFrame({
    'Title': [
        'Inception',
        'The Dark Knight',
        'Titanic',
        'Interstellar',
        'Cars',
        'Avengers: Endgame'
    ],
    'Year': [
        2010,
        2008,
        1997,
        2014,
        2006,
        2019
    ],
    'Rating': [
        8.8,
        9.0,
        7.9,
        8.7,
        7.2,
        8.4
    ],
    'Genre': [
        'Sci-Fi',
        'Action',
        'Romance/Drama',
        'Sci-Fi',
        'Animation',
        'Action/Sci-Fi'
    ]
})

df.to_csv('movies.csv',index = False)
# iloc
print(df.iloc[0])        # pehli movie
print('\n')
print(df.iloc[0:3])      # pehli 3 movies
print('\n')
print(df.iloc[0, 0])     # pehli movie ka title
print('\n')

# loc
print(df.iloc[:4][['Title','Rating']])           # pehli movie ka title
print('\n')
print(df.loc[2:4, ['Title','Rating']]) # rows 2 to 4, sirf Title aur Rating
