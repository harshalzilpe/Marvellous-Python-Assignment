""" 
    Write aprogram which accepts one number from user and addition of its factors.
    Input: 12
    Output: 16  (1+2+3+4+6)
"""
def FactorSum(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum += i
    return sum

def main():
    value = int(input("Enter the number : "))
    
    Result = FactorSum(value)
    
    print(f"The addition of {value} factors is {Result}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_4.py
    Enter the number : 12
    The addition of 12 factors is 16
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_4.py
    Enter the number : 4
    The addition of 4 factors is 3
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""