# __str__ & __repr__

class Patient:
    def __init__(self, name, lname, weight, age, state):
        self.name = name
        self.lname = lname
        self.weight = weight
        self.age = age
        self.state = state

    def __repr__(self):
        print (f"(Patient Information : '{self.name}', '{self.lname}', '{self.weight}', '{self.age}', '{self.state}')")

    def __str__(self):
        print (f"{self.name} has {self.state} situation")

p1 = Patient("john", "kenedy", 70, 58, "Critical")

# used as the default method, returns the info... 
p1.__repr__()

# returns the info for the user
p1.__str__()

