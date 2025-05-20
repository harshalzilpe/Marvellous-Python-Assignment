""" 
    Accept a 5 numbers from the user. Find and print the largest number.
    Expected Input:
    Enter 5 numbers: 23 89 12 56 45
    Expected Output:
    Maximum number is 89.
    
"""
def Maximum(no):
    Max = no[0]
    for i in no:
        if i > Max:
            Max = i
    print(f"Maximum number is {Max}.")
    
def main():
    Num = []
    print("Enter 5 numbers....")
    for i in range(5):
        ret = int(input(f"Enter number {i+1}: "))
        Num.append(ret)  
    print("Your entered 5 numbers are",Num)
    
    Maximum(Num)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_7.py
    Enter 5 numbers....
    Enter number 1: 23
    Enter number 2: 89
    Enter number 3: 12
    Enter number 4: 56
    Enter number 5: 45
    Your entered 5 numbers are [23, 89, 12, 56, 45]
    Maximum number is 89.
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_7.py
    Enter 5 numbers....
    Enter number 1: 10
    Enter number 2: 11
    Enter number 3: 21
    Enter number 4: 101
    Enter number 5: 51
    Your entered 5 numbers are [10, 11, 21, 101, 51]
    Maximum number is 101.

"""