userName = input("Enter your name: ")
userSurname = input("Enter your surname: ")
userAge = int(input("Enter your age: "))

if(userAge <= 0):
    print("Write positive numbers")
else:
    print(f'Hello, {userName} {userSurname}. You are {userAge} years old.')
    
