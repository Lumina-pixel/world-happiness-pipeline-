students = []

n = int(input("enter number of students: "))
num = int(input("enter number of subjects: "))

for i in range(n):
    print(f"{i+1} student: ")
    name = input("enter name: ")
    total = 0

    for j in range(num):
        marks = int(input(f"enter marks for {name}: "))
        total = total+marks

    average = total/num

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    students.append({
        "Name": name,
        "Average": average,
        "grade": grade
    })

with open("result.txt","w") as f:
    for student in students:
        f.write(f"{student['Name']},{student['Average']},{student['grade']}\n")

with open("result.txt", "r") as f:
    print(f.read())


toppers = [student for student in students if student['grade'] in ['A','B']]
with open("topper.txt","w") as f:
    for student in toppers:
        f.write(f"{student['Name']},{student['Average']},{student['grade']}\n")


with open("topper.txt", "r") as f:
    print(f.read())