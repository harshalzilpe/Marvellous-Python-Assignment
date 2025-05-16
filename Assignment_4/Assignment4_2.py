""" 
    Write a program which contains one lambda function which accepts two parameter and return its multiplication.
    Input: 4  3      Output: 12
    Input: 6  3      Output: 18
"""
def main():
    value1 = int(input("Enter the first number : "))
    value2 = int(input("Enter the second number : "))
    
    mul = lambda no1, no2 : no1 * no2
    
    Result = mul(value1, value2)
    
    print(f"The multiplication of {value1} * {value2} is {Result}.")
    
if __name__ =="__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_1.py
    Enter the number : 4
    The power of two of 4 is 16.
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_1.py
    Enter the number : 6
    The power of two of 6 is 36.
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_1.py
    Enter the number : 8
    The power of two of 8 is 64.
    macbook@Macbooks-MacBook-Pro Assignment_4 % 
"""