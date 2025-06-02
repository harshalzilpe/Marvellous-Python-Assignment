""" 
    Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers.
    List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply
    each number by 2. Reduce will return maximum number from that numbers. (You can use normal functions instead of lambda functions).
    Input List: [2, 70, 11, 10, 17, 23, 31, 77]
    List after filter = [2, 11, 17, 23, 31]
    List after map = [4, 22, 34, 46, 32]
    Output of reduce = 62
"""
from functools import reduce

def ChkPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
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

    FData = list(filter(ChkPrime, Data))
    print("List after filter : ",FData)

    MData = list(map(lambda No : No * 2, FData))
    print("List after Map : ",MData)

    RData = reduce(lambda a,b : a if a > b else b, MData)
    print("List after Reduce : ",RData)

if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_5.py
    Enter number of elements : 
    8
    Please enter numeric values : 
    2
    70
    11
    10
    17
    23
    31
    77
    Input Data :  [2, 70, 11, 10, 17, 23, 31, 77]
    List after filter :  [2, 11, 17, 23, 31]
    List after Map :  [4, 22, 34, 46, 62]
    List after Reduce :  62
    macbook@Macbooks-MacBook-Pro Assignment_10 % 
"""