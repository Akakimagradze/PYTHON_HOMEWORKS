userNum = int(input("Enter positive whole number(1-999): "))

if(userNum <= 0 or userNum >= 1000):
    print("Try number in this range (1-999)")
else:
    for dividers in range(1, userNum):
        if(userNum % dividers == 0):
            print(dividers, end=" ")
        
    print(userNum)
    
