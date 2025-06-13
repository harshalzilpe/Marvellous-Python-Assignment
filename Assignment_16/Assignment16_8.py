""" 
    Write a script to remove all blank lines from a file. Save the cleaned output to a new file.
"""  
def main():
    ip_file_name = input("Enter the name of the input file: ")
    op_file_name = input("Enter the name of the output file: ")

    input_file = open(ip_file_name, "r")
    lines = input_file.readlines()
    input_file.close()

    output_file = open(op_file_name, "w")

    for line in lines:
        if line.strip() != " ":
            output_file.write(line)

    output_file.close()

    print("Blank lines removed. Output saved to:", op_file_name)
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_8.py
    Enter the name of the input file: Assignment16_8.py
    Enter the name of the output file: Output.txt
    Blank lines removed. Output saved to: Output.txt
    macbook@192 Assignment_16 % 
"""