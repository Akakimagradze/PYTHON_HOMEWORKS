words_list = ["Python", "Javascript", "C", "C++", "Java", "SQL", "C#", "Rust", "Swift"]
filtered_list = []

for word in range(len(words_list)):
    if len(words_list[word]) > 3:
        filtered_list.append(words_list[word].upper())

print(filtered_list)   

 