s = input("Input: ")
s = s.lower()
symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = ""

for i in s:
    if i in symbols:
        word += i

if word[::-1] == word:
    print(f"Output: Is palindrome")
else:
    print(f"Output: Is not palindrome")
    
    