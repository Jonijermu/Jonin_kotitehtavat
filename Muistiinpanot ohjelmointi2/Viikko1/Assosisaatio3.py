class Student:

    def __init__(self, name):
        self.name = name
        self.courses = []

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def ilmoita_kurssille(self, student):
        self.students.append(student)
        student.courses.append(self)

student1 = Student("Masa")
student2 = Student("Jari")
student3 = Student("Okkko")


course1 = Course("fysiikka")
course2 = Course("matikka")
course3 = Course("python")

course1.ilmoita_kurssille(student1)
course2.ilmoita_kurssille(student2)
course3.ilmoita_kurssille(student3)
course3.ilmoita_kurssille(student1)


for course in student1.courses:
    print(course.name)

for student in course1.students:
    print(student.name)
for student in course2.students:
    print(student.name)

