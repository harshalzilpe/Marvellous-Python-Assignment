""" 
    Write a program which contains one class named as Circle.
    Circle class contains three instance variables As Radius, Area, Circumference.
    That class contains one class variable as PI which is intialise to 3.14
    Inside init method initialise all instance variables to 0.0
    There are three instance methods inside class Accept(), CalculateArea(),
    CalculateCircumference(), Display().
    Accept method will accept value of Radius from user.
    CalculateArea() method will calculate area of circle and store it into instance variable Area.
    CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
    And Display() method awill display value of all the instance variables as Radius, Area, Circumference.
    After designing the above class call all instance methods by creating multiple objects.
"""
class Circle:
    PI = 3.14 

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius of Circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")


def main():
    circle1 = Circle()
    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    circle1.Display()

    circle2 = Circle()
    circle2.Accept()
    circle2.CalculateArea()
    circle2.CalculateCircumference()
    circle2.Display()


if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_12 % python3 Assignment12_2.py
    Enter Radius of Circle: 5
    Radius: 5.0
    Area: 78.5
    Circumference: 31.400000000000002
    Enter Radius of Circle: 8
    Radius: 8.0
    Area: 200.96
    Circumference: 50.24
    macbook@Macbooks-MacBook-Pro Assignment_12 %   
"""