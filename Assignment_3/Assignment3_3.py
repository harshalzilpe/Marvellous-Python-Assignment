""" 
    Write a program which accept N numbers from user and store it into list. return Minimum number from that list.
    Input: Number of elements: 4
    Input Elements: 13 5 45 7
    Output: 5
"""
def Minimum(no):
    numbers = []
    print("Enter the numbers ")
    for i in range(no):
        num = int(input())
        numbers.append(num)
        
    print("Your list is",list(numbers))
    
    ans = numbers[0] 
    for num in numbers:
        if num < ans:
            ans = num
    return ans
    
def main():
    value = int(input("Enter the number of elements : "))
    
    Result = Minimum(value)
    
    print(f"Maximum number from the list is {Result}")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_3.py
    Enter the number of elements : 4
    Enter the numbers 
    13
    5
    45
    7
    Your list is [13, 5, 45, 7]
    Maximum number from the list is 5
    macbook@Macbooks-MacBook-Pro Assignment_3 % python3 Assignment3_3.py
    Enter the number of elements : 5
    Enter the numbers 
    101
    51
    10
    11
    21
    Your list is [101, 51, 10, 11, 21]
    Maximum number from the list is 10
    macbook@Macbooks-MacBook-Pro Assignment_3 % 
"""