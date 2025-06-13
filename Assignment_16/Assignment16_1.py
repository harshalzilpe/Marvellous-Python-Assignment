""" 
    Write a python program to create a text file named student.txt and write the names of 5 students into it.
"""    
def main():
    file = open("student.txt", "w")

    for i in range(5):
        name = input(f"Enter name of student {i + 1}: ")
        file.write(name + "\n")

    file.close()

    print("Student names written to student.txt successfully.")
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_1.py
    Enter name of student 1: Harshal
    Enter name of student 2: Piyush
    Enter name of student 3: Devendra
    Enter name of student 4: Karan
    Enter name of student 5: Devashish
    Student names written to student.txt successfully.
    macbook@192 Assignment_16 % 
"""