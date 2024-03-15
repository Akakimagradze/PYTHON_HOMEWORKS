import random

player_amount = int(input("Enter players number: "))

while player_amount <= 0:
    player_amount = int(input("Enter players number: "))

for each_player in range(player_amount):
    print(random.randint(1,6), random.randint(1,6))
        
