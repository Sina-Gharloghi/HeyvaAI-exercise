# __len__

class Patient:
    def __init__(self, name, lname, weight, age, state):
        self.name = name
        self.lname = lname
        self.weight = weight
        self.age = age
        self.state = state

    def __repr__(self):
        print (f"{self.name} has {self.state} situation")

    # def __bool__(self):
    #     return bool(self.age) and not (self.age < 0)
    
    def __len__(self):
        return self.age

p1 = Patient("john", "kenedy", 70, 58, "Critical")
p2 = Patient("john", "kenedy", 70, 0, "Critical")

# although bool is not defined, the len will implement bool's functionality 
# but it only works with amounts greater than 0 cuse length can't be neg

print (bool(p1), "\n", bool(p2))