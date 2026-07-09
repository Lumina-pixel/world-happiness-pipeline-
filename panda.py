import pandas as pd

df = pd.read_csv("whatever.csv")

# Sirf naam aur maths marks dikhao jinka maths 70+ ho
print(df[df['Maths'] > 70][['Name', 'Maths']])
print('\n')
# Jinka Science 80 se zyada ho
print(df[df['Science'] > 80])
print('\n')
# Multiple conditions - Maths > 70 AND Science > 80
print(df[(df['Maths'] > 70) & (df['Science'] > 80)][['Name','English']])
print('\n')
# Maths > 70 OR English > 80
print(df[(df['Maths'] > 70) | (df['English'] > 80)])