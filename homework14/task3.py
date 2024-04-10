import random

random_numbers = []
for i in range(0, 50):
    random_numbers.append(random.randint(1,30))

list_without_duplicates = []
for num in random_numbers:
    if num not in list_without_duplicates:
        list_without_duplicates.append(num)

print(f"List - {list_without_duplicates}")
print(f"Length - {len(list_without_duplicates)}")

