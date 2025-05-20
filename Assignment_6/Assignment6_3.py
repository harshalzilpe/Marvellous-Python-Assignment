""" 
    Accept a number from the user and print its multiplication table up to 10.
    Expected Input:
    Enter a number: 7
    Expected Output:
    7 * 1 = 7
    7 * 2 = 14
    ....
    7 * 10 = 70
    
"""
def Table(num):
    mul = 0
    for i in range(1,11):
        mul = num * i
        print(f"{num} * {i} = {mul}")

def main():
    no = int(input("Enter the number: "))
    
    Table(no) 
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_3.py
    Enter the number: 7
    7 * 1 = 7
    7 * 2 = 14
    7 * 3 = 21
    7 * 4 = 28
    7 * 5 = 35
    7 * 6 = 42
    7 * 7 = 49
    7 * 8 = 56
    7 * 9 = 63
    7 * 10 = 70
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_3.py
    Enter the number: 22
    22 * 1 = 22
    22 * 2 = 44
    22 * 3 = 66
    22 * 4 = 88
    22 * 5 = 110
    22 * 6 = 132
    22 * 7 = 154
    22 * 8 = 176
    22 * 9 = 198
    22 * 10 = 220
    macbook@Macbooks-MacBook-Pro Assignment_6 % 
"""