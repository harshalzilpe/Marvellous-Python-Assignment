""" 
    Write a program which contains filter(), map(), and reduce() in it. Python application which
    contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which greater than or equal to 70 and less than or equal to
    90. Map function will increase each number by 10. Reduce will return product of all that numbers.
    Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter = [76, 89, 86, 90, 70]
    List after map = [89, 99, 96, 100, 80]
    Output of reduce = 6538752000
"""
from functools import reduce

# Range = lambda No : 70 <= No <= 90

# Increase = lambda No : No + 10

# Product = lambda No1, No2 : No1 * No2

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print(f"Enter {Size} numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    print("Your list is",Data)
    
    FData = list(filter(lambda No : 70 <= No <= 90, Data))
    print("List after filter =",FData)
    
    MData = list(map(lambda No : No + 10, FData))
    print("List after map =",MData)
    
    RData = reduce(lambda No1, No2 : No1 * No2, MData)
    print("The product of value after reduced data is",RData)
    
if __name__ =="__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_3.py
    Enter number of elements : 
    12
    Enter 12 numeric values : 
    4 
    34
    36
    76
    68
    24
    89
    23
    86
    90
    45
    70
    Your list is [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List aftyer filter = [76, 89, 86, 90, 70]
    List after map = [86, 99, 96, 100, 80]
    The product of value after reduced data =  6538752000
    macbook@Macbooks-MacBook-Pro Assignment_4 % python3 Assignment4_3.py
    Enter number of elements : 
    5
    Enter 5 numeric values : 
    69
    70
    89
    90
    91
    Your list is [69, 70, 89, 90, 91]
    List aftyer filter = [70, 89, 90]
    List after map = [80, 99, 100]
    The product of value after reduced data is 792000
    macbook@Macbooks-MacBook-Pro Assignment_4 %  
"""