import json

def main():
    with open("data.txt", "r") as file:
        lines = file.readlines()
        
        most_expensive_product = ""
        most_expensive_product_cost = 0
        
        most_sold_product = ""
        most_sold_product_quantity = 0
        
        maximum_purchaser = ""
        maximum_purchaser_cost = 0
        
        purchase_sum = 0
        cost_sum = 0
        
        for line in lines:
            each_line = line.strip().split(",")
            quantity = int(each_line[2])
            cost = each_line[3]
            
            purchase_sum += int(quantity)
            cost_sum += float(cost)
            
            if quantity > int(most_sold_product_quantity):
                most_sold_product = each_line[1]
                most_sold_product_quantity = quantity
                
            if quantity * float(cost) > int(maximum_purchaser_cost):
                maximum_purchaser_cost = quantity * float(cost)
                maximum_purchaser = each_line
                
            if float(cost) > float(most_expensive_product_cost):
                most_expensive_product_cost = cost
                most_expensive_product = each_line[1]
                
            my_dict = {
            "Quantity Average": purchase_sum / len(lines),
            "Cost Average": cost_sum / len(lines),
            "Most Sold Product": f"{most_sold_product} - {most_sold_product_quantity}",
            "Maximum Purchaser": f"{maximum_purchaser[0]} - {maximum_purchaser_cost}",
            "Most Expensive Product": f"{most_expensive_product} - {most_expensive_product_cost}"
            }
            
    with open("stats.json", "w") as file:
        json.dump(my_dict, file)
        
        
if __name__ == "__main__":
    main()
    
