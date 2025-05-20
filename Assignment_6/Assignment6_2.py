""" 
    Print Sum of Even numbers between 1 and 100. Use a loop to find and print the sum of all even numbers from 1 to 100.
    Expected output:
    Sum of even numbers between 1 to 100 is 2550.
"""
def SumEven(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(f"{i}",end=" ")
            sum = sum + i
    print()
    return sum

def main():
    no1 = int(input("Enter the start number: "))
    no2 = int(input("Enter the end number: "))
    
    ret = SumEven(no1, no2) 
    print(f"Sum of even numbers between {no1} to {no2} is {ret}.")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_2.py
    Enter the start number: 1
    Enter the end number: 100
    2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
    Sum of even numbers between 1 to 100 is 2550.
    macbook@Macbooks-MacBook-Pro Assignment_6 % python3 Assignment6_2.py
    Enter the start number: 250
    Enter the end number: 300
    250 252 254 256 258 260 262 264 266 268 270 272 274 276 278 280 282 284 286 288 290 292 294 296 298 300 
    Sum of even numbers between 250 to 300 is 7150.
    macbook@Macbooks-MacBook-Pro Assignment_6 % 
"""