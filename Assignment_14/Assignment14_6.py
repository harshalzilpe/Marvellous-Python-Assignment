""" 
    Create a class Calculator with methods for add, subtract, multiply, divide. 
    Ask user input for values and call methods accordingly.
"""
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
        
def main():
    calc = Calculator()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = calc.add(num1, num2)
        print(f"Result: {result}")
    elif choice == '2':
        result = calc.subtract(num1, num2)
        print(f"Result: {result}")
    elif choice == '3':
        result = calc.multiply(num1, num2)
        print(f"Result: {result}")
    elif choice == '4':
        result = calc.divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice.")
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_6.py
    Enter first number: 51
    Enter second number: 21

    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Enter choice (1/2/3/4): 1
    Result: 72.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_6.py
    Enter first number: 51
    Enter second number: 21

    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Enter choice (1/2/3/4): 2
    Result: 30.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_6.py
    Enter first number: 51
    Enter second number: 21

    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Enter choice (1/2/3/4): 3
    Result: 1071.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_6.py
    Enter first number: 51
    Enter second number: 21

    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Enter choice (1/2/3/4): 4
    Result: 2.4285714285714284
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""