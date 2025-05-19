""" 
    Area and Perimeter of Rectangle
    Accept the length and width of a rectangle. Calculate and display the area and perimeter.
    Input:
    Enter length: 5
    Enter width: 3
    Output:
    Area: 15
    Perimeter: 16
"""
def Area(num1, num2):
    A = num1 * num2
    return A

def Perimeter(num1, num2):
    P = 2 * (num1 + num2)
    return P

def main():
    no1 = float(input("Enter length: "))
    no2 = float(input("Enter width: "))
    
    ret1 = Area(no1, no2)
    print(f"Area of Rectangle is {ret1}.")
    
    ret2 = Perimeter(no1, no2)
    print(f"Pemimeter of Rectangle is {ret2}.")
    
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_7.py
    Enter length: 5
    Enter width: 3
    Area of Rectangle is 15.0.
    Pemimeter of Rectangle is 16.0.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_7.py
    Enter length: 10.11            
    Enter width: 21.51
    Area of Rectangle is 217.4661.
    Pemimeter of Rectangle is 63.24.
    macbook@Macbooks-MacBook-Pro Assignment_5 %   
"""