""" 
    Find Largest Among Three Number
    Accept three numbers from the user and print the largest using nested if-else statements.
    Input:
    Enter three number: 5 9 3
    Output:
    Largest number is 9.
"""
def LargestNo(num1, num2, num3):
    largest = 0
    if num1 >= num2:
        if num1 >=num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 >= num3:
            largest = num2
        else:
            largest = num3
    return largest

def main():
    no1 = int(input("Enter first numbers: "))
    no2 = int(input("Enter second numbers: "))
    no3 = int(input("Enter third numbers: "))
    
    ret = LargestNo(no1, no2, no3)
    print(f"{ret} is largest number amongs remaining two numbers.")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_4.py
    Enter first numbers: 5
    Enter second numbers: 9
    Enter third numbers: 3
    9 is largest number amongs remaining two numbers.
    macbook@Macbooks-MacBook-Pro Assignment_5 % 
"""