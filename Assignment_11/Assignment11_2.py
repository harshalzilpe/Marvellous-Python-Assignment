""" 
    Factorial Using Recursion
    Write a recursive function to calculate factorial of number
    
    Expected Output (for n=5):
    factorial(5) -> 120
"""
def Fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Fact(n - 1)
        
def main():
    no = int(input("Enter the number: "))
    ret = Fact(no)
    print(f"Factorial({no}) -> {ret}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_2.py
    Enter the number: 5
    Factorial(5) -> 120
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_2.py
    Enter the number: 8
    Factorial(8) -> 40320
    macbook@Macbooks-MacBook-Pro Assignment_11 %  
"""