""" 
    Write a program which accept number from user and check whether that number is positive or
    negative or zero.
    Input: 11       Output: Positive Number
    Input: -8       Output: Negative Number
    Input: 0        Output: Zero
"""

def ChkNum(no):
    
    if(no > 0):
        print("This s Positive Number.")
    elif(no < 0):
        print("This is Negative Number.")
    else:
        print("This is Zero")

def main():
    print("Enter the number : ")
    value = int(input())
    
    ChkNum(value)
    
if __name__ == "__main__":
    main() 
    
""" 
    macbook@192 Assignment % python3 Assignment1_6.py
    Enter the number : 
    11
    This s Positive Number.
    macbook@192 Assignment % python3 Assignment1_6.py
    Enter the number : 
    -8
    This is Negative Number.
    macbook@192 Assignment % python3 Assignment1_6.py
    Enter the number : 
    0
    This is Zero
    macbook@192 Assignment % 
""" 