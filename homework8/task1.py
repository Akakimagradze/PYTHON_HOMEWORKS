user_input = input("Enter a string: ")

for i in range(0, len(user_input)):
    if user_input[i] != "e" and i % 2 == 0:
        print(user_input[i], end=" ")
print()

