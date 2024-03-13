userPassword = input("Enter your password: ")
correctPassword = "georgia"
maxTries = 3

for i in range(1, maxTries):
    if userPassword != correctPassword and i < maxTries:
        userPassword = input("Enter your password: ")
    
if userPassword == correctPassword and i < maxTries:
        print("Password is correct")  
if userPassword != correctPassword:
    print("You are blocked")
    
