import random

class Student:

    educational_platform = "Udemy"

    def __init__(self, name, age=20):
        self.name = name     

    def greet(self):
        print (random.choice([f"Hey there, my name is {self.name} ", f"Hi. Oh, my name is {self.name} ", f"Hi, I'm {self.name} " ]))


s_name=["jon","steve","charlie","ted"]
s = Student(s_name)

for x in s_name:
    setattr(s,"name",x)
    s.greet()