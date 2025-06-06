""" 
    Write a program which contains one class named as Arithmetic.
    Arithmetic class contains two instance variables As Value1, Value2.
    Inside init method initialise all instance variables to 0
    There are three instance methods inside class Accept(), Addition(), Subtraction(),
    Multiplication(), Division().
    Accept method will accept of Value1 and Value2 from user.
    Addition() method will perform addition of Value1, Value2 and return result.
    Subtraction() method will perform subtraction of Value1, Value2 and return result.
    Multiplication() method will perform multiplication of Value1, Value2 and return result.
    Division() metjod will perform division of Value1, Value2 and return result
    After designing the above class call all instance methods by creating multiple objects.
"""
class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter first number: "))
        self.Value2 = float(input("Enter second number: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2
        
def main():
    obj1 = Arithmetic()
    obj1.Accept()
    print("Addition:", obj1.Addition())
    print("Subtraction:", obj1.Subtraction())
    print("Multiplication:", obj1.Multiplication())
    print("Division:", obj1.Division())

    print("-----------------------------------------")

    obj2 = Arithmetic()
    obj2.Accept()
    print("Addition:", obj2.Addition())
    print("Subtraction:", obj2.Subtraction())
    print("Multiplication:", obj2.Multiplication())
    print("Division:", obj2.Division())

if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_12 % python3 Assignment12_3.py
    Enter first number: 10
    Enter second number: 11
    Addition: 21.0
    Subtraction: -1.0
    Multiplication: 110.0
    Division: 0.9090909090909091
    -----------------------------------------
    Enter first number: 51
    Enter second number: 21
    Addition: 72.0
    Subtraction: 30.0
    Multiplication: 1071.0
    Division: 2.4285714285714284
    macbook@Macbooks-MacBook-Pro Assignment_12 % 
"""