""" 
    Count Zeros in a Number (Recursively)
    Write a recursive function to count how many zeros are in the given number.
    
    Expected Output:
    count_zeros(1020300) -> 4
"""
def CntZero(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    last_digit = n % 10
    if last_digit == 0:
        return 1 + CntZero(n // 10)
    else:
        return CntZero(n // 10)

def main():
    no = int(input("Enter the number: "))
    ret = CntZero(no)
    print(f"The count zero from {no} -> {ret}")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_5.py
    Enter the number: 1020300
    The count zero from 1020300 -> 4
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_5.py
    Enter the number: 12345
    The count zero from 12345 -> 0
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_5.py
    Enter the number: 0
    The count zero from 0 -> 1  
"""