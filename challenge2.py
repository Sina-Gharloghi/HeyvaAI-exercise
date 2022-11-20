import random

userop = input("if you want to define the length of the passwrd please enter 'y', if not enter 'n'")
strength = "low"
if userop =="y" or userop== "Y":
    length = input("enter the stength => l:low - m:mid - h:high ")
    if length == "l":
        strength = "low"
    elif length == "m":
        strength = "mid"
    elif length == "h":
        strength = "high"
else:
    pass

c=[]

class Password:

    def __init__(self, strength, letters, nums, pun,length=12):
        self.strength = strength
        self.length = length
        self.letters = letters
        self.pun = pun
        self.nums = nums

    def gen(self):
        c1 = [1,2]
        c2 = [1,2,3]
        if self.strength == "low":
            for x in range(0,8):
                x = random.choice(self.letters)
                c.append(x)

        elif self.strength == "mid":
            for x in range(0,12):
                choose = random.choice(c1)
                if choose == 1:
                    x = random.choice(self.letters)
                elif choose == 2:
                    x = random.choice(self.nums)
                c.append(x)

        elif self.strength == "high":
            for x in range(0,16):
                choose = random.choice(c2)
                if choose == 1:
                    x = random.choice(self.letters)
                elif choose == 2:
                    x = random.choice(self.nums)
                elif choose == 3:
                    x = random.choice(self.pun)
                c.append(x)
        

        mypass = ''.join(map(str,c))
        print (mypass)

    @staticmethod
    def show_input_universe():
        d1 = Password.__dict__
        print (d1)

#low strength material
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#mid level
nums = [0,1,2,3,4,5,6,7,8,9]
#high level
pun = ["@","!","?","$","&"]

code = Password(strength,letters,nums,pun)
code.gen()

code.show_input_universe()