""" 
    Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
    Input: Numbers of elements: 6
    Input Elements: 13 5 45 7 4 56
    Output: 130
"""
def Addition(no):
    numbers = []
    print("Enter the numbers ")
    for i in range(no):
        num = int(input())
        numbers.append(num)
        
    print("Your list is",list(numbers))
    
    total = 0
    for num in numbers:
        total += num
    return total
    
def main():
    value = int(input("Enter the number of elements : "))
    
    Result = Addition(value)
    
    print(f"The addition of all element from the given list is {Result}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_1.py
    Enter the number of elements : 6
    Enter the numbers 
    13
    5
    45
    7
    4
    56
    Your list is [13, 5, 45, 7, 4, 56]
    The addition of all element from the given list is 130
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_1.py
    Enter the number of elements : 5
    Enter the numbers 
    10
    11
    21
    51
    101
    Your list is [10, 11, 21, 51, 101]
    The addition of all element from the given list is 194
    macbook@Macbooks-MacBook-Pro Assignment_3 % 
"""