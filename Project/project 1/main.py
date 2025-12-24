import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "Gun"}

you = youDict[youStr]

# By now we have two numbers, you and computer 
print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == -1):
        print("You lose!")
    else:
        print("Somethings went wrong")