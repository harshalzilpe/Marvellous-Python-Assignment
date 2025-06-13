""" 
    Accepts file name from user and one string from user and return the frequency of that string from file.
    Input: Demo.txt     Marvellous
    Search "Marvellous" in Demo.txt
""" 
def cnt_string(filename, search_string):
    try:
        file = open(filename, 'r')    
        content = file.read()             
        file.close()                   
        count = content.count(search_string)  
        return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
   
def main():
    filename = input("Enter filename: ")   
    search_string = input("Enter string to search: ")  

    frequency = cnt_string(filename, search_string)

    if frequency is not None:
        print(f"The string '{search_string}' appears {frequency} times in '{filename}'.")
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_15 % python3 Assignment15_5.py                   
    Enter filename: Demo.txt
    Enter string to search: Marvellous
    The string 'Marvellous' appears 0 times in 'Demo.txt'.
    macbook@192 Assignment_15 % python3 Assignment15_5.py
    Enter filename: Demo.txt
    Enter string to search: main
    The string 'main' appears 3 times in 'Demo.txt'.
    macbook@192 Assignment_15 % 
"""