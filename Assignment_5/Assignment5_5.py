""" 
    Even or Odd Number Check
    Write a program to check whether the entyerd number is even or odd.
    Input:
    Enter three number: 17
    Output:
    17 is an odd number.
"""
def OddEven(num):
    if num % 2:
        print(f"{num} is an odd number.")
    else:
        print(f"{num} is an even number.")

def main():
    no = int(input("Enter the numbers: "))
    
    OddEven(no)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_5.py
    Enter the numbers: 17
    17 is an odd number.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_5.py
    Enter the numbers: 18
    18 is an even number.
    macbook@Macbooks-MacBook-Pro Assignment_5 %  
"""