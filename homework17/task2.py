user_input = input("Input: ")

def symbol_counter(string):
    symbols_dict = {}
    
    for symbol in string:
        if symbol in symbols_dict:
            symbols_dict[symbol] += 1
        else:
            symbols_dict[symbol] = 1
    
    for key, value in symbols_dict.items():
        print(f"{key} - {value}")   
     
if __name__ == "__main__":
    symbol_counter(user_input)

