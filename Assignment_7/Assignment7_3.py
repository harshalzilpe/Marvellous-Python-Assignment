""" 
    Accept a list of numbers and use the filter() function to keep only even numbers.
    Expected Input:
    Enter the list: 1 2 3 4 5 6
    Expected Output:
    Doubled list : [2, 4, 6]
"""
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
    print("Even numbers : ",FData)
    
if __name__ == "__main__":
    main()
""" 
    macbook@192 Assignment_7 % python3 Assignment7_3.py
    Enter number of elements : 
    6
    Please enter numeric values : 
    1
    2
    3
    4
    5
    6
    Input Data :  [1, 2, 3, 4, 5, 6]
    Even numbers :  [2, 4, 6]
    macbook@192 Assignment_7 % 
"""