""" 
    Write a program to read a file line by line and display only those line that contains more than 5 words.
"""  
def main():
    filename = input("Enter the filename: ")

    file = open(filename, "r")  

    for line in file:
        words = line.strip().split()
        if len(words) > 5:
            print(line.strip())

    file.close()
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_5.py
    Enter the filename: Assignment16_5.py
    Write a program to read a file line by line and display only those line that contains more than 5 words.
    filename = input("Enter the filename: ")
    macbook@192 Assignment_16 % 
"""