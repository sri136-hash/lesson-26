import random
import time
number=random.randint
def intro():
    print("Can you please enter your name?")
    global name
    name=input()
    print(name+",this is the guess game.I am thinging of a number between 1-100.")
    if number%2==0:
        x="even"
    else:
        x="odd"
    print("The number is an",x,"number")
    time.sleep(0.5)
    print("Go ahead and guess!")

def pick():
    guesstaken=0
    while guesstaken<6:
        time.sleep(0.25)
        guess=input("guess")
        try:
            guess=int(guess)
            if guess<=100 and guess>=1:
                guesstaken=guesstaken+1
                if guess>number:
                    print("Your value is too high!")
                if guess<number:
                    print("Your value is too low!")
                if guess!=number:
                    time.sleep(0.5)
                    print("Please try again!")
                if guess==number:
                    break
                
        