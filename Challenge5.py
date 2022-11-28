class DNABase:
    bases = {"adenine","cytosine","guanine","thymine"}

    def __init__(self, nucleotide):
        self.nucleotide = nucleotide

    def get_nucleotide(self):
        print (f"The nucleotide is '{self._nucleotide}'")

    def set_nucleotide(self,type):
        if type == "adenine" or type =="a":
            type = "adenine"
        elif user_data == "cytosine" or user_data =="c":
            type = "cytosine"
        elif user_data == "guanine" or user_data =="g":
            type = "guanine"
        elif user_data == "thymine" or user_data =="t":
            type = "thymine"
        else:
             raise ValueError("invalid input !")

        if type not in self.bases:
            raise ValueError (f"{type} is not valid !")

        self._nucleotide = type 
    
    nucleotide = property(fget=get_nucleotide , fset=set_nucleotide)


user_data = input("enter the type of nucleotide of its initials : \t").lower()

n = DNABase(user_data)
n.get_nucleotide()

# *** We coud have also check our input out of the class***
# if user_data == "adenine" or user_data =="a":
#     n = DNABase("adenine")
# elif user_data == "cytosine" or user_data =="c":
#     n = DNABase("cytosine")
# elif user_data == "guanine" or user_data =="g":
#     n = DNABase("guanine")
# elif user_data == "thymine" or user_data =="t":
#     n = DNABase("thymine")
# else:
#     raise ValueError("invalid input !")