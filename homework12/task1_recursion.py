a = int(input("Enter a: "))
while a <= 0 or a > 10000:
    a = int(input("Enter a: "))

b = int(input("Enter b: "))
while b <= 0 or b > 10000:
    b = int(input("Enter b: "))

def gcd(a, b): #Because of recursion running is limited, there are some cases where this program  will crush example(a=17, b=10000) 
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)

print(f"GCD of {a} and {b} is {gcd(a, b)}.")

