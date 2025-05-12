""" 
    Write a program which display 5 times Marvellous on screen.
    Output:
        Marvellous
        Marvellous
        Marvellous
        Marvellous
        Marvellous
"""

def Iteration(no):
    
    for no in range(no):
        print("Marvellous")

def main():
    print("Enter the number : ")
    value = int(input())
    
    Iteration(value)
    
if __name__ == "__main__":
    main() 
    
""" 
    macbook@192 Assignment % python3 Assignment1_4.py
    Enter the number : 
    5
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    macbook@192 Assignment % python3 Assignment1_4.py
    Enter the number : 
    2
    Marvellous
    Marvellous
    macbook@192 Assignment % python3 Assignment1_4.py
    Enter the number : 
    9
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    macbook@192 Assignment % 
"""