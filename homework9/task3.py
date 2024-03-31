user_date = input("Enter a date: ")

date = user_date[8:10] + "-" + user_date[5:7] + "-" + user_date[0:4]
time = str(int(user_date[11:13]) % 12) + user_date[13:19]
timezone = user_date[26] + str(int(user_date[27:29]))

print(f"{date} {time} {timezone}") 
print("22-03-2024 7:17:42 +0")