user_num = int(input("Enter positive integer(0-9999): "))

while user_num < 0 or user_num >= 10000:                      
    user_num = int(input("Enter positive integer(0-9999): "))
          

print(f"enter number: {user_num}") 
reversed_number = ""
numbers_sum = 0

user_num_string = str(user_num)
index = len(user_num_string) - 1
while index >= 0:    
    reversed_number += str(user_num_string[index])
    index -= 1 
            
while user_num > 0:
    digit = user_num % 10
    numbers_sum += digit
    user_num //= 10
                                                                         
print(f"reversed number is {reversed_number}")
print(f"sum of digits: {numbers_sum}")

