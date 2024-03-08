wholeNumber = int(input("Please enter whole number in (1-10) interval: "))

if(wholeNumber <= 0 or wholeNumber > 10):
    print("Try different number")
else:
    for startPoint in range(10):
        startPoint += 2
        if(wholeNumber % startPoint == 0 and startPoint != wholeNumber):
            print(startPoint, end=" ")
            
