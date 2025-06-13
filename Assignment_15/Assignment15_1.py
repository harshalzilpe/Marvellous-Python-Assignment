""" 
    Write a program which accepts file name from user and check whether that file exists in current directory or not.
    Input: Demo.txt
    Check whether Demo.txt exists or not.
""" 
import os
       
def main():
    filename = input("Enter the file name: ")

    if os.path.isfile(filename):
        print(f"The file '{filename}' exists in the current directory.")
    else:
        print(f"The file '{filename}' does NOT exist in the current directory.")
    
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_15 % python3 Assignment15_1.py 
    Enter the file name: Demo.txt
    The file 'Demo.txt' does NOT exist in the current directory.
    macbook@192 Assignment_15 % python3 Assignment15_1.py
    Enter the file name: Assignment15_1.py
    The file 'Assignment15_1.py' exists in the current directory.
    macbook@192 Assignment_15 % 
"""