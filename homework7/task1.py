user_num = int(input("Enter number(0-19): "))

while user_num < 0 or user_num >= 20:
    user_num = int(input("Enter number(0-19): "))

i = 1
a, b = 0, 1
print(0, end=" ")

while i < user_num: 
    a, b = b, a + b
    print(a, end=" ")
    i += 1

