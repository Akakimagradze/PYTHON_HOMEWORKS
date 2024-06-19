class Inset:
    def __init__(self):
        self.elements = []
        
    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)
            
    def member(self, element):
        return element in self.elements
    
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("Didn't find it")
            
    def __str__(self):
        return str(sorted(self.elements))
        
def main():
    inset = Inset()
    inset.insert(32)
    inset.insert(23)
    inset.insert(65)
    inset.insert(52)
    inset.insert(23)
    inset.insert(32)
    inset.insert(65)
         
    print(f"List: {inset.elements}")
    print(f"Is 25 in list?: {inset.member(25)}")    
    print(f"Is 2 in list?: {inset.member(2)}")
    print(f"To String and Sorted List: {inset.__str__()}")
    inset.remove(32)
    print(f"List after removed element: {inset.elements}")
    inset.remove(2)
    
if __name__ == "__main__":
    main()
    
