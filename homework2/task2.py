firstNum = float(input("First Number: "))
secondNum = float(input("Second Number: "))

roundedFirstNum = round(firstNum)
roundedSecondNum = round(secondNum)

if(roundedFirstNum % roundedSecondNum == 0 or roundedSecondNum % roundedFirstNum == 0):
    print("ჯერადია")
else:
    print("არ არის ჯერადი")
    
