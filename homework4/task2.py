import random

user_num = int(input("Enter number between(1-29): ")) 

while user_num <= 0 or user_num >= 30:
    user_num = int(input("Enter number between(1-29): ")) 

highest_number = 0
for i in range(0, user_num):
    generated_number = random.randint(0, 1000)
    if generated_number > highest_number:
        highest_number = generated_number
    print(generated_number, end=", ")
print()
print(highest_number)
        

           
