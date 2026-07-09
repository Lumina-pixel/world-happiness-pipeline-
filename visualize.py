import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the charts directory if it doesn't exist
os.makedirs('charts', exist_ok=True)

# Connect to the database
conn = sqlite3.connect('happiness.db')

# --- Plot 1: Top 10 Happiest Countries ---
print("Generating Plot 1 (Top 10 Happiest)...")
q1 = """
SELECT Country, Happiness_Score 
FROM happiness_report 
ORDER BY Happiness_Score DESC 
LIMIT 10;
"""
df_q1 = pd.read_sql_query(q1, conn)

plt.figure(figsize=(10, 6))
sns.barplot(data=df_q1, x='Country', y='Happiness_Score', palette='viridis')
plt.title('Top 10 Happiest Countries (2023)', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/top10_happiness.png', dpi=300)
plt.close()

# --- Plot 2: GDP Groups vs Happiness & Freedom ---
print("Generating Plot 2 (GDP Group Comparison)...")
q2 = """
SELECT
    CASE WHEN GDP >= 10 THEN 'High GDP' ELSE 'Low GDP' END AS gdp_group,
    AVG(Happiness_Score) AS avg_happiness,
    AVG(Freedom) AS avg_freedom
FROM happiness_report
GROUP BY gdp_group;
"""
df_q2 = pd.read_sql_query(q2, conn)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot Avg Happiness
sns.barplot(data=df_q2, x='gdp_group', y='avg_happiness', ax=axes[0], palette='Blues_r')
axes[0].set_title('Average Happiness Score', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Happiness Score')
axes[0].set_xlabel('GDP Group')

# Plot Avg Freedom
sns.barplot(data=df_q2, x='gdp_group', y='avg_freedom', ax=axes[1], palette='Oranges_r')
axes[1].set_title('Average Freedom Score', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Freedom Score')
axes[1].set_xlabel('GDP Group')

plt.suptitle('GDP Group Comparison: Happiness vs Freedom', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/gdp_groups_comparison.png', dpi=300)
plt.close()

# --- Plot 3: GDP vs Happiness with Outliers Highlighted ---
print("Generating Plot 3 (GDP vs Happiness Scatter)...")
# Get all data
q_all = "SELECT Country, GDP, Happiness_Score FROM happiness_report;"
df_all = pd.read_sql_query(q_all, conn)

# Get outliers (High happiness, low GDP)
q_outliers = """
SELECT Country, GDP, Happiness_Score 
FROM happiness_report 
WHERE Happiness_Score > (SELECT AVG(Happiness_Score) FROM happiness_report)
  AND GDP < (SELECT AVG(GDP) FROM happiness_report);
"""
df_outliers = pd.read_sql_query(q_outliers, conn)

plt.figure(figsize=(10, 6))
# Plot all countries in grey
sns.scatterplot(data=df_all, x='GDP', y='Happiness_Score', color='grey', alpha=0.5, label='Normal Countries')

# Plot outliers in red (larger size)
sns.scatterplot(data=df_outliers, x='GDP', y='Happiness_Score', color='red', s=100, edgecolor='black', label='Outliers (High Happiness, Low GDP)')

# Annotate some outlier countries
for idx, row in df_outliers.iterrows():
    plt.annotate(row['Country'], (row['GDP'] + 0.05, row['Happiness_Score'] + 0.02), fontsize=9)

plt.title('GDP vs Happiness: Highlighting the Outliers', fontsize=14, fontweight='bold')
plt.xlabel('Logged GDP per Capita')
plt.ylabel('Happiness Score')
plt.legend()
plt.tight_layout()
plt.savefig('charts/gdp_vs_happiness_outliers.png', dpi=300)
plt.close()

# Close database connection
conn.close()
print("All plots generated and saved in the 'charts/' folder!")
