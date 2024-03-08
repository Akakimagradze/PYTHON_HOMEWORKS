import datetime

today = datetime.date.today()
year = today.year

userName = input("Enter your name: ")
userBirthYear = int(input("Enter your birth year: "))
userAge = year - userBirthYear 

if(userBirthYear > year or userBirthYear <= 0):
    print("Wrong input")
else:
    print(f"Hello {userName}, You are {userAge} years old.")
    
