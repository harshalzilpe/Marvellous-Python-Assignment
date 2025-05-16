""" 
    Write a program which contains filter(), map(), and reduce() in it. Python application which
    contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return 
    Maximum number from that numbers.
    Input List = [2, 70, 11, 10, 17, 23, 31, 77]
    List after filter = [2, 11, 17, 23, 31]
    List after map = [4, 22, 34, 46, 62]
    Output of reduce = 62
"""
from functools import reduce

def ChkPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print(f"Enter {Size} numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    print("Your list is",Data)
    
    FData = list(filter(lambda x: ChkPrime(x), Data))
    print("List after filter =",FData)
    
    MData = list(map(lambda No : No * 2, FData))
    print("List after map =",MData)
    
    RData = reduce(lambda a, b : a if a > b else b, MData)
    print("The maximum number from map list is",RData)
    
if __name__ =="__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_5.py
    Enter number of elements : 
    8
    Enter 8 numeric values : 
    2
    70
    11
    10
    17
    23
    31
    77
    Your list is [2, 70, 11, 10, 17, 23, 31, 77]
    List after filter = [2, 11, 17, 23, 31]
    List after map = [4, 22, 34, 46, 62]
    The maximum number from map list is 62
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_5.py
    Enter number of elements : 
    5
    Enter 5 numeric values : 
    9
    6
    7
    3
    4
    Your list is [9, 6, 7, 3, 4]
    List after filter = [7, 3]
    List after map = [14, 6]
    The maximum number from map list is 14
    macbook@Macbooks-MacBook-Pro Assignment_4 % 
"""