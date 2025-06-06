""" 
    Write a class Rectangle with length and width. Add a method to compute area and perimeter.
    Area: 50, Perimeter: 30
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
        
def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    rect = Rectangle(length, width)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_2.py
    Enter the length of the rectangle: 10
    Enter the width of the rectangle: 5
    Area: 50.0
    Perimeter: 30.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""