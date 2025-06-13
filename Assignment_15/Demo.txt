""" 
    Write a program which accepts file name from user and create new file named as Demo.txt and 
    copy all contents from existing file into new file. Accept file name through command line arguments.
    Input: ABC.txt
    Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
""" 
import sys

def copy_file(source_file, destination_file="Demo.txt"):
    try:
        src = open(source_file, 'r')
        data = src.read()
        src.close()

        dest = open(destination_file, 'w')
        dest.write(data)
        dest.close()

        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
   
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_filename>")
    else:
        source_filename = sys.argv[1]
        copy_file(source_filename)
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_15 % python3 Assignment15_3.py
    Usage: python script.py <source_filename>
    macbook@192 Assignment_15 % python3 Assignment15_3.py Demo.txt
    Error: The file 'Demo.txt' was not found.
    macbook@192 Assignment_15 % python3 Assignment15_3.py Assignment15_3.py
    Contents copied from Assignment15_3.py to Demo.txt successfully.
    macbook@192 Assignment_15 % 
"""