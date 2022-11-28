# properties ...
class Car:
    def __init__(self, speed):
        self.speed=speed

c1 = Car("high")
c2 = Car("mid")
c3 = Car("low")

def get_speed(car):
    speeds = {
        "high":300,
        "mid":200,
        "low":100
    }
    speed = speeds.get(car.speed , None)

    if not speed:
        raise TypeError("car not specified!")
    return speed

for car in [c1,c2,c3]:
    print (f"this car's going {get_speed(car): 0}") 

    