""" 
    Write a program which accepts two file names from user and compare contents of both the files.
    If both files contains same contents then display success otherwise display failure. Accept names
    of both the files from command line.
    Input: Demo.txt     Hello.txt
    Compare contents of Demo.txt and Hello.txt
""" 
import sys

def compare_files(file1, file2):
    try:
        f1 = open(file1, 'r')
        f2 = open(file2, 'r')

        content1 = f1.read()
        content2 = f2.read()

        f1.close()
        f2.close()

        if content1 == content2:
            print("Success: Both files have the same contents.")
        else:
            print("Failure: Files have different contents.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
   
def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        compare_files(file1, file2)
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_15 % python3 Assignment15_4.py                   
    Usage: python compare_files.py <file1> <file2>
    macbook@192 Assignment_15 % python3 Assignment15_4.py Demo.txt Hello.txt
    Error: [Errno 2] No such file or directory: 'Hello.txt'
    macbook@192 Assignment_15 % python3 Assignment15_4.py Demo.txt Assignment15_3.py
    Success: Both files have the same contents.
    macbook@192 Assignment_15 % python3 Assignment15_4.py Assignment15_4.py Assignment15_3.py
    Failure: Files have different contents.
    macbook@192 Assignment_15 % 
"""