""" 
    Accept a list of numbers and use the reduce() (from functools) to find the product of all numbers.
    Expected Input:
    Enter the list: 2 3 4
    Expected Output:
    product : 24
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
    
    RData = reduce(lambda No1, No2 : No1 * No2, Data)
    print("Product : ",RData)
    
if __name__ == "__main__":
    main()
""" 
    macbook@192 Assignment_7 % python3 Assignment7_4.py
    Enter number of elements : 
    4
    Please enter numeric values : 
    1
    2
    3
    4
    Input Data :  [1, 2, 3, 4]
    Product :  24
    macbook@192 Assignment_7 % python3 Assignment7_4.py
    Enter number of elements : 
    3
    Please enter numeric values : 
    2
    3
    4
    Input Data :  [2, 3, 4]
    Product :  24
    macbook@192 Assignment_7 %  
"""