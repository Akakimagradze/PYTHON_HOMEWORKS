def friendship_maker():
    FINISH_KEYWORD = "FINISH"
    friends_dict = {}
    while True:
        user_input = input("Input: ")
        if user_input.upper() == FINISH_KEYWORD:
            break
        
        if "-" in user_input:
            names = user_input.split('-')
            friend1, friend2 = names[0].strip(), names[1].strip()
            
            if friend1 not in friends_dict:
                friends_dict[friend1] = []
            friends_dict[friend1].append(friend2)
            
            if friend2 not in friends_dict:
                friends_dict[friend2] = []
            friends_dict[friend2].append(friend1)
            
    print("Output:")
    for name, friends in friends_dict.items():
        friend_str = ", ".join(friends)
        print(f"{name} - {friend_str}") 

if __name__ == "__main__":
    friendship_maker()

