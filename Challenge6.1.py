class Point3D:
    __slots__ = ("x" , "y" , "z")

    def __init__(self, x, y, z ,c):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        print (f"Size of x,y,z = {self.x}{self.y}{self.z}")

class ColorPoint(Point3D):
    def __init__(self, color= "black"):
        # super().__init__(x,y,z)
        self.color = color
    def __repr__(self):
        print (f"color = {self.color}")
        
class ShapePoint(Point3D):
    def __init__(self, shape = "sphere"):
        # super().__init__(x,y,z)
        self.shape = shape
    def __repr__(self):
        print (f"shape = {self.shape}")

a = Point3D(1,2,3)
b = ColorPoint("pink")
c = ShapePoint("circle")
a.__repr__()
b.__repr__()
c.__repr__()

