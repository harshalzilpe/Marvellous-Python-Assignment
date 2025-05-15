""" 
    Write a program which accept N numbers from user and store it into list. Accept one another number from user and return frequency of that number from list.
    Input: Number of elements: 11
    Input Elements: 13 5 45 7 4 56 5 34 2 5
    Elements to search: 5
    Output: 3
"""
def SearchNum(no):
    numbers = []
    print("Enter the numbers ")
    for i in range(no):
        num = int(input())
        numbers.append(num)
        
    print("Your list is",list(numbers))
    
    find = int(input("Enter the number that you want to search : "))
    
    frequency = numbers.count(find)
    
    return frequency
    
def main():
    value = int(input("Enter the number of elements : "))
    
    Result = SearchNum(value)
    
    print(f"Maximum number from the list is {Result}")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_4.py
    Enter the number of elements : 11
    Enter the numbers 
    13
    5
    45
    7
    4
    56
    5
    34
    2
    5
    65
    Your list is [13, 5, 45, 7, 4, 56, 5, 34, 2, 5, 65]
    Enter the number that you want to search : 5
    Maximum number from the list is 3
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_4.py
    Enter the number of elements : 5
    Enter the numbers 
    1
    0
    1
    1
    0
    Your list is [1, 0, 1, 1, 0]
    Enter the number that you want to search : 1
    Maximum number from the list is 3
    macbook@Macbooks-MacBook-Pro Assignment_3 % 
"""