import pandas as pd

df = pd.DataFrame({
    'Employee': ['Amit', 'Sara', 'Raj', 'Priya', 'Karan', 'Neha', 'Vikas', 'Pooja'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [75000, 45000, 85000, 60000, 50000, 70000, 65000, 48000],
    'Experience': [5, 3, 7, 4, 2, 6, 5, 3],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai']
})
'''
print(df.sort_values(by='Salary',ascending = False))

print('\n')
print(df.sort_values(by='Experience'))

print('\n')
print(df.sort_values(by=['Department','Salary']))

print('\n')
print(df.groupby('Department')['Salary'].mean())

print('\n')
print(df.groupby('City')['Salary'].sum())

print('\n')
print(df.groupby('Department')['Employee'].count())
'''
print('\n')
print(df.groupby('Department')['Salary'].agg(['max','min']))

print('\n')
average_sal = df.groupby('Department')['Salary'].mean()
print(average_sal.sort_values())

print('\n')
print(df[df['Department'] == 'HR'].sort_values(by='Salary'))

print('\n')
print(df.groupby('City')['Experience'].mean())
