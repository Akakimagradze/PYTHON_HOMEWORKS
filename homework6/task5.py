userNum = int(input("Enter positive number(1-9): "))

while userNum <= 0 or userNum >= 10:
    userNum = int(input("Enter positive number(1-9): "))

i = 0
while i <= userNum:
    j = 1
    while j <= userNum - i:
        print(end=" ")
        j += 1
        
    j = i
    while j >= 0:
        print(j, end="")
        j -= 1
        
    j = 1
    while j < i + 1:
        print(j, end="")
        j += 1
        
    print()
    i += 1

