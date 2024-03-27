n = int(input("Enter a number: "))

while n <= 1:
    n = int(input("Enter a number: "))
    
result = 0
sign = 1

for i in range(1, n + 1):
    result += sign * (1 / (2 * i - 1))
    sign *= -1
    
print(4 * result)

