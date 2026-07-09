import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Rohan", "Isha", "Kabir", "Meera", "Vihaan", "Anaya", "Arjun", "Sara"],
    "Age": [23, 31, 19, 27, 35, 29, 22, 24, 40, 21],
    "Country": ["India", "USA", "India", "UK", "India", "USA", "UK", "India", "USA", "UK"],
    "Score": [85, 92, 78, 88, 95, 80, 76, 89, 90, 84],
    "Hours_Studied": [5, 6, 3, 4, 7, 4, 3, 5, 6, 4]
}

df = pd.DataFrame(data)

print(df.iloc[:5])
print('\n')
print(df.iloc[-5:])

print('\n')
print(df.shape)

print('\n')
print(df.columns)

print('\n')
print(df['Age'])

print('\n')
print(df[['Name','Age','Country']])

print('\n')
print(df.iloc[:10])

print('\n')
print(df.loc[:4,'Age'])

print('\n')
print(df[df['Age']>30])

print('\n')
print(df[df['Country']=='India'])

print('\n')
print(df.loc[5,'Age'])

print('\n')
average_sc = df.Score.median()
print(df[df['Score']>average_sc])

