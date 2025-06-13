""" 
    Write a program which accepts file name from user and open that file and display the contents of that file on screen.
    Input: Demo.txt
    Display contents of Demo.txt on console
""" 
import os
       
def main():
    filename = input("Enter the file name: ")

    if os.path.isfile(filename):
        file = open(filename, 'r')
    
        contents = file.read()
        
        print("\n--- File Contents ---\n")
        print(contents)
        
        file.close()
    else:
        print(f"The file '{filename}' does NOT exist in the current directory.")
    
    
if __name__ == "__main__":
    main()

"""  
macbook@192 Assignment_15 % python3 Assignment15_2.py
Enter the file name: Demo.txt
The file 'Demo.txt' does NOT exist in the current directory.
macbook@192 Assignment_15 % python3 Assignment15_2.py
Enter the file name: Assignment15_2.py

--- File Contents ---

Write a program which accepts file name from user and open that file and display the contents of that file on screen.
Input: Demo.txt
Display contents of Demo.txt on console

import os
       
def main():
    filename = input("Enter the file name: ")

    if os.path.isfile(filename):
        file = open(filename, 'r')
    
        contents = file.read()
        
        print("\n--- File Contents ---\n")
        print(contents)
        
        file.close()
    else:
        print(f"The file '{filename}' does NOT exist in the current directory.")
    
    
if __name__ == "__main__":
    main()

macbook@192 Assignment_15 % 
"""