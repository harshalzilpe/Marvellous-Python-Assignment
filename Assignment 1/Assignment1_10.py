""" 
    Write a program which accept name from user and display length of its name.
    Input: Marvellous   Output: 10
"""

def Length(str):
    count = len(str)
    return count

def main():
    print("Enter the String : ")
    string = input()
    
    Result = Length(string)
    
    print("The length of string is",Result)
    
if __name__ == "__main__":
    main() 

""" 
    macbook@192 Assignment % python3 Assignment1_10.py
    Enter the String : 
    Marvellous
    The length of string is 10
    macbook@192 Assignment % python3 Assignment1_10.py
    Enter the String : 
    Harshal Zilpe               // Blank space is also counted.
    The length of string is 13  
    macbook@192 Assignment % 
"""    