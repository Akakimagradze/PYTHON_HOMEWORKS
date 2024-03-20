keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
action = input("Enter action (e/d): ")

while action != "e" and action != "d":
    action = input("Enter action (e/d): ")
    
text = input("Enter text: ")
result = ""


for char in text:
    if char.islower():
        for row in keyboard:
            if char in row:
                if action == 'e':
                    if char == row[-1]:
                        result += row[0]
                    else:
                        result += row[row.index(char) + 1]
                elif action == 'd':
                    if char == row[0]:
                        result += row[-1]
                    else:
                        result += row[row.index(char) - 1]
print(result)

