class Point3D:
    __slots__ = ("x" , "y" , "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
            print (f"Size of x,y,z = {self.x},{self.y},{self.z} - color = {ColorPoint.__repr__()} - shape = {ShapePoint}") #dastresi gereftam be subclassam
        

class ColorPoint(Point3D):
    # __slots__ = ("color")
    def __init__(self, x, y, z, color="black"):
        super().__init__(x, y, z, color)
        self.color = color
    def __repr__(self,color):
        return super().__repr__(color)             #object ro barmigardone :(((
        
class ShapePoint(Point3D):
    __slots__ = "shape"
    def __init__(self, x, y, z, shape="sphere"):
        super().__init__(x, y, z)
        self.shape = shape

a = Point3D(1,2,3)
a.__repr__()
