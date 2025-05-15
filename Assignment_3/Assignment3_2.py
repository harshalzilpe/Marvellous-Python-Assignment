""" 
    Write a program which accept N numbers from user and store it into list. return Maximum number from that list.
    Input: Number of elements: 7
    Input Elements: 13 5 45 7 4 56 34
    Output: 56
"""
def Maximum(no):
    numbers = []
    print("Enter the numbers ")
    for i in range(no):
        num = int(input())
        numbers.append(num)
        
    print("Your list is",list(numbers))
    
    ans = numbers[0] 
    for num in numbers:
        if num > ans:
            ans = num
    return ans
    
def main():
    value = int(input("Enter the number of elements : "))
    
    Result = Maximum(value)
    
    print(f"Maximum number from the list is {Result}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_2.py
    Enter the number of elements : 7
    Enter the numbers 
    13
    5
    45
    7
    4
    56
    34
    Your list is [13, 5, 45, 7, 4, 56, 34]
    Maximum number from the list is 56
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_2.py
    Enter the number of elements : 5
    Enter the numbers 
    11
    21
    10
    101
    51
    Your list is [11, 21, 10, 101, 51]
    Maximum number from the list is 101
    macbook@Macbooks-MacBook-Pro Assignment_3 % 
"""