# 👉write a programe to override super class comstructor and method
#   in sub class

class teacher:
    def __init__(self):
        self.id = 1001

    def display(self):
        print("Teachers id=",self.id)

class student(teacher):
    def __init__(self):
        self.id = 1

    def display(self):
        print("Student id",self.id)

s = student()
s.display()


#output:-
# Student id 1


