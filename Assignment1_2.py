""" 
    Write a program which contains one fun ction named as ChkNum() which accept one parameter as number. 
    If number is even then it should display "Even number" otherwise display "Odd number" on console.
    Input: 11     Output: Odd Number
    Input: 8      Output: Even Number
"""

def ChkNum(number):
    
    if(number % 2):
        print(number,"is Odd Number.")
    else:
        print(number,"is Even Number.")

def main():
    print("Enter the number : ")
    value1 = int(input())

    ChkNum(value1)
    
if __name__ == "__main__":
    main() 
    
""" 
    macbook@192 Assignment % python3 Assignment1_2.py
    Enter the number : 
    11
    11 is Odd Number.
    macbook@192 Assignment % python3 Assignment1_2.py
    Enter the number : 
    8
    8 is Even Number.
    macbook@192 Assignment % 
"""
