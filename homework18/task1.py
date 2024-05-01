user_number = int(input("Number: "))
cache_dict = {}

def sequence_generator_without_cache(number):
    result = number
    while result != 1:
        if result % 2 == 0:
            result //=  2
            print(result, end=" ")
        else:
            result = result * 3 + 1
            print(result, end=" ")
            

def sequenece_generator_with_cache(number):
    if number in cache_dict:
        print(cache_dict[number])
    
    result = number
    list_of_nums = []
    while result != 1:
        if result % 2 == 0:
            result //= 2
            list_of_nums.append(result)
        else:
            result = result * 3 + 1
            list_of_nums.append(result)
    cache_dict[number] = list_of_nums

    print(list_of_nums)
    print(f"Cache: {cache_dict}")
    
    
def main():
    print("Without cache: ", end=" --  ")
    sequence_generator_without_cache(user_number)
    print()
    print("With cache: ", end=" --  ")
    sequenece_generator_with_cache(user_number)

if __name__ == "__main__":
    main()
    
    
