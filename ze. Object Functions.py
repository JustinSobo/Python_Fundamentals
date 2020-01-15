FILE 1

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


FILE 2

from student import Student

student1 = Student("Justin", "Computer Science", 3.5)
student2 = Student("Alana", "Psychology", 3.0)

print(student1.on_honor_role())
