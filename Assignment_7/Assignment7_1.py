""" 
    Write two lambda functions:
    • One to calculate square of a number
    • Another to calculate cube of a number
    Expected Input:
    Enter the number: 3
    Expected Output:
    Square: 9
    Cube: 27
"""
def main():
    no = int(input("Enter the number : "))
    
    Square = lambda no1 : no1*no1
    print("Square : ",Square(no))
    
    Cube = lambda no1 : no1*no1*no1
    print("Cube : ",Cube(no))
if __name__ == "__main__":
    main()
""" 
    macbook@192 Assignment_7 % python3 Assignment7_1.py
    Enter the number : 3
    Square :  9
    Cube :  27
    macbook@192 Assignment_7 % python3 Assignment7_1.py
    Enter the number : 9
    Square :  81
    Cube :  729
    macbook@192 Assignment_7 % 
"""