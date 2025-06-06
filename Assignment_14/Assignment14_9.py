""" 
    Create a class Product with attributes name and price. 
    Implement __eq__ method to compare two products if they are equal in price.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def __str__(self):
        return f"{self.name} - ₹{self.price}"
        
def main():
    name1 = input("Enter name of first product: ")
    price1 = input("Enter price of first product: ")
    product1 = Product(name1, price1)

    name2 = input("Enter name of second product: ")
    price2 = input("Enter price of second product: ")
    product2 = Product(name2, price2)

    if product1 == product2:
        print(f"Both products have the same price: ₹{product1.price}")
    else:
        print(f"The products have different prices:\n"
            f"{product1.name}: ₹{product1.price}\n"
            f"{product2.name}: ₹{product2.price}")
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_9.py
    Enter name of first product: car
    Enter price of first product: 500000
    Enter name of second product: cream 
    Enter price of second product: 55
    The products have different prices:
    car: ₹500000.0
    cream: ₹55.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_9.py
    Enter name of first product: nexon
    Enter price of first product: 50
    Enter name of second product: venue
    Enter price of second product: 50
    Both products have the same price: ₹50.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""