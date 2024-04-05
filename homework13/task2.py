def simple_number_checker(n):
    if n == 0 or n == 1:
        print("0 and 1 is not simple numbers")
        exit(1)
    
    counter = 0
    for i in range(1, n + 1):
       if n % i == 0:
           counter += 1
    if counter > 2:
        print("Is not simple number")
    else:
        print("Is simple number")      

n = int(input("Number: "))

if __name__ == "__main__":
    simple_number_checker(n)
    # n = 2 is simple, Divisors --> 1 2
    # n = 8 is not simple, Divisors --> 1 2 4 8
    # n = 11 is simple, Divisors --> 1 11
    # n = 15 is not simple, Divisors --> 1 3 5
    
