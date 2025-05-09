""" 
    Write a program which display 10 to 1 on screen.
    Output: 10 9 8 7 6 5 4 3 2 1
"""

def Reverse(no):
    
    for no in range(no,0,-1):
        print(no, end=" ")

def main():
    print("Enter the number : ")
    value = int(input())
    
    Reverse(value)
    
if __name__ == "__main__":
    main() 
    
""" 
    macbook@192 Assignment % python3 Assignment1_5.py
    Enter the number : 
    10
    10 9 8 7 6 5 4 3 2 1
    macbook@192 Assignment % python3 Assignment1_5.py
    Enter the number : 
    5
    5 4 3 2 1
    macbook@192 Assignment % 
"""