import random

def main():
    random_number = random.randint(1,3)
    computer_move = ""
    if random_number == 1:
        computer_move = "R"
    elif random_number == 2:
        computer_move = "P"
    else:
        computer_move = "S"
    
    user_move = input("Enter (R/P/S): ")
    while user_move.upper() != "R" and user_move.upper() != "P" and user_move.upper() != "S":
        user_move = input("Enter (R/P/S): ")
    
    if computer_move.upper() == "R" and user_move.upper() == "S":
        print("Computer Won")
    elif computer_move.upper() == "R" and user_move.upper() == "P":
        print("You Won")
    elif computer_move.upper() == "R" and user_move.upper() == "R":
        print("Draw")
    elif computer_move.upper() == "P" and user_move.upper() == "R":
        print("Computer Won")
    elif computer_move.upper() == "P" and user_move.upper() == "P":
        print("Draw")
    elif computer_move.upper()== "P" and user_move.upper() == "S":
        print("You Won")
    elif user_move.upper() == "S" and computer_move.upper() == "S":
        print("Draw")
    elif user_move.upper() == "S" and computer_move.upper() == "P":
        print("Computer Won")
    elif user_move.upper() == "S" and computer_move.upper() == "R":
        print("You Won")
        
main()

