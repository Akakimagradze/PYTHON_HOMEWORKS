userNumber = int(input("Enter positive number(1-49): "))

if(userNumber <= 0 or userNumber >= 50):
    print("Try number in this range(1-49)")
else:
    for num in range(1, userNumber  + 1):
        print(num, end=" - ")
        count = 0
        for divisors in range(1, num + 1):
            if(num % divisors == 0):
                print(divisors, end=" ")
                count += 1
                if(count >= 3):
                    break
        print()

        