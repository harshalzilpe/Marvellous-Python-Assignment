""" 
    Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers.
    List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal 
    to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
    Input List: [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter = [76, 89, 86, 90, 70]
    List after map = [86, 99, 96, 100, 80]
    Output of reduce = 6538752000
"""
from functools import reduce

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    print("Input Data : ",Data)

    FData = list(filter(lambda No : 70 <= No <= 90, Data))
    print("List after filter : ",FData)

    MData = list(map(lambda No : No + 10, FData))
    print("List after Map : ",MData)

    RData = reduce(lambda A,B : A * B, MData)
    print("List after Reduce : ",RData)

if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_3.py
    Enter number of elements : 
    12
    Please enter numeric values : 
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
    Input Data :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter :  [76, 89, 86, 90, 70]
    List after Map :  [86, 99, 96, 100, 80]
    List after Reduce :  6538752000
    macbook@Macbooks-MacBook-Pro Assignment_10 %  
"""