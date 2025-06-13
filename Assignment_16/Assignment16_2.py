""" 
    Write a python program to read and display the contents of a file data.txt.
"""    
import os

def main():
    file_name = input("Enter the file name: ")

    if os.path.exists(file_name):
        file = open(file_name, 'r')      
        content = file.read()           
        print("\nFile Contents:\n")
        print(content)                   
        file.close()                    
    else:
        print("Error: The file does not exist.")
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_2.py
    Enter the file name: Data.txt
    Error: The file does not exist.
    macbook@192 Assignment_16 % python3 Assignment16_2.py
    Enter the file name: Student.txt

    File Contents:

    Harshal
    Piyush
    Devendra
    Karan
    Devashish

    macbook@192 Assignment_16 % 
"""