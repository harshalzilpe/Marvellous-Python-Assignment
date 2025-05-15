""" 
    Write a program which accept one number for and check whether number is prime or not.
    Input: 5
    Output: It is Prime Number
"""
def ChkNum(no):
    if no <= 1:
        return False
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False
    return True
    
def main():
    value = int(input("Enter the number : "))
    
    if ChkNum(value):
        print(f"{value} is a Prime Number")
    else:
        print(f"{value} is not Prime Number")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_5.py
    Enter the number : 5
    5 is a Prime Number
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_5.py
    Enter the number : 6
    6 is not Prime Number
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_5.py
    Enter the number : 7
    7 is a Prime Number
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_5.py
    Enter the number : 9
    9 is not Prime Number
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""