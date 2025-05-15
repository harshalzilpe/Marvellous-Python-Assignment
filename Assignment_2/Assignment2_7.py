""" 
    Write a program which accept one number and display below pattern
    Input: 5
    Output:1   2   3   4   5 
           1   2   3   4   5  
           1   2   3   4   5
           1   2   3   4   5
           1   2   3   4   5
"""
def Pattern(no):
    for i in range(no):
        for j in range(1, no + 1):
            print(j, end="   ")
        print()

def main():
    value = int(input("Enter the number : "))
    
    Pattern(value)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_7.py
    Enter the number : 5
    1   2   3   4   5   
    1   2   3   4   5   
    1   2   3   4   5   
    1   2   3   4   5   
    1   2   3   4   5   
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_7.py
    Enter the number : 3
    1   2   3   
    1   2   3   
    1   2   3   
    macbook@Macbooks-MacBook-Pro Assignment_2 % python3 Assignment2_7.py
    Enter the number : 2
    1   2   
    1   2   
    macbook@Macbooks-MacBook-Pro Assignment_2 % 
"""