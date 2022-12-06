class StdDes:
    def __init__(self, field_name):
        self.field_name = field_name
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(f"StdDes_{self.field_name}")

    def __set__(self, instance, value):
        # if not type(value)==str or type(value)==int :
        #     raise ValueError("invalid !")
        if type (value) == int:
            if value < 130:
                raise ValueError ("value can not be less than 130 Scores")
            elif value > 340 and value < 400:
                raise ValueError ("value can not be between 340 , 400")
            elif value > 1600 :
                raise ValueError ("value can not be less than 400 Scores")
            else:
                instance.__dict__[f"StdDes_{self.field_name}"] = value

        elif type (value) == str:
            instance.__dict__[f"StdDes_{self.field_name}"] = value
        
        else:
            raise ValueError ("Invalid !")

    def __delete__(self, instance):
        pass

class StudentProfile:
    Student_name = StdDes("Student_name")
    Gre_score = StdDes(range(130,340))
    Sat_score = StdDes(range(400,1600))

m = StudentProfile()

m.Student_name = "Sina"
m.Gre_score = 310
m.Sat_score = 1000

print ("Student name = \t", m.Student_name, "\n","GRE Score = \t", m.Gre_score, "\n","SAT Score = ", m.Sat_score)