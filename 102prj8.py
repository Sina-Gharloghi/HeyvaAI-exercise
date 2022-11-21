# __format__

class Patient:
    def __init__(self, name, lname, weight, age, state):
        self.name = name
        self.lname = lname
        self.weight = weight
        self.age = age
        self.state = state

    def __repr__(self):
        print (f"{self.age} years old {self.name} {self.lname} has {self.state} situation")
    
    def __format__(self, format_spec):
        if format_spec == "short":
            print (f"{self.name} - {self.state}")

a = input ("If you want short info press 's' : ")
p1 = Patient("john", "kenedy", 70, 58, "Critical")

if a == "s":
    p1.__format__("short")
else:
    p1.__repr__()
    