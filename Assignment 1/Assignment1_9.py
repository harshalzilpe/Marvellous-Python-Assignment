""" 
    Write a program which display first 10 even numbers on screen.
    Output: 2 4 6 8 10 12 14 16 18 20
"""

def DisplayEven(no):
    
    for no in range(2,no+1,2):
        print(no, end=" ")

def main():
    
    DisplayEven(20)
    
if __name__ == "__main__":
    main() 

""" 

"""