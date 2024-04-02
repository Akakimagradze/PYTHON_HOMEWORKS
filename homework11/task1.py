def shifted_string(user_input):
    print("Output: ")
    for i in range(len(user_input)-1, -1,-1):
        reversed_str = user_input[i:] + user_input[:i]
        print(reversed_str)

user_input = str(input("Input: "))

shifted_string(user_input)

