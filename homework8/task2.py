user_input = input("Enter a string: ")

consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

for i in user_input:
    if i in consonants:
        print(i, end="")
print()
    
