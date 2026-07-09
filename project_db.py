import sqlite3
import pandas as pd

# 1. Load and clean data (from WHR2023.csv)
df = pd.read_csv('WHR2023.csv')

# Fill missing values
df['Healthy life expectancy'] = df['Healthy life expectancy'].fillna(df['Healthy life expectancy'].median())
df['Explained by: Healthy life expectancy'] = df['Explained by: Healthy life expectancy'].fillna(df['Explained by: Healthy life expectancy'].median())
df['Dystopia + residual'] = df['Dystopia + residual'].fillna(df['Dystopia + residual'].median())

# Rename columns to make them clean for SQL
df = df.rename(columns={
    'Country name': 'Country',
    'Ladder score': 'Happiness_Score',
    'Logged GDP per capita': 'GDP',
    'Social support': 'Social_Support',
    'Healthy life expectancy': 'Life_Expectancy',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption'
})

# 2. Connect to SQLite (creates happiness.db file automatically)
conn = sqlite3.connect('happiness.db')

# 3. Save DataFrame to SQL Table 'happiness_report'
df.to_sql('happiness_report', conn, if_exists='replace', index=False)
print("Database 'happiness.db' created and populated successfully!")

# 4. Test Query: Check if we can read from it using SQL
query = """
SELECT Country, Happiness_Score, GDP 
FROM happiness_report 
LIMIT 5;
"""
df_from_sql = pd.read_sql_query(query, conn)
print("\nTest SQL Query Output:")
print(df_from_sql)

# Close connection
conn.close()
