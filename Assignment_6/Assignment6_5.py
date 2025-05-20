""" 
    Accept a number from the user and check whether it is prime or not.
    Expected Input:
    Enter a number: 11
    Expected Output:
    11 is a prime number.
    
"""
def ChkPrime(num):
    if num <= 1:
        print(f"{num} is not a prime number.")
        return

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return

    print(f"{num} is a prime number.")

def main():
    no = int(input("Enter the number: "))
    
    ChkPrime(no) 
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_5.py
    Enter the number: 11
    11 is a prime number.
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_5.py
    Enter the number: 1
    1 is not a prime number.
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_5.py
    Enter the number: 2
    2 is a prime number.
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_5.py
    Enter the number: 9
    9 is not a prime number.
    macbook@Macbooks-MacBook-Pro Assignment_6 % 
"""