def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

s = input("String: ")

if __name__ == "__main__":
    print(f"{s} -> {reverse_string(s)}")
    # Input: Correct --> Output: tcerroC
    # Input: Right --> Output: thgiR 
    
    