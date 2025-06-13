""" 
    Accept 10 number from the user and write them into a file named numbers.txt, each on new line.
"""  
def main():
    file = open("numbers.txt", "w")

    for i in range(10):
        number = input(f"Enter number {i + 1}: ")
        file.write(number + "\n")  

    file.close()

    print("All numbers have been written to numbers.txt")
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_4.py
    Enter number 1: 10
    Enter number 2: 11
    Enter number 3: 21
    Enter number 4: 51
    Enter number 5: 101
    Enter number 6: 111
    Enter number 7: 121
    Enter number 8: 151
    Enter number 9: 201
    Enter number 10: 211
    All numbers have been written to numbers.txt
    macbook@192 Assignment_16 % 
"""