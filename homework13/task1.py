def converter():
    convert_to = input("Input (C / F): ")
    n = int(input("Number: "))
    result = ''
    
    if convert_to.upper() == "C":
        result = (n - 32) * 5 / 9
        print(result.__round__(3))
    elif convert_to.upper() == "F":
        result = (n * 9 / 5) + 32
        print(result.__round__(3))
    else:
        print("Wrong Input")


if __name__ == "__main__":
    converter()
    # convert_to == "C"
    # n = 0
    # output = "-17.778"
            
    # convert_to == "F"
    # n = 20
    # output = "68.0"
    
    