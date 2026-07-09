import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv('WHR2023.csv')

# Rename columns
df = df.rename(columns={
    'Country name': 'Country',
    'Ladder score': 'Happiness_Score',
    'Logged GDP per capita': 'GDP',
    'Social support': 'Social_Support',
    'Healthy life expectancy': 'Life_Expectancy',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption'
})

top10 = df.head(10)

plt.figure(figsize=(8,5))

plt.plot(top10['Country'],
         top10['GDP'],
         linestyle = '--',
         marker='o',
         label='GDP')

plt.plot(top10['Country'],
         top10['Happiness_Score'],
         marker='s',
         label='Happiness Score',color = 'red')

plt.title("Top 10 Countries: GDP vs Happiness")
plt.xlabel("Country")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend() 
plt.tight_layout()



fig, axes = plt.subplots(1, 2, figsize=(12,5))

axes[0].bar(top10['Country'],
            top10['GDP'])

axes[0].set_title('GDP by Country')
axes[0].tick_params(axis='x', rotation=45)


axes[1].scatter(top10['Country'],
            top10['Happiness_Score'])

axes[1].set_title('Happiness Score by Country')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()

plt.show()
plt.show()

plt.hist(df['GDP'],bins=10)
plt.show()


corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(18,15))

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",      
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

sns.barplot(x='Country',y = 'Happiness_Score', data = top10)
plt.xticks(rotation=45)
plt.show()
'''
print(bottom10[['Ladder score','Country name']])

plt.bar(bottom10['Country name'],bottom10['Ladder score'])

plt.figure(figsize=(8,6))

plt.scatter(df['Freedom'],df['Happiness_Score'])


plt.hist(df['Corruption'],bins=10)
plt.show()

top10 = df.head(10)

fig, axes = plt.subplots(1,2, figsize=(12,5))

axes[0].bar(top10['Country'], top10['Happiness_Score'])
axes[0].set_title('Happiness')

axes[1].scatter(df['GDP'], df['Happiness_Score'])
axes[1].set_title('GDP vs Happiness')

plt.bar(top10['Country'], top10['Happiness_Score'], color='green')
plt.plot(0,1,color='red', linestyle='--', marker='o')
'''
plt.show()

