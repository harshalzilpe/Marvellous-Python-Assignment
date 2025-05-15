""" 
    Write a program which accept one number and display below pattern.
    Input: 5
    Output: * * * * *
            * * * * *
            * * * * *
            * * * * *
            * * * * *
"""
def Pattern(no):
    for i in range(no):
        print("*    " * no)
    return no

def main():
    value = int(input("Enter the number : "))
    
    Pattern(value)
    
if __name__ == "__main__":
    main()
    
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_2.py
    Enter the number : 5
    *    *    *    *    *    
    *    *    *    *    *    
    *    *    *    *    *    
    *    *    *    *    *    
    *    *    *    *    *    
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_2.py
    Enter the number : 2
    *    *    
    *    *    
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_2.py
    Enter the number : 3
    *    *    *    
    *    *    *    
    *    *    *    
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""