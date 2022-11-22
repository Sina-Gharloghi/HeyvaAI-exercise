# __bool__

class Patient:
    def __init__(self, name, lname, weight, age, state):
        self.name = name
        self.lname = lname
        self.weight = weight
        self.age = age
        self.state = state

    def __repr__(self):
        print (f"{self.name} has {self.state} situation")

    def __bool__(self):
        return bool(self.age) and not (self.age < 0)

p1 = Patient("john", "kenedy", 70, 58, "Critical")
p2 = Patient("john", "kenedy", 70, -10, "Critical")

print (bool(p1), "\n", bool(p2))

    
