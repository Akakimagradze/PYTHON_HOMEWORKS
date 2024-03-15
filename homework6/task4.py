user_num = int(input("Enter positive number(1-9): "))

while user_num <= 0 or user_num >= 10:
    user_num = int(input("Enter positive number(1-9): "))
    
i = 1
while i <= user_num:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
    
i = user_num - 1
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1

