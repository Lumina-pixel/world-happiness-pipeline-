import pandas as pd

employees = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4, 5],
    'Name': ['Amit', 'Sara', 'Raj', 'Priya', 'Karan'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR']
})

salaries = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 6, 7],
    'Salary': [75000, 45000, 85000, 60000, 50000]
})

new_employees = pd.DataFrame({
    'Emp_ID': [6, 7],
    'Name': ['Neha', 'Vikas'],
    'Department': ['IT', 'Finance']
})

df = employees.rename(columns = {
    'Emp_ID' : 'ID',
   'Name' : 'Employee_Name',
   'Department' : 'Dept'
})

print(df)

print('\n')
combined_emp = pd.concat([new_employees,employees],ignore_index = True)
print(combined_emp)

print('\n')
inner_emp = pd.merge(employees,salaries,on = 'Emp_ID',how = 'inner')
print(inner_emp.Name)

print('\n')
left_emp = pd.merge(employees,salaries,on = 'Emp_ID',how = 'left')
print(left_emp['Salary'].isnull().sum())

print('\n')
left_emp['Salary'] = left_emp['Salary'].fillna(left_emp['Salary'].mean())
print(left_emp)