user_num = int(input("Enter positive number(1-9): "))

while user_num <= 0 or user_num >= 10:
    user_num = int(input("Enter positive number(1-9): "))

i = 0
while i <= user_num:
    j = 1
    while j <= user_num - i:
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

