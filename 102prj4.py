#getattar and setattar

class PC:
    Manufacturer = "MSI"
    Model = "GP 62m"
    Ram = 16
    Gpu = 4

m = PC()

print (getattr(m, "Ram"))
# same as print(m.Ram)

setattr (m, "Gpu", 8)
print (getattr(m, "Gpu"))

#setting a group of new objects into the class

opt = ["color", "cpu", "screen"]
val = ["black", "i7", 16]


for y,z in zip(opt, val):
    setattr(m, y, z)

ui=input("enter the detail you want : ")
print(getattr(m, ui))