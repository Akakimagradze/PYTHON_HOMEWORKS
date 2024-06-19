class LST(list):
    def __init__(self, lst):
        self.lst = lst
        super().__init__(self.lst)
        
    def min(self):
        if not self.lst:
            raise ValueError("List is empty")
        return min(self.lst)
        
    def max(self):
        if not self.lst:
            raise ValueError("List is empty")
        return max(self.lst)
    
def main():
    random_list = [12, 53, 423, 4, 23, 52]
    my_list = LST(random_list)
    print(my_list.max())
    print(my_list.min())
    
if __name__ == "__main__":
    main()
    
