import pandas as pd

df = pd.read_csv('cricket.csv')

max_match = df['Matches'].idxmax()
print(df.loc[max_match,'Player'])

print(df.Average.median())

print('\n')
print(df.Role.value_counts())

print('\n')
print(df.Runs.sum())

print('\n')
df["Average_grade"] = df["Average"].map(
    lambda x: "Legend" if x >= 50 else ("Great" if x >= 40 else "Good")
)

print(df)