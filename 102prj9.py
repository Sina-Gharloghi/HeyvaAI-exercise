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

    def __eq__(self,other):
        return True

p1 = Patient("john", "kenedy", 70, 58, "Critical")
p2 = Patient("john", "kenedy", 70, 58, "Critical")

print (p1==p2)

    
