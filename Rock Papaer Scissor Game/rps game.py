# rock paper scissar game
# Are you ready to play!!!
from random import randint
t=["rock","paper","scissor"]
computer=t[randint(0,2)]
player=False
while player==False:
    player=input("rock,paper,scissor?")
    if player==computer:
        print("tie")
    elif player=="rock":
        if computer=="paper":
             print("you lose", computer, "covers you")
        else:
            print("yes you broke him")
            
    elif player=="paper":
        if computer=="scissor":
            print("you lose he cuts you")
        else:
            print("yes! you cover him")
    elif player=="scissor":
        if computer=="rock":
            print("sorry you are broken by him")
        else:
             print("yes! you cut him")
    else:
       print(" i think! you dont know the game")
    player=False
    computer=t[randint(0,2)]
