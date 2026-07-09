import pandas as pd

df = pd.read_csv('WHR2023.csv')

# Missing values fill karo median se
df['Healthy life expectancy'] = df['Healthy life expectancy'].fillna(df['Healthy life expectancy'].median())
df['Explained by: Healthy life expectancy'] = df['Explained by: Healthy life expectancy'].fillna(df['Explained by: Healthy life expectancy'].median())
df['Dystopia + residual'] = df['Dystopia + residual'].fillna(df['Dystopia + residual'].median())

# Columns rename karo — names bohot lame hain
df = df.rename(columns={
    'Country name': 'Country',
    'Ladder score': 'Happiness_Score',
    'Logged GDP per capita': 'GDP',
    'Social support': 'Social_Support',
    'Healthy life expectancy': 'Life_Expectancy',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption'
})
'''
print(df.shape)
print(df.isnull().sum().sum())  # 0 hona chahiye
print(df.head())

print('\n')
print(df[['Country','Corruption']].sort_values(by = 'Corruption',ascending = False).head(10))

print('\n')
gdp_sc=df.sort_values(by = 'GDP',ascending = False).head(10)
print(gdp_sc[['Country','GDP','Happiness_Score']].sort_values(by='Happiness_Score'))

print('\n')
avg_sc = df['Happiness_Score'].median().sum()
print(avg_sc)
print(df[df['Happiness_Score']>avg_sc])

print('\n')
freedom_sc = df.sort_values(by='Freedom',ascending = False).head(50)
free = freedom_sc[['Country','Freedom','Happiness_Score']].sort_values(by = 'Happiness_Score')
print(free)

print('\n')
incnpk = df[df['Country'].isin(['India', 'China', 'Pakistan'])][
    ['Country', 'Happiness_Score', 'GDP', 'Freedom', 'Corruption']
].set_index('Country')
 
incnpk['Greater_than_average_happiness'] = incnpk['Happiness_Score'].map(lambda x: 'True' if x>avg_sc else 'False')
print(incnpk)
'''




