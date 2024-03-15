user_password = input("Enter your password: ")
correct_password = "georgia"
max_tries = 3

for i in range(1, max_tries):
    if user_password != correct_password:
        user_password = input("Enter your password: ")
    
if user_password == correct_password and i < max_tries:
        print("Password is correct")  
if user_password != correct_password:
    print("You are blocked")
    
