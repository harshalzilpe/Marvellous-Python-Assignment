""" 
    Sum of First N Natural  Numbers
    Write a recursive function to calculate sum from 1 to n.
    
    Expected Output:
    sum_n(5) -> 15
"""
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

def main():
    no = int(input("Enter the number: "))
    ret = sum_n(no)
    print(f"The sum of first {no} natural numbers is -> {ret}")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_6.py
    Enter the number: 5
    The sum of first 5 natural numbers is -> 15
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_6.py
    Enter the number: 7
    The sum of first 7 natural numbers is -> 28
    macbook@Macbooks-MacBook-Pro Assignment_11 %  
"""