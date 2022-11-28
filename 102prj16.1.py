class Student:
    def __init__(self, tidiness):
        self.tidiness = tidiness
    

s1 = Student("messy")
s2 = Student("normal")
s3 = Student("neat")

def get_tidy(student):
    tidy_stat = {
        "messy":16,
        "normal":18,
        "neat":20
    }

    score = tidy_stat.get(student.tidiness, None)

    if not score:
        raise ValueError ("there is no status of the tidiness")

    return score

for student in [s1,s2,s3]:
    print (f"The student's score is {get_tidy(student)}")    