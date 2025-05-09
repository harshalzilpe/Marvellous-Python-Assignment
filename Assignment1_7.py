""" 
    Write a program which contains one function that one number from user and
    return true if number is divisible by 5 otherwise return false.
    Input: 8    Output: False
    Input: 25   Output: True
"""

def ChkNum(no):
    if(no % 5):
        print(bool(False))
    else:
        print(bool(True))

def main():
    print("Enter the number : ")
    value = int(input())
    
    ChkNum(value)
    
if __name__ == "__main__":
    main() 
    
""" 
    macbook@192 Assignment % python3 Assignment1_7.py
    Enter the number : 
    8
    True
    macbook@192 Assignment % python3 Assignment1_7.py
    Enter the number : 
    8
    False
    macbook@192 Assignment % python3 Assignment1_7.py
    Enter the number : 
    25
    True
    macbook@192 Assignment % python3 Assignment1_7.py
    Enter the number : 
    -8
    False
    macbook@192 Assignment % python3 Assignment1_7.py
    Enter the number : 
    -25
    True
    macbook@192 Assignment % 
"""