import json

def main():
    try:
        with open('markets.json') as file:
            markets_data = json.load(file)

        with open('recipes.json') as f:
            recipes_data = json.load(f)
    except FileNotFoundError as err:
        print(err)
        

    print(f"Avaliable dishes: {list(recipes_data.keys())}")
    dish = input("Which dish would you like to cook? ")

    if dish not in recipes_data:
        print(f"Cant make {dish}")
        exit(1)
    else:
        required_ingredients = []
        markets_to_go = set()
        ingredients = []
        for item in recipes_data[dish]['ingredients']:
            required_ingredients.append(item)
        
        for key, value in markets_data.items():
            for i in value:
                if i in required_ingredients and i not in ingredients:
                    markets_to_go.add(key)
                    ingredients.append(i)
        print(f"You need to go to these markets {markets_to_go}")

if __name__ == "__main__":
    main()
    
