""" 
    Write a program which accept number from user and return number of digits in that number.
    Input: 5187934
    Output: 7
"""
def CntDigit(no):
    count = 0
    while no > 0:
        no = no // 10
        count += 1
    return count
    
def main():
    value = int(input("Enter the number : "))
    
    Result = CntDigit(value)
    print(f"The number of digits in {value} is {Result}.")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_9.py 
    Enter the number : 5187934
    The number of digits in 5187934 is 7.
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_9.py
    Enter the number : 1234567890
    The number of digits in 1234567890 is 10.
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_9.py
    Enter the number : 098765
    The number of digits in 98765 is 5.
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""