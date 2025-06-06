""" 
    Write a program which contains one class named as BankAccount.
    BankAccount class contains two instance variables as Name & Amount.
    That class contains one class variable as ROI which is initialise to 10.5.
    Inside init method initialise all name and amount variables by accepting the values from user.
    There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
    Deposit() method will accept the amount from user and add that value in class instance variable Amount.
    Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
    CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
    And Display() method will display value of all the instance variables as Name and Amount. 
    After designing the above class call all instance methods by creating multiple objects.
"""
class BankAccount:
    ROI = 10.5  

    def __init__(self):
        self.Name = input("Enter account holder's name: ")
        self.Amount = float(input("Enter initial amount: "))

    def Display(self):
        print(f"\nAccount Holder Name: {self.Name}")
        print(f"Current Balance: ₹{self.Amount:.2f}")

    def Deposit(self):
        deposit_amt = float(input(f"{self.Name}, enter amount to deposit: "))
        self.Amount += deposit_amt
        print(f"₹{deposit_amt:.2f} deposited successfully.")

    def Withdraw(self):
        withdraw_amt = float(input(f"{self.Name}, enter amount to withdraw: "))
        if withdraw_amt <= self.Amount:
            self.Amount -= withdraw_amt
            print(f"₹{withdraw_amt:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Calculated Interest (@{BankAccount.ROI}%): ₹{interest:.2f}")
        return interest
        
def main():
    print("Create first account:")
    acc1 = BankAccount()
    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    acc1.CalculateInterest()
    acc1.Display()

    print("\nCreate second account:")
    acc2 = BankAccount()
    acc2.Deposit()
    acc2.Withdraw()
    acc2.CalculateInterest()
    acc2.Display()

if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_13 % python3 Assignment13_2.py
    Create first account:
    Enter account holder's name: Harshal
    Enter initial amount: 2000

    Account Holder Name: Harshal
    Current Balance: ₹2000.00
    Harshal, enter amount to deposit: 1000
    ₹1000.00 deposited successfully.
    Harshal, enter amount to withdraw: 500
    ₹500.00 withdrawn successfully.
    Calculated Interest (@10.5%): ₹262.50

    Account Holder Name: Harshal
    Current Balance: ₹2500.00

    Create second account:
    Enter account holder's name: Piyush
    Enter initial amount: 500
    Piyush, enter amount to deposit: 10000000
    ₹10000000.00 deposited successfully.
    Piyush, enter amount to withdraw: 50
    ₹50.00 withdrawn successfully.
    Calculated Interest (@10.5%): ₹1050047.25

    Account Holder Name: Piyush
    Current Balance: ₹10000450.00
    macbook@Macbooks-MacBook-Pro Assignment_13 % 
"""