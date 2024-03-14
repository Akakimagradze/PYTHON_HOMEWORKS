car_speed = float(input("Please enter car speed: "))
rounded_car_speed = round(car_speed)

if(rounded_car_speed <= 0):
    print("Try again")
elif(rounded_car_speed <= 30):
    print("SLOW")
elif(rounded_car_speed > 30 and rounded_car_speed <= 60):
    print("MODERATE")
elif(rounded_car_speed > 60 and rounded_car_speed <= 120):
    print("FAST")
else:
    print("VERY FAST")
    
