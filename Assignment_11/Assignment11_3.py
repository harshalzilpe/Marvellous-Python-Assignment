""" 
    Sum of Digits
    Write a recursive function to calculate the sum of digits of a number
    
    Expected Output (for n=1234):
    factorial(1234) -> 10
"""
def SumNum(n):
    if n == 0:
        return 0
    return n % 10 + SumNum(n // 10)
        
def main():
    no = int(input("Enter the number: "))
    ret = SumNum(no)
    print(f"Sum of digits ({no}) -> {ret}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_3.py
    Enter the number: 12345
    Sum of digits (12345) -> 15
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_3.py
    Enter the number: 1234
    Sum of digits (1234) -> 10
    macbook@Macbooks-MacBook-Pro Assignment_11 % 
"""