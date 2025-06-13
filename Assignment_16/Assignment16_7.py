""" 
    Create a file marks.txt with student name and marks, Then read the file and 
    display students who scored more than 75 marks.
"""  
def main():
    file = open("marks.txt", "w")

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = input(f"Enter marks of {name}: ")
        file.write(name + " " + marks + "\n")

    file.close()

    file = open("marks.txt", "r")

    print("\nStudents scoring more than 75 marks:")
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            name = parts[0]
            marks = int(parts[1])
            if marks > 75:
                print(name)

    file.close()
        
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_16 % python3 Assignment16_7.py
    Enter number of students: 5
    Enter name of student 1: Harshal
    Enter marks of Harshal: 90
    Enter name of student 2: Piyush
    Enter marks of Piyush: 75
    Enter name of student 3: Devendra
    Enter marks of Devendra: 70
    Enter name of student 4: Karan
    Enter marks of Karan: 80
    Enter name of student 5: Devashish
    Enter marks of Devashish: 98

    Students scoring more than 75 marks:
    Harshal
    Karan
    Devashish
    macbook@192 Assignment_16 % 
"""