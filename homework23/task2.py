class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        
        return self.elements.pop(0)
    
def main():
    my_queue = Queue()
    nums_list = [1,2,3,4,5]
    for i in nums_list:
        my_queue.insert(i)
    print(f"List: {my_queue.elements}")
    
    print(f"Removed: {my_queue.pop()}")
    print(f"Removed: {my_queue.pop()}")
    print(f"Removed: {my_queue.pop()}")

    print(f"List: {my_queue.elements}")

if __name__ == "__main__":
    main()
    
