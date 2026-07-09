import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("WHR2023.csv")
df = df.rename(columns={
    'Country name': 'Country',
    'Ladder score': 'Happiness_Score',
    'Logged GDP per capita': 'GDP',
    'Social support': 'Social_Support',
    'Healthy life expectancy': 'Life_Expectancy',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption'
})
print(df['GDP'].mean())
print(df['GDP'].std())
print(df['GDP'].min())
print(df['GDP'].max())