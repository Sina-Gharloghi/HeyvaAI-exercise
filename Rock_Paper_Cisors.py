import random
from tracemalloc import start

def rpc():
    a = ["Rock","Paper","Cisors"]
    uc = input ("enter r for rock, p for paper and c for cisors : ")
    cc = random.choice(a)

    if uc == "r":
        if cc == "Rock":
            print ("draw")
        elif cc == "Paper":
            print("you lost")
        elif cc == "Cisors":
            print ("you win")
            pass
    
    elif uc == "p":
        if cc == "Rock":
            print ("you win")
        elif cc == "Paper":
            print("draw")
        elif cc == "Cisors":
            print ("you lost")
            pass

    elif uc == "c":
        if cc == "Rock":
            print ("you lost")
        elif cc == "Paper":
            print("you win")
        elif cc == "Cisors":
            print ("draw")
            pass       

    repeat = input("if you want to play again press a")
    if repeat=="a":
        rpc() 
    
start = input("press s to start the game : ")
rpc()
