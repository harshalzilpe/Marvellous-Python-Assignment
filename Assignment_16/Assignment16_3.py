""" 
    Write a python script to count the number of lines, words, and characters in a given file.
"""  
def main():
    filename = input("Enter the filename: ")

    file = open(filename, "r")

    lines = file.readlines()
    file.close()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        word_count += len(line.split())
        char_count += len(line)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_3.py
    Enter the filename: Student.txt
    Lines: 5
    Words: 5
    Characters: 40
    macbook@192 Assignment_16 %  
"""