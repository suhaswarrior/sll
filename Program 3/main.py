class rectangle: # Class name
    def __init__(self, breadth, length): # Constructor
        self.breadth = breadth # Instance variable
        self.length = length

    def area(self): # Method
        return self.breadth * self.length


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = rectangle(a, b) # Object creation
print("Area of rectangle:", obj.area()) # Calling method
