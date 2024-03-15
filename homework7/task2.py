import sys

user_num = int(input("Enter number(1-1000): "))

while user_num <= 0 or user_num > 1000:
    user_num = int(input("Enter number(1-1000): "))

while user_num != 1:
        if user_num % 2 == 0:
            user_num = user_num // 2
        else:
            user_num = user_num * 3 + 1
        print(user_num, end=' ')        
        
sys.exit(1)

