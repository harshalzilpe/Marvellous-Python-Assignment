""" 
    Demonstrate private, protected and public access modifiers using a class Employee with attributes: __salary, __department, name.
"""
class Employee:
    def __init__(self, name, department, salary):
        self.name = name              
        self._department = department  
        self.__salary = salary         

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")
        
def main():
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    emp = Employee(name, department, salary)

    print(f"\nAccessing public attribute: {emp.name}")

    print(f"Accessing protected attribute: {emp._department}")

    print(f"Accessing private attribute via method: {emp.get_salary()}")

    print("\n--- Employee Details ---")
    emp.display_info()
    
if __name__ == "__main__":
    main()

"""  
    Enter employee name: Harshal
    Enter department: IT
    Enter salary: 50000

    Accessing public attribute: Harshal
    Accessing protected attribute: IT
    Accessing private attribute via method: 50000.0

    --- Employee Details ---
    Name: Harshal
    Department: IT
    Salary: 50000.0
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""