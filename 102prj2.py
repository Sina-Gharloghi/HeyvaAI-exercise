class PC:
    Manufacturer = "MSI"
    Model = "GP 62m"
    Ram = 16
    Gpu = 4

    def test(self):
        print (f"ir is ==> {self}")

m = PC()
n = PC()

m.test()
n.test()
# m and n are not the same although they are both refered to class PC