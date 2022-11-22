class Contact:
    def __init__(self, name, last_name, phone, email, display_mode="masked"):
        self.name=name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.display_mode=display_mode

    @staticmethod
    def Create_contact():
        a = input("do you want to create a new contact? y=yes \t")
        b = int(input("how many contacts do you want to create? \t"))
        global c
        c = []
        if a == "y":
            for x in range (0,b):
                name1 = input("name : \t")
                lname1 = input("last name : \t")
                optional = input("do you want to add more info? y=yes \t")

                if optional=="y":
                    phone1 = input("phone : \t")
                    email1 = input("email : \t")
                    x = Contact(name1,lname1,phone1,email1)            
                else:
                    x = Contact(name1,lname1,"empty","empty")

                c.append(x)
        else:
            pass

    def __repr__(self):
        print (f"details : {self.name} - {self.last_name} ")

    def __format__(self, display_mode):
        display_mode = input("deo you want to see all info? y=yes ")
        if display_mode == "y":
            print(f"{self.name} - {self.last_name} - {self.email} - {self.phone}")
        else:
            Contact.__repr__(self)

    def __str__(self):
        self.name = self.name[0]
        self.last_name = self.last_name[-1]
        x = self.name+self.last_name
        print(x)

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        else:
            if self.name==other.name and self.last_name==other.last_name:
                print("user has already registered !")
            elif self.phone==other.phone or self.email==other.email:
                print("user has already registered !")
            else:
                pass 

y = Contact("","","","")
y.Create_contact()

# d=[]
# if len(c)>1:
#     del c[0]
#     d = c

for y in c:
    y.__format__("masked")
    y.__str__()
    y.__eq__(y)
    # i=0
    # for x in d:
    #     x = d[i]
    #     y.__eq__(x)
    #     i = i+1