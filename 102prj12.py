# __eq__ method
from functools import total_ordering

@total_ordering
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
        if not isinstance(other, Patient):
            return False
        else:
            return self.age == other.age
    
    def __gt__(self,other):
        if not isinstance(other,Patient):
            return False
        else:
            return self.weight > other.weight

p1 = Patient("john", "kenedy", 70, 58, "Critical")
p2 = Patient("john", "kenedy", 67, 60, "Critical")

print(p1==p2, "\n", p1!=p2, "\n", p1>p2, "\n", p1>=p2, "\n", p1<p2, "\n", p1<=p2)
    
