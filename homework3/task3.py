import random

cardSuits = ['♣', '♦', '♥', '♠']
cardRanks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

print(f"Generated card is {random.choice(cardSuits)}", end="")
print(f"{random.choice(cardRanks)}")

