""" 
    Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers.
    List contains the numbers which are accepted from user. Filter should filter out all such numbers which even. Map function 
    will calculate its square. Reduce will return addition of all that numbers.
    Input List: [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    List after filter = [2, 4, 4, 2, 8, 10]
    List after map = [4, 16, 16, 4, 64, 100]
    Output of reduce = 204
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

    FData = list(filter(lambda No : No % 2 == 0, Data))
    print("List after filter : ",FData)

    MData = list(map(lambda No : No * No, FData))
    print("List after Map : ",MData)

    RData = reduce(lambda A,B : A + B, MData)
    print("List after Reduce : ",RData)

if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_10 % python3 Assignment10_4.py
    Enter number of elements : 
    10
    Please enter numeric values : 
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
    Input Data :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    List after filter :  [2, 4, 4, 2, 8, 10]
    List after Map :  [4, 16, 16, 4, 64, 100]
    List after Reduce :  204
    macbook@Macbooks-MacBook-Pro Assignment_10 % 
"""