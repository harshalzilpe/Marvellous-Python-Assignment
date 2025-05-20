""" 
    Print Triangle Pattern using Nested Loops.
    Expected Input:
    Enter a number: 4
    Expected Output:
    *
    * *
    * * *
    * * * *
    
"""
def Pattern(num):
    for i in range(1,num+1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    no = int(input("Enter the number: "))
    
    Pattern(no) 
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_6.py
    Enter the number: 4
    * 
    * * 
    * * * 
    * * * * 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_6.py
    Enter the number: 10
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * * * 
    * * * * * * * 
    * * * * * * * * 
    * * * * * * * * * 
    * * * * * * * * * * 
    macbook@Macbooks-MacBook-Pro Assignment_6 % 
"""