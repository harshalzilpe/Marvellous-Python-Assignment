""" 
    Create a base class Person with name and age. Derive a class Teacher with subject and salary. 
    Use super() to call base class constructor and print both.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age) 
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display() 
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")
        
def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    subject = input("Enter subject: ")
    salary = float(input("Enter salary: "))

    teacher = Teacher(name, age, subject, salary)
    print("\n--- Teacher Details ---")
    teacher.display()
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_7.py
    Enter name: Harshal
    Enter age: 25
    Enter subject: CS
    Enter salary: 50000

    --- Teacher Details ---
    Name: Harshal
    Age: 25
    Subject: CS
    Salary: 50000.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""