height = int(input("Enter positive number(1-49): "))

if(height <= 0 or height >= 50):
    print("Enter number in this range(1-49)")
else:
    for i in range(1, height + 2):
        spaces = " " * (height - i)
        trunkSpaces = " " * (height - 1)

        if i == 1:
            print(spaces + "*")
        elif i == height+1:
            print(trunkSpaces + "|")
        else:
            leftSlashes = "/" * (i - 1)
            rightBackslashes = "\\" * (i - 1)
            print(spaces + leftSlashes + "|" + rightBackslashes)

