
#My First real life project done by me
import random

play = ["rock","paper","scissor"]
choose = random.choice(play)

print("Input your move, remember all move must me in small letters. :")
user = input().lower()
if user not in play:
    print("Wrong input")
elif user == choose :
    print("Drawn")
elif user == "rock" and choose == "paper" :
    print("You lost")
elif user == "paper" and choose == "scissor" :
    print("you Lost")
elif user == "scissor" and choose == "rock" :
    print("You loss")

else :
    print("You win")


