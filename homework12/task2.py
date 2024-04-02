from task1_recursion import gcd

print("FOR LCM CALCULATION")
a = int(input("Enter a: "))
while a <= 0 or a > 10000:
    a = int(input("Enter a: "))

b = int(input("Enter b: "))
while b <= 0 or b > 10000:
    b = int(input("Enter b: "))
    
def smallest_multiple_number(a,b):
    print(f"LCM of {a} and {b} is {int(((a * b) / gcd(a,b)))}.")

        
if __name__ == '__main__':
    smallest_multiple_number(a,b)
    
    