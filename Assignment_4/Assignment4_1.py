""" 
    Write a program which contains one lambda function which accepts one parameter and return power of two.
    Input: 4        Output: 16
    Input: 6        Output: 64
"""
def main():
    value = int(input("Enter the number : "))
    
    power = lambda x : x * x
    
    result = power(value)
    
    print(f"The power of two of {value} is {result}.")
    
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