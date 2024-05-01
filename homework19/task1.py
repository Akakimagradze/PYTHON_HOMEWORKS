def main():
    with open("data.txt", "r") as file:
        lines = file.readlines()
        
        small_purchase = []
        high_purchase = []
        
        for line in lines:
            each_line = line.strip().split(",")
            if float(each_line[2]) * float(each_line[3]) < 10:
                small_purchase.append(line)
            else:
                high_purchase.append(line)
        
        with open("small.txt", "w") as file:
            file.writelines(small_purchase)
        
        with open("high.txt", "w") as file:
            file.writelines(high_purchase)
        
if __name__ == "__main__":
    main()        
    
    