""" 
    Arithmetic Operations on Two Numbers
    Write a program to accept two integers from the user and display their:
    • Sum  • Difference  • Product  • Division
    Input:
    Enter first number: 10
    Enter second number: 2
    Output:
    Sum: 12
    Difference: 8
    Product: 20
    Division: 5.0
"""
def Sum(value1, value2):
    Ans = value1 + value2
    return Ans

def Dif(value1, value2):
    Ans = value1 - value2
    return Ans

def Pro(value1, value2):
    Ans = value1 * value2
    return Ans

def Div(value1, value2):
    Ans = value1 / value2
    return Ans

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    
    ret1 = Sum(no1, no2)
    ret2 = Dif(no1, no2)
    ret3 = Pro(no1, no2)
    ret4 = Div(no1, no2)
    
    print(f"Sum: {ret1}")
    print(f"Difference: {ret2}")
    print(f"Product: {ret3}")
    print(f"Div: {ret4}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_1.py 
    Enter the first number: 12
    Enter the second number: 5
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_1.py
    Enter the first number: 10
    Enter the second number: 2
    Sum: 12
    Difference: 8
    Product: 20
    Division: 5.0
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_1.py
    Enter the first number: -10
    Enter the second number: 2 
    Sum: -8
    Difference: -12
    Product: -20
    Division: -5.0
    macbook@Macbooks-MacBook-Pro Assignment_5 %
"""