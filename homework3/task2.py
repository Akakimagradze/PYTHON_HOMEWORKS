import calendar

userBirthYear = int(input("What year were you born?: "))
userBirthMonth = int(input("What month were you born?(1-12): "))
userBirthDate = int(input("What date were you born?(1-31): "))

if((userBirthYear < 1000 and userBirthYear > 2024) or (userBirthMonth <= 0 or userBirthMonth > 12) or (userBirthDate <= 0 or userBirthDate > 31)):
    print("Something went wrong")

result = calendar.weekday(userBirthYear, userBirthMonth, userBirthDate)

match result:
    case 0:
        print(f"You were born on Monday")
    case 1:
        print(f"You were born on Tuesday")
    case 2:
        print(f"You were born on Wednesday")
    case 3:
        print(f"You were born on Thursday")
    case 4:
        print(f"You were born on Friday")
    case 5:
        print(f"You were born on Saturday")
    case 6:
        print(f"You were born on Sunday")
        
