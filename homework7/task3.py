import sys

user_num = int(input("Enter positive integer(0-9999): "))

while user_num < 0 or user_num >= 10000:                      
    user_num = int(input("Enter positive integer(0-9999): "))

reversed_number = 0     
numbers_sum = 0          

print(f"enter number: {user_num}") 

while user_num != 0:                                                        
    each_number = user_num % 10                           #ყოველ იტერაციაზე ინახავს შემოყვანილი რიცხვის ბოლო ციფრს.
    reversed_number = reversed_number * 10 + each_number  #მიღებულ რიცხვს ამრავლებს 10ზე და უმატებს ცვლადში შენახულ მნიშნველობას  
    user_num //= 10                                       #შლის ბოლო ციფრს 
    numbers_sum += each_number                            #თითოეულ იტერაციაზე ცვლადს ამატებს მიღებულ ციფრს.

print(f"reversed number is {reversed_number}")
print(f"sum of digits: {numbers_sum}")

sys.exit(1)

