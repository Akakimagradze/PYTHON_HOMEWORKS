first_num = float(input("First number: "))
second_num = float(input("Second number: "))

rounded_first_num = round(first_num)
rounded_second_num = round(second_num)

if(rounded_first_num % rounded_second_num == 0 or rounded_second_num % rounded_first_num == 0):
    print("ჯერადია")
else:
    print("არ არის ჯერადი")
    
