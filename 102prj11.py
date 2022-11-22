# __gt__ method

class Patient:
    def __init__(self, name, lname, weight, age, state):
        self.name = name
        self.lname = lname
        self.weight = weight
        self.age = age
        self.state = state

    def __repr__(self):
        print (f"{self.name} has {self.state} situation")

    def __gt__(self,other):
        if not isinstance(other, Patient):
            return False
        else:
            print (self.age > other.age)

    def __lt__(self,other):
        if not isinstance(other, Patient):
            return False
        else:
            print (self.weight > other.weight)

p1 = Patient("John", "Kenedy", 70, 105, "Critical")
p2 = Patient("George", "Washington", 90, 290, "Critical")

p1.__gt__(p2)
p2.__lt__(p1)
    
