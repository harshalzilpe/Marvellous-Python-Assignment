""" 
    Write a program which accept number from user and print that number of "*" on screen.
    Input: 5    Output: * * * * *
"""

def PrintStar(no):
    for no in range(no):
        print("*", end=" ")

def main():
    print("Enter the number : ")
    value = int(input())
    
    PrintStar(value)
    
if __name__ == "__main__":
    main() 
    
""" 
    macbook@192 Assignment % python3 Assignment1_8.py
    Enter the number : 
    5
    * * * * *                                                                      
    macbook@192 Assignment % 
"""