import pandas as pd

df = pd.DataFrame({
    'Student': ['Vaibhav', 'Rahul', 'Priya', 'Ankit', 'Neha'],
    'Maths': [72, 35, 85, 45, 90],
    'Science': [68, 72, 90, 38, 88],
    'Attendance': [90, 60, 95, 40, 85]
})

df['math_status'] = df['Maths'].map(lambda x:'pass' if x>40 else 'fail')
df['science_status'] = df['Science'].map(lambda x:'pass' if x>40 else 'fail')


df['science_div_10'] = df['Science'].map(lambda x: x/10)

df['attendance_grade'] = df['Attendance'].map(lambda x:'Excellent' if x>90 else('Good' if 75<=x<=90 else 'poor'))

def total(row):
    return row['Maths']+ row['Science']
df['Total'] = df.apply(total,axis=1)

def final_result(row):
    if row['Maths']>=40 and row['Science']>=40 and row['Attendance']>=75:
        return 'Pass'
    else:
        return 'Fail'
df['Final_result'] = df.apply(final_result,axis = 1)

def summary(row):
    return row['Student'] + ':' + 'M-'+ str(row['Maths']) + 'S-' + str(row['Science'])
df['summary'] = df.apply(summary,axis = 1)

print(df)