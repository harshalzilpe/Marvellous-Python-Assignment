""" 
    Accept a list of integers from the user and use the map() function to double each value.
    Expected Input:
    Enter the list: 1 2 3 4 5
    Expected Output:
    Doubled list : [2, 4, 6, 8, 10]
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
    
    MData = list(map(lambda No : No * 2, Data))
    print("Doubled list : ",MData)
    
if __name__ == "__main__":
    main()
""" 
    macbook@192 Assignment_7 % python3 Assignment7_2.py
    Enter number of elements : 
    5
    Please enter numeric values : 
    1
    2
    3
    4
    5
    Input Data :  [1, 2, 3, 4, 5]
    Doubled list :  [2, 4, 6, 8, 10]
    macbook@192 Assignment_7 %
"""