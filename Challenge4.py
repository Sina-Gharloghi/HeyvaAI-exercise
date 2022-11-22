import math
from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        # self.a=a
        # self.b=b
        # self.c=c
        #self.vector1 = (x,y,z)
        #self.vector2 = vector2
        
    def magnitude(self):
        mag = math.sqrt(abs(self.x+self.y+self.z))
        if mag == 0:
            return False
        else:
            print(mag)

    def hashcheck(self):
        h = hash(Vector)
        print(h)

    def multiply(self):
        cof = float(input("Enter the number you want to multiply : \t"))
        new_vector = (cof*self.x, cof*self.y, cof*self.z)
        print (new_vector)
    
    #defined to sum and sub the vecs
    def __SubAndSum__(self, other, op): 
        if not isinstance(other, Vector):
            return ("not qualified!")
        else:    
            if op == "+":
                sum = (self.x+other.x , self.y+other.y , self.z+other.z)
                print (sum)
            elif op == "-":
                sub = (self.x-other.x , self.y-other.y , self.z-other.z)
                print(sub)

    def __eq__(self,other):
        if not isinstance(other, Vector):
            return False
        else:
            self.x == other.x
    
    def __gt__(self,other):
        if not isinstance(other,Vector):
            return False
        else:
            return True


x = float(input("enter x1 value : \t"))
y = float(input("enter y1 value : \t"))
z = float(input("enter z1 value : \t"))
i = float(input("enter x2 value : \t"))
j = float(input("enter y2 value : \t"))
k = float(input("enter z3 value : \t"))

calc = input("do you want to calulate something your vectors? y=yes  \t")

v1 = Vector(x,y,z)
v2 = Vector(i,j,k)

if calc == "y":
    global op
    op = input("for multiply press '*', for sum press '+' and for sub press '-'")
         
    v1.magnitude()
    v2.magnitude()
    if op == "*":
        v1.multiply()
        v2.multiply()
    elif op == "+" or "-":    
        v1.__SubAndSum__(v2,op)
    
    v1 == v2
    v1 > v2

    v1.hashcheck()
else:
    pass

print(v1==v2, "\n", v1!=v2, "\n", v1>v2, "\n")
