import random
print ("Welcome to play  ")
print("  ")
print("Enter your move : ")
move = input().lower()
lists = ("rock","paper","scissor")
choose = random.choice(lists)
if move not in choose:
    print("Invalid input ")
elif move == choose :
    print("Drawn")
    elif move ==