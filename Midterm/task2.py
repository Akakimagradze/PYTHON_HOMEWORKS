user_number = int(input("Plase, enter whole number: "))
if user_number <= 100:
    print("Wrong Value")
    exit(1)
elif user_number >= 1000:
    print("Wrong Value")
    exit(1)
    
counter = 0
sum = 0
for i in range(1, user_number + 1):
    if i % 13 == 0:
        print(i, end=" ")
        counter += 1
        sum += i
print()
print(f"Sum: {sum}")

