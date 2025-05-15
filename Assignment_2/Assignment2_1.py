""" 
    Create on module named as Arithmetic which contains 4 function as Add() for addition, Sub() for subtraction,
    Multi() for multiplication and Div() for division. All function accepts two parameters as number and perform
    the operation. Write on python program which call all the function from Arithmetic module by accepting the
    paramters from user.
"""
import Arithmetic

def main():
    value1 = int(input("Enter the first number : "))
    value2 = int(input("Enter the second number : "))
    
    Result = Arithmetic.Add(value1, value2)
    print("Addition is", Result)
    
    Result = Arithmetic.Sub(value1, value2)
    print("Subtraction is", Result)
    
    Result = Arithmetic.Mul(value1, value2)
    print("Multiplication is", Result)
    
    Result = Arithmetic.Div(value1, value2)
    print("Division is", Result)
    
if __name__ == "__main__":
    main()
    
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_1.py
    Enter the first number : 11
    Enter the first number : 21
    Addition is 32
    Subtraction is -10
    Multiplication is 231
    Division is 0.5238095238095238
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_1.py
    Enter the first number : 100
    Enter the first number : 50
    Addition is 150
    Subtraction is 50
    Multiplication is 5000
    Division is 2.0
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""