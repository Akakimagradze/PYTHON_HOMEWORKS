def check_shift(input_a, input_b):
    if len(input_a) != len(input_b):
        return False

    for i in range(len(input_a)):
        shifted_line = input_a[i:] + input_a[:i]
        if shifted_line == input_b:
            return True
        
    return False

input_a = str(input("Input a: "))
input_b = str(input("Input b: "))

if check_shift(input_a, input_b):
    print("Output: YES")
else:
    print("Output: NO")

