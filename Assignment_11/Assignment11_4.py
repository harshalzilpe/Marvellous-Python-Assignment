""" 
    Power Function Using Recursion
    Write a recursive function to calculate x^n
    
    Expected Output:
    power(2, 3) -> 8
"""
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

def main():
    no1 = int(input("Enter the base (x): "))
    no2 = int(input("Enter the exponent (n): "))
    ret = power(no1, no2)
    print(f"power({no1}, {no2}) -> {ret}")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_4.py
    Enter the base (x): 2
    Enter the exponent (n): 3
    power(2, 3) -> 8
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_4.py 
    Enter the base (x): 3
    Enter the exponent (n): 4
    power(3, 4) -> 81
    macbook@Macbooks-MacBook-Pro Assignment_11 % python3 Assignment11_4.py
    Enter the base (x): 10
    Enter the exponent (n): 10
    power(10, 10) -> 10000000000
    macbook@Macbooks-MacBook-Pro Assignment_11 %  
"""