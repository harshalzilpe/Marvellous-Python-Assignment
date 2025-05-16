""" 
    Write a program which contains filter(), map(), and reduce() in it. Python application which
    contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which even. Map function will its sqaure. Reduce will return 
    addition of all that numbers.
    Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    List after filter = [2, 4, 4, 2, 8, 10]
    List after map = [4, 16, 16, 4, 64, 100]
    Output of reduce = 204
"""
from functools import reduce

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print(f"Enter {Size} numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    print("Your list is",Data)
    
    FData = list(filter(lambda No : No % 2 == 0, Data))
    print("List after filer =",FData)
    
    MData = list(map(lambda No : No * No, FData))
    print("List after map =",MData)
    
    RData = reduce(lambda No1, No2 : No1 + No2, MData)
    print("The addition of value after reduced data is",RData)
    
if __name__ =="__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_4.py
    Enter number of elements : 
    10  
    Enter 10 numeric values : 
    5
    2
    3
    4
    3
    4
    1
    2
    8
    10
    Your list is [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    List after filer = [2, 4, 4, 2, 8, 10]
    List after map = [4, 16, 16, 4, 64, 100]
    The addition of value after reduced data is 204
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_4.py
    Enter number of elements : 
    5
    Enter 5 numeric values : 
    12
    15
    16
    11
    18
    Your list is [12, 15, 16, 11, 18]
    List after filer = [12, 16, 18]
    List after map = [144, 256, 324]
    The addition of value after reduced data is 724
    macbook@Macbooks-MacBook-Pro Assignment_4 %   
"""