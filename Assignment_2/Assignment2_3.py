""" 
    Write a program which accept one number from user and return its factorial.
    Input: 5
    Output: 120
"""
def Factorial(no):
    if no == 0 or no == 1:
        return 1
    else:
        fact = 1
        for i in range(1, no + 1):
            fact *= i
    return fact

def main():
    value = int(input("Enter the number : "))
    
    Result = Factorial(value)
    print(f"Factorial of {value} is {Result}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_3.py
    Enter the number : 5
    Factorial of 5 is 120
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_3.py
    Enter the number : 2
    Factorial of 2 is 2
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_3.py
    Enter the number : 8
    Factorial of 8 is 40320
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""