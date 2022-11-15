#function

def calc(r):
    s = (r**2)*3.14
    p = (r*2)*3.14

    print ("surface = ", s, " cm^2","\n", "primeter = ", p, " cm")

r = float(input("please inter the radius : "))

calc(r)