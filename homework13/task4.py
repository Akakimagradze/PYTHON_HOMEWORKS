def vowel_counter(s):
    vowels_to_check = ["a","e","i","o","u","A","E","I","O","U"]
    counter = 0
    for c in range(len(s)):
        for i in range(len(vowels_to_check)):
            if s[c] == vowels_to_check[i]:
                counter += 1
    print(f"{s} -> {counter}")

s = input("String: ")    
    
if __name__ == "__main__":
    vowel_counter(s)
    # s = "Xinkali" -> 3
    # s = "Mwvadi" -> 2
    # s = "Xachapuri" -> 4
    
    