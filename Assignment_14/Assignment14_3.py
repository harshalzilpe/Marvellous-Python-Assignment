""" 
    Create a class Book with private attribute price. Add methods to get and set the price. Show encapsulation.
"""
class Book:
    def __init__(self):
        self.__price = 0

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")
        
def main():
    obj1 = Book()
    user_input = input("Enter the price of the book: ")

    price = float(user_input)
    obj1.set_price(price)

    print("The price of the book is:", obj1.get_price())
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_3.py
    Enter the price of the book: 500
    The price of the book is: 500.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""