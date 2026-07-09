import pandas as pd
import numpy_test as np

df = pd.DataFrame({
    'Student': ['Vaibhav', 'Rahul', 'Priya', None, 'Neha', 'Rahul'],
    'Maths': [72, None, 85, 45, None, None],
    'Science': [68, 72, None, 38, 88, 72],
    'City': ['Delhi', 'Mumbai', None, 'Delhi', 'Mumbai', 'Mumbai']
})

print(df.isnull().sum())

print('\n')
print(df[df.Maths.isnull()])

print('\n')
df.Maths = df['Maths'].fillna(df['Maths'].mean())

print('\n')
df.Science = df['Science'].fillna(df['Science'].median())

print('\n')
df.City = df.City.fillna('Unknown')


print('\n')
df.Student = df.Student.fillna('Unknown')


print('\n')
print(df.duplicated().sum())

dupes = df.drop_duplicates()

print("\nFinal Cleaned DataFrame:")
print(dupes)