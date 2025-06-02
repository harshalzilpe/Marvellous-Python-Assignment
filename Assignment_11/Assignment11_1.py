""" 
    Print Numbers Using Recursion
    Write a recursive function to print numbers from 1 to N
    
    Expected Output (for n=5):
    1 2 3 4 5
"""
def Num(no):
    if no >= 1:
        Num(no - 1)
        print(no, end=" ")
        
def main():
    no = int(input("Enter the number: "))
    Num(no)
    print()

if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_1.py
    Enter the number: 5
    1 2 3 4 5 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_1.py
    Enter the number: 9
    1 2 3 4 5 6 7 8 9 
    macbook@Macbooks-MacBook-Pro Assignment_11 % 
"""