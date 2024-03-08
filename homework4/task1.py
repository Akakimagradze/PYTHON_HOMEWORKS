import random

playerAmount = int(input("Please enter player amount: "))
playerNumber = 1

if(playerAmount <= 0):
    print("Enter positive number")
else:
    for eachPlayer in range(playerAmount):
        print(f"Player {playerNumber} Dices are: {random.randint(1,6)} {random.randint(1,6)}")
        playerNumber += 1
        
