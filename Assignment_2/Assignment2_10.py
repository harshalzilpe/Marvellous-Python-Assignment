""" 
    Write a program which accept number from user and return additionm of digits in that number.
    Input: 5187934
    Output: 37
"""
def SumDigit(no):
    total = 0
    while no > 0:
        digit = no % 10
        total += digit
        no = no // 10
    return total
    
def main():
    value = int(input("Enter the number : "))
    
    Result = SumDigit(value)
    print(f"The Addition of {value} is {Result}.")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_10.py
    Enter the number : 5187934
    The Addition of 5187934 is 37.
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_10.py
    Enter the number : 1234567890
    The Addition of 1234567890 is 45.
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_10.py
    Enter the number : 098765
    The Addition of 98765 is 35.
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""