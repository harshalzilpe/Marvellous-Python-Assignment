""" 
    Write a program which contains one class named as Demo.
    Demo class contains two instance variables as no1, no2.
    That class contains one class variable as Value.
    There are two instance methods of class as Fun and Gun which displays values of instance variables.
    Initialise instance variable in init method by accepting the values from user.
    After creating the class create the two objects of Demo class as
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)
    
    Now call the instance methods as
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()
"""
class Demo:
    Value = 0

    def __init__(self, no1, no2):
        self.no1 = no1  # instance variable
        self.no2 = no2  # instance variable

    def Fun(self):
        print("Inside Fun:")
        print("no1 =", self.no1)
        print("no2 =", self.no2)

    def Gun(self):
        print("Inside Gun:")
        print("no1 =", self.no1)
        print("no2 =", self.no2)

def main():
    
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()
    
if __name__ == "__main__":
    main()
"""  
    macbook@Macbooks-MacBook-Pro Assignment_12 % python3 Assignment12_1.py
    Inside Fun:
    no1 = 11
    no2 = 21
    Inside Fun:
    no1 = 51
    no2 = 101
    Inside Gun:
    no1 = 11
    no2 = 21
    Inside Gun:
    no1 = 51
    no2 = 101
    macbook@Macbooks-MacBook-Pro Assignment_12 % 
"""