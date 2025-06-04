

# answer_1 = input("what is the color of a apple \n(a)Red \n(b)Yellow \n(c)Orange \n")
# answer_2 = input("what is the color of a orange \n(a)Red \n(b)Yellow \n(c)Orange \n")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def agef(self):
        if self.age > 25 :
            print("ur old")
    
    def pri(self):
        print("hrid pco")

class pre_student(Student):
    def make(self):
        print("make")

st2 = pre_student("name", 35)
st2.pri()