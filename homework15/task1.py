import random

generated_numbers = []
for i in range(100):
    generated_numbers.append(random.randint(10, 1000000000))

shortest_number = min(generated_numbers, key=lambda x: len(str(x)))
longest_number = max(generated_numbers, key=lambda x: len(str(x)))

sorted_by_increment = sorted(generated_numbers, key=lambda x: len(str(x)))
sorted_by_decrement = sorted(generated_numbers, key=lambda x: len(str(x)), reverse=True)

print(f"Generated Numbers: {generated_numbers}")
print()
print(f"Shortest Number: {shortest_number}")
print()
print(f"Longest Number: {longest_number}")
print()
print(f"Sorted By Increment: {sorted_by_increment}")
print()
print(f"Sorted By Decrement: {sorted_by_decrement}")

