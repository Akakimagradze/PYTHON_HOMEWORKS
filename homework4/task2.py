import random

userNum = int(input("Enter number between(1-29): ")) 
arr = []

if(userNum <= 0 or userNum >= 30):
    print("Try number in this range(1-29)")
else:
    for i in range(0, userNum):
       arr.append(random.randint(0, 1000))
    if(len(arr) > 0):
           print(f"Generated numbers are {arr}")
           print(f"Highest Number is {max(arr)}")
           
