""" 
    Write a program which contains one lambda function which accepts two parameters and return its multiplication.
    Input: 4    3        Output: 12
    Input: 6    3        Output: 18
"""

def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the number number : "))

    Result = ((lambda a, b : a * b) (no1, no2))
    
    print(f"The multiplication of {no1} and {no2} is {Result}.")

if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_2.py
    Enter the first number : 4
    Enter the number number : 3
    The multiplication of 4 and 3 is 12.
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_2.py
    Enter the first number : 6
    Enter the number number : 3
    The multiplication of 6 and 3 is 18.
    macbook@Macbooks-MacBook-Pro Assignment_10 % 
"""