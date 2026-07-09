import pandas as pd

df = pd.read_csv('cricket.csv')

print(df.iloc[:4])
print('\n')

print(df[['Player','Runs']])

print('\n')
print(df.shape)

print('\n')
print(df.Runs.describe())

print('\n')
print(df[df['Role']=='Batsman'])

print('\n')
print(df[df['Runs']>10000])

print('\n')
print(df[(df['Matches']>300) & (df['Average']>45)])

print('\n')
print(df.iloc[:3,4])

print('\n')
print(df.loc[df['Player']=='Virat','Average'])

print('\n')
print(df.loc[df['Average']>45,['Player','Average']])

print('\n')
data = (df.loc[df['Matches']>200])
print(data.sort_values(by='Average',ascending = False))

print('\n')
unique_roles = df.Role.value_counts()
print(unique_roles)

print('\n')
df['Runs_in_thousands'] = df['Runs'].map(lambda x: x/1000)
print(df[['Player', 'Runs', 'Runs_in_thousands']])

# Average ko round karo 1 decimal pe
print('\n')
df['Average_rounded'] = df['Average'].map(lambda x: round(x, 1))
print(df[['Player', 'Average', 'Average_rounded']])

print('\n')
# Sabse zyada runs wale player ka naam
best_idx = df['Runs'].idxmax()
print(df.loc[best_idx, 'Player'])

# Sabse kam average wala
worst_idx = df['Average'].idxmin()
print(df.loc[worst_idx, 'Player'])