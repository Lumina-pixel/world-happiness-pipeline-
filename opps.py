class Student:
    def __init__(self,name,num_subjects):
        self.name = name
        self.num_subjects = num_subjects
        self.marks = []
        for i in range(num_subjects):
            while True:
                try:
                    mark = int(input(f"enter subject {i+1} marks: "))
                    self.marks.append(mark)
                    break
                except ValueError:
                    print("invalid input")
            
    def calculate_average(self):
        total = sum(self.marks)
        return total/self.num_subjects
       
    def calculate_grade(self):
        avg = self.calculate_average()
        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=40:
            return "C"
        else:
            return "D"
        
    def display(self):
        print("NAME: ",self.name)
        print("Marks: ",self.marks)
        print("AVERAGE: ",self.calculate_average())
        print("GRADE: ",self.calculate_grade())
    
    def to_file_string(self):
        return f"{self.name},{self.calculate_average()},{self.calculate_grade()}"   
    
students = []

n = int(input("Enter how many students: "))

for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter name: ")
    num_subjects = int(input("Enter subjects: "))

    s = Student(name, num_subjects)
    students.append(s)
    
print("\nSTUDENT REPORT")

for student in students:
    student.display()
    print('\n')

with open("result.txt","w") as f:
    for student in students:
        f.write(student.to_file_string()+'\n') 

with open("toppers.txt","w") as f:
    for student in students:
        if student.calculate_grade()=='A':
            f.write(student.to_file_string()+'\n')

with open("result.txt","r") as f:
    for line in f:
        print(line.strip())

with open("toppers.txt","r") as f:
    for line in f:
        print(line.strip())
    

    