""" 
    Write a program using a while loop to print numbers from 1 to 50.
    Expected output:
    1,2,3,4,5.....50
"""
def PrintNum(num1, num2):
    while num1 < num2:
        print(num1, end=",")
        num1 = num1 + 1
    print(num2)


def main():
    no1 = int(input("Enter the start number: "))
    no2 = int(input("Enter the end number: "))
    
    PrintNum(no1, no2) 
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_1.py
    Enter the start number: 1
    Enter the end number: 50
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_1.py
    Enter the start number: -5
    Enter the end number: 5
    -5,-4,-3,-2,-1,0,1,2,3,4,5
    macbook@Macbooks-MacBook-Pro Assignment_6 %
"""