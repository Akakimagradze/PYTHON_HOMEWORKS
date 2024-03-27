import random
import math

n = int(input("Enter a number: "))

while n <= 1:
    n = int(input("Enter a number: "))

counter = 0
for i in range(0, n):
    a = int(random.random() * 10) / 10.0
    b = int(random.random() * 10) / 10.0
    print(a,b)
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1

print(4 * counter / n)

