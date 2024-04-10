def sorter(list1, list2):
    main_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            main_list.append(list1[i])
            i += 1
        else:
            main_list.append(list2[j])
            j += 1

    while i < len(list1):
        main_list.append(list1[i])
        i += 1

    while j < len(list2):
        main_list.append(list2[j])
        j += 1
    
    return main_list

def main():
    list1 = [3, 8, 12, 15]
    list2 = [1, 6, 10, 14]
    print(sorter(list1, list2))
    list3 = [1, 3, 10]
    list4 = [0, 4, 7, 9]
    print(sorter(list3, list4))
    
if __name__ == "__main__":
    main()
    
