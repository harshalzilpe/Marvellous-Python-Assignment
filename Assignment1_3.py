""" 
    Write a program which contains one function nmaed as Add() which accepts two numbers
    from user and return addition of that two numbers.
    Input: 11   5       Output: 16
"""

def Add(no1, no2):
    ans = no1 + no2
    return ans

def main():
    print("Enter the number : ")
    value1 = int(input())
    
    print("Enter the number : ")
    value2 = int(input())
    
    result  = Add(value1, value2)
    
    print("Addition is ",result)
    
if __name__ == "__main__":
    main() 

""" 
    macbook@192 Assignment % python3 Assignment1_3.py
    Enter the number : 
    11
    Enter the number : 
    5
    Addition is  16
    macbook@192 Assignment % python3 Assignment1_3.py
    Enter the number : 
    -11
    Enter the number : 
    -21
    Addition is  -32
    macbook@192 Assignment % python3 Assignment1_3.py
    Enter the number : 
    -51
    Enter the number : 
    101
    Addition is  50
    macbook@192 Assignment % 
"""