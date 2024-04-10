temp_list = [22, 25, 19, 23, 25, 26, 23]

def temp_teller(nums_list):
    sum = 0
    for elem in range(len(nums_list)):
        sum += nums_list[elem]
        
    result = sum / len(nums_list)
    print(f"Average temperature: {result}")
    
    
temp_teller(temp_list)

