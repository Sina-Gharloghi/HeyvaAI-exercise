# __repr__ method

class Patient:
    def __init__(self, name, lname, weight, age, state):
        self.name = name
        self.lname = lname
        self.weight = weight
        self.age = age
        self.state = state

    def __repr__(self):
        print (f"{self.name} has {self.state} situation")

p1 = Patient("john", "kenedy", 70, 58, "Critical")

p1.__repr__()
    