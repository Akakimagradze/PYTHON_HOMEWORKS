import random

computerNum = random.randint(0, 99)
userNum = int(input("Guess the number(0-99): "))
maxTries = 10
counter = 1

while counter < maxTries:
    if userNum > computerNum:
        print("High")
    elif userNum < computerNum:
        print("Low")
    else:
        print("You are winner")
        break
    counter += 1
    userNum = int(input("Guess the number(0-99): "))
    
if userNum != computerNum:
    print("Computer is winnner")

    