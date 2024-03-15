import random

computer_number = random.randint(0, 99)
user_number = int(input("Guess the number(0-99): "))
max_tries = 10
counter = 1

while counter < max_tries:
    if user_number > computer_number:
        print("High")
    elif user_number < computer_number:
        print("Low")
    else:
        print("You are winner")
        break
    counter += 1
    user_number = int(input("Guess the number(0-99): "))
    
if user_number != computer_number:
    print("Computer is winnner")

    