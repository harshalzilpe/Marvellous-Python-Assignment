""" 
    Write a program which contains one lambda function which accepts one parameter and return power of two.
    Input: 4        Output: 16
    Input: 8        Output: 64
"""

def main():
    no = int(input("Enter the number : "))
    
    Result = ((lambda a : a * a) (no))
    
    print(f"The power of two of {no} is {Result}.")

if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_1.py
    Enter the number : 4
    The power of two of 4 is 16.
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_1.py
    Enter the number : 6
    The power of two of 6 is 36.
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_1.py
    Enter the number : 8
    The power of two of 8 is 64.
    macbook@Macbooks-MacBook-Pro Assignment_10 % 
"""