""" 
    Create a class Student with name, roll_no, and a class variable school_name. 
    Print student details and school name. Change the school name using class name.
"""
class Student:
    school_name = "CD High School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"School Name: {Student.school_name}")
        
def main():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = Student(name, roll_no)

    print("\nStudent Details before changing school name:")
    student.display()

    Student.school_name = "VB High School"

    print("\nStudent Details after changing school name:")
    student.display()
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_4.py
    Enter student name: Harshal
    Enter roll number: 21

    Student Details before changing school name:
    Name: Harshal
    Roll No: 21
    School Name: ABC High School

    Student Details after changing school name:
    Name: Harshal
    Roll No: 21
    School Name: VB High School
    macbook@Macbooks-MacBook-Pro Assignment_14 %  
"""