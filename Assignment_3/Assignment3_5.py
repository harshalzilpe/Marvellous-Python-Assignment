""" 
    Write a program which accept N numbers from user and store it into list. Return addition of all prime numbers from the list.
    Main python file accepts N numbers from user and pass each number to ChkPrime() function which is a part of our user defined
    module named as MarvellousNum. Name of the function from main python file should be ListPrime.
    Input: Number of elements: 11
    Input Elements: 13 5 45 7 4 56 10 34 2 5 8
    This are the prime numbers: 13, 5, 7, 2, 5
    Output: 54 
"""
import MarvellousNum

def ListPrime(no):
    sum = 0
    list = []
    
    for num in no:
        if MarvellousNum.ChkPrime(num):
            list.append(num)
            sum += num
    print(f"Prime numbers from list are {list}.")
    return sum

def main():
    value = int(input("Enter the number of elements : "))
    
    print("Enter the numbers ")
    elements = list(map(int, input().split()))
    
    if len(elements) != value:
        print(f"Error: Expected {value} numbers but got {len(elements)}.")
        return
    result = ListPrime(elements)
    
    print("Output:", result)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_5.py
    Enter the number of elements : 11
    Enter the numbers 
    13 5 45 7 4 56 10 34 2 5 8
    Prime numbers from list are [13, 5, 7, 2, 5].
    Output: 32
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_5.py
    Enter the number of elements : 5
    Enter the numbers 
    3 5 6 7 9
    Prime numbers from list are [3, 5, 7].
    Output: 15
    macbook@Macbooks-MacBook-Pro Assignment_3 % 
"""