""" 
    Create a class Employee with attributes name, emp_id, and salary. Create objects 
    of this class and print their details using a method..

    Expected Output:
    Name: Rohit, ID: 101, Salary: 50000
"""
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")
        
def main():
    name = input("Enter employee name: ")
    emp_id = int(input("Enter employee ID: "))
    salary = float(input("Enter employee salary: "))

    emp = Employee(name, emp_id, salary)

    emp.display_details()
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_1.py
    Enter employee name: Rohit
    Enter employee ID: 101
    Enter employee salary: 50000
    Name: Rohit, ID: 101, Salary: 50000.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""