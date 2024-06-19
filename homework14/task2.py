import random

random_numbers = []
for i in range(0, 50):
    random_numbers.append(random.randint(1,30))

new_list = []
for num in random_numbers:
    new_list += [num] * num
    
print(f"List - {new_list}")
print(f"Length - {len(new_list)}")

