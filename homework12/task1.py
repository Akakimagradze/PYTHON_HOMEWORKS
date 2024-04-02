a = int(input("Enter a: "))
while a <= 0 or a > 10000:
    a = int(input("Enter a: "))

b = int(input("Enter b: "))
while b <= 0 or b > 10000:
    b = int(input("Enter b: "))

def greatest_divisor(a,b):       
    a_divisors = []
    for i in range(1, a + 1):
        if a % i == 0:
            a_divisors.append(i)
    
    b_divisors = []
    for i in range(1, b + 1):
        if b % i == 0:
            b_divisors.append(i)   
    
    same_divisors = [element for element in a_divisors if element in b_divisors]
    print(f"GCD of {a} and {b} is {max(same_divisors)}.")
    

if __name__ == "__main__":
    greatest_divisor(a,b)

