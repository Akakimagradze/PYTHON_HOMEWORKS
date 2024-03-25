first_string = input("First string: ")
second_string = input("Second string: ")

sorted_first_string = sorted(first_string.lower())
sorted_second_string = sorted(second_string.lower())

if sorted_first_string == sorted_second_string:
    print("Output: YES")
else:
    print("Output: NO")
    
