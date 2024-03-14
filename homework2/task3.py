whole_number = int(input("Please enter whole number in (1-10) interval: "))

if(whole_number <= 0 or whole_number > 10):
    print("Try different number")
else:
    if whole_number == 1:
        print(1)
    elif whole_number == 2:
        print(2)
    elif whole_number == 3:
        print(3)
    elif whole_number == 4:
        print(2, 4)
    elif whole_number == 5:
        print(1, 5)
    elif whole_number == 6:
        print(1, 2, 3, 6)
    elif whole_number == 7:
        print(1, 7)
    elif whole_number == 8:
        print(1, 2, 4, 8)
    elif whole_number == 9:
        print(1, 3, 9)
    elif whole_number == 10:
        print(1, 2, 5, 10)