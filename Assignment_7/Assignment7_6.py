""" 
    Write a function that accepts a list of integers and return a list of prime numbers using filter().
    Expected Input:
    Enter the list: 10 11 12 13 14 15 16 17
    Expected Output:
    Prime numbers: [11, 13, 17]
"""
def Chkprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    print("Input Data : ",Data)
    
    Ret = list(filter(Chkprime, Data))

    print("Prime numbers:", Ret)
    
if __name__ == "__main__":
    main()
""" 
    macbook@192 Assignment_7 % python3 Assignment7_6.py
    Enter number of elements : 
    8
    Please enter numeric values : 
    10
    11
    12
    13
    14
    15
    16
    17
    Input Data :  [10, 11, 12, 13, 14, 15, 16, 17]
    Prime numbers: [11, 13, 17]
    macbook@192 Assignment_7 % 
"""