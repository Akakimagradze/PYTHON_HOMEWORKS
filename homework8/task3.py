user_input = input("Enter a string: ")

i = 0 
while i < 5:
    print(user_input[0], end="")
    i += 1
print(end=" ")

if(len(user_input) % 2 != 0):
    j = 0
    while j < 5:
        middle = int(len(user_input) / 2)
        print(user_input[middle], end="")
        j += 1
    print(end=" ")
else:
    j = 0
    while j < 5:
        middle = int(len(user_input) / 2)
        print(f"{user_input[middle - 1]}{user_input[middle]}", end="")
        j += 1
    print(end=" ")
    
k = 0
while k < 5:
    print(user_input[-1], end="")
    k += 1
print() 
        
        