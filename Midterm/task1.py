def info_teller():
    user_name = input("Enter your name: ")
    user_surname = input("Enter your username: ")
    user_age = int(input("Enter your age: "))
    print(f"Hello {user_name} {user_surname}.")
    print(f"Age: {user_age}.")

if __name__ == "__main__":
    info_teller()

