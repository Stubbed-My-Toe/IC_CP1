import csv
class Student:
    def __init__(self, name, student_id, grades, academic_standing):
        self.name = name
        self.student_id = student_id
        self.grades = grades
        self.academic_standing = academic_standing
    def __str__(self, name, student_id, grades, academic_standing):
        print(f"""Name: {name}
ID: {student_id}
Grade: {grades}
Academic Standing: {academic_standing}
""")

    def save_data(self, name, student_id, grades, academic_standing):
        with open('assignments_pt2/grade_book/docs/student.csv', mode = 'w+', newline ='') as file:
            writer = csv.writer(file)

            writer.writerows(name, student_id, grades, academic_standing)
        
name = input("")
student_id = input("")
grades = input("")
academic_standing = input("")

student = Student(name, student_id, grades, academic_standing)

