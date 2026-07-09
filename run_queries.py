import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('happiness.db')

# Query 1: Top 10 Happiest Countries
print("--- Query 1: Top 10 Happiest Countries ---")
q1 = """
SELECT
    Country,
    Happiness_Score,
    GDP,
    Corruption
FROM happiness_report
ORDER BY Happiness_Score DESC
LIMIT 10;
"""
df_q1 = pd.read_sql_query(q1, conn)
print(df_q1)
print("\n" + "="*50 + "\n")

# Query 2: GDP Groups Analysis
print("--- Query 2: GDP Groups vs Happiness & Freedom ---")
q2 = """
SELECT
    CASE
        WHEN GDP >= 10 THEN 'High GDP'
        ELSE 'Low GDP'
    END AS gdp_group,
    AVG(Happiness_Score) AS avg_happiness_score,
    AVG(Freedom) AS avg_freedom
FROM happiness_report
GROUP BY gdp_group;
"""
df_q2 = pd.read_sql_query(q2, conn)
print(df_q2)
print("\n" + "="*50 + "\n")

# Query 3: High Happiness but Low GDP
print("--- Query 3: High Happiness but Low GDP ---")
q3 = """
SELECT
    Country,
    Happiness_Score,
    GDP
FROM happiness_report
WHERE Happiness_Score > (
    SELECT AVG(Happiness_Score)
    FROM happiness_report
)
AND GDP < (
    SELECT AVG(GDP)
    FROM happiness_report
)
ORDER BY Happiness_Score DESC;
"""
df_q3 = pd.read_sql_query(q3, conn)
print(df_q3)

# Close connection
conn.close()
