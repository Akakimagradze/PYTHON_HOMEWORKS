userNumber = int(input("Enter positive number(0-19): "))

if(userNumber < 0 or userNumber >= 20):
    print("Try numbers in this range(0-19)")
else:
    a, b = 0, 1 
    for i in range(userNumber):
        a, b = b, a + b 
    print(a)
    
