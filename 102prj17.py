# properties ...
class Car:
    speeds = {"high", "mid", "low"}
    def __init__(self, speed):
        self.set_speed = speed
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        if speed not in self.__class__.speeds:
            raise ValueError(f"speed of {speed} is not valid") 
        self.speeds = speed
        print ("True")

a = input("enter value : \t")

b = Car(a)

# It is not working :(((