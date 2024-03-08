carSpeed = float(input("Please enter car speed: "))
roundedCarSpeed = round(carSpeed)

if(roundedCarSpeed <= 0):
    print("Try again")
elif(roundedCarSpeed <= 30):
    print("Car is slow")
elif(roundedCarSpeed > 30 and roundedCarSpeed <= 60):
    print("Car is moderate")
elif(roundedCarSpeed > 60 and roundedCarSpeed <= 120):
    print("Car is fast")
else:
    print("Car is very fast")
    
