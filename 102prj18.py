class Student:
    tidiness = {"messy","normal","neat"}

    def __init__(self, tidiness):
        self.set_tidiness(tidiness)
    
    def get_tidiness(self):
        return self.tidiness

    def set_tidiness(self, level):
        if level not in self.tidiness:
            raise ValueError (f"{level} is invalid")
        self.tidiness = level

    tidiness = property(fget=get_tidiness , fset=set_tidiness)

s1 = "messy"
s2 = "normal"
s3 = "neat"

for student in [s1,s2,s3]:
    print (f"the score is {student.get_tidiness(student)}") 