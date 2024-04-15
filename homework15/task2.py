import random

list1 = []
for i in range(5):
    list1.append(random.randint(1,100))
    
list2 = []
for i in range(5):
    list2.append(random.randint(1,100))
    
list3 = []
for i in range(5):
    list3.append(random.randint(1,100))
    
for i in range(len(list1)):
    result = list1[i] + list2[i] + list3[i]
    print(f"Sum: {result}")

