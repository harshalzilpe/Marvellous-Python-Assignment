""" 
    Print Pattern Using Recursion (Right Triangle)
    Write a recursive function to print the following pattern.
    
    Expected Output: 
    *
    *   *
    *   *   *
    *   *   *   *
"""
def Pattern(a, b=0):
    if a == 0:
        return
    Pattern(a - 1)
    for i in range(a):
        print("*", end="   ")
    print()

def main():
    no = int(input("Enter the number: "))
    Pattern(no)
    
if __name__ == "__main__":
    main()
"""  
macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_7.py
Enter the number: 4
*   
*   *   
*   *   *   
*   *   *   *   
macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_7.py
Enter the number: 5
*   
*   *   
*   *   *   
*   *   *   *   
*   *   *   *   *   
macbook@Macbooks-MacBook-Pro Assignment_11 %  
"""