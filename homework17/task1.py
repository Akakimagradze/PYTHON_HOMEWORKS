import random

def numbers_gen():
    nums = []
    for _ in range(100):
        nums.append(random.randint(1, 500))
    nums = tuple(nums)
    return nums

def main(tuple_of_nums):
    nums_dict = {"Even": 0, "Odd": 0}
    
    for number in range(len(tuple_of_nums)):
        if tuple_of_nums[number] % 2 == 0:
            nums_dict["Even"] += 1
        else:
            nums_dict["Odd"] += 1        
    print(nums_dict)

if __name__ == "__main__":
    main(numbers_gen())

