#classes

class PC:
    Manufacturer = "MSI"
    Model = "GP 62m"
    Ram = 16
    Gpu = 4

print (PC.__dict__)

PC.Hdd = "1Tb"
print (PC.__dict__)

device = PC

print (device.Model)