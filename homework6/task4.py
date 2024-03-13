userNum = int(input("Enter positive number(1-9): "))

while userNum <= 0 or userNum >= 10:
    userNum = int(input("Enter positive number(1-9): "))
    
i = 1
while i <= userNum:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1
    
i = userNum - 1
while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1

