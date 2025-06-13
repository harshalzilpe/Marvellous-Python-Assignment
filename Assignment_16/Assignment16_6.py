""" 
    Write a python program to copy contents of one file (source.txt) into another file (destination.txt).
"""  
def main():
    source_file = input("Enter source file name : ")
    destination_file = input("Enter destination file name : ")

    source = open(source_file, 'r')

    content = source.read()

    source.close()

    destination = open(destination_file, 'w')

    destination.write(content)

    destination.close()

    print("File copied successfully.")
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_6.py
    Enter source file name : Student.txt
    Enter destination file name : Destination.txt
    File copied successfully.
    macbook@192 Assignment_16 % 
"""