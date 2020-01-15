FILE 1
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

FILE 2
from student import Student

student1 = Student("Justin", "Computer Science", 3.5, False)
student2 = Student("Alana", "Psychology", 3.0, False)

print(student1.name)
print(student2.major)
