""" 
    Write a program which contains one class named as Numbers.
    Arithmetic class contains one instance variables as Value.
    Inside init method initialise that instance variables to the value which is accepted from user.
    There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
    ChkPrime() method will returns true if number is prime otherwise return false.
    ChkPerfect() method will returns true if number is perfect otherwise return false.
    Factors() method will display all factors of instance variable.
    SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
    After designing the above class call all instance methods by creating multiple objects.
"""
class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        print(f"Factors of {self.Value} are:", end=' ')
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=' ')
        print()
        
def main():
    value = [6, 28, 11, 10] 
    for val in value:
        print(f"\n--- For number: {val} ---")
        obj = Numbers(val)
        obj.Factors()
        print("Sum of factors:", obj.SumFactors())
        print("Is Prime?:", obj.ChkPrime())
        print("Is Perfect?:", obj.ChkPerfect())

if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_13 % python3 Assignment13_3.py

    --- For number: 6 ---
    Factors of 6 are: 1 2 3 6 
    Sum of factors: 6
    Is Prime?: False
    Is Perfect?: True

    --- For number: 28 ---
    Factors of 28 are: 1 2 4 7 14 28 
    Sum of factors: 28
    Is Prime?: False
    Is Perfect?: True

    --- For number: 11 ---
    Factors of 11 are: 1 11 
    Sum of factors: 1
    Is Prime?: True
    Is Perfect?: False

    --- For number: 10 ---
    Factors of 10 are: 1 2 5 10 
    Sum of factors: 8
    Is Prime?: False
    Is Perfect?: False
    macbook@Macbooks-MacBook-Pro Assignment_13 % 
"""