""" 
    Accept a number from the user and print its factorial using for loop.
    Expected Input:
    Enter a number: 5
    Expected Output:
    Factorial of 5 is 120
    
"""
def Factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print(f"Factorial of {num} is {fact}")

def main():
    no = int(input("Enter the number: "))
    
    Factorial(no) 
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_4.py
    Enter the number: 5
    Factorial of 5 is 120
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_4.py
    Enter the number: 8
    Factorial of 8 is 40320
    macbook@Macbooks-MacBook-Pro Assignment_6 % 
"""