sideA = float(input("Side A size: "))
sideB = float(input("Side B size: "))
sideC = float(input("Side C size: "))

x = (sideA + sideB + sideC) / 2
triangleArea = (x *(x - sideA) * (x - sideB) * (x - sideC)) ** 0.5
perimeter = sideA + sideB + sideC

if(sideA <= 0 or sideB <= 0 or sideC <= 0):
    print("Please write positive numbers")
else:
    print(f"Triangle area is: {triangleArea}")
    print(f"Triangle perimeter is: {perimeter}")
    
