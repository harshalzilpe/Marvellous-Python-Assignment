""" 
    Create a class BankAccount with account_number, name, and balance. 
    Use __init__ and create methods for deposit, withdraw, and displaying balance.
"""
class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")
        
def main():
    AcNumber = input("Enter account number: ")
    AcName = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))

    account = BankAccount(AcNumber, AcName, initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you for using the BankAccount system!")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_5.py
    Enter account number: 12345
    Enter account holder name: Harshal
    Enter initial balance: 500

    Choose an option:
    1. Deposit
    2. Withdraw
    3. Display Balance
    4. Exit
    Enter your choice (1-4): 1 
    Enter amount to deposit: 100
    100.0 deposited successfully.

    Choose an option:
    1. Deposit
    2. Withdraw
    3. Display Balance
    4. Exit
    Enter your choice (1-4): 3
    Account Number: 12345
    Account Holder: Harshal
    Current Balance: 600.0

    Choose an option:
    1. Deposit
    2. Withdraw
    3. Display Balance
    4. Exit
    Enter your choice (1-4): 2   
    Enter amount to withdraw: 200
    200.0 withdrawn successfully.

    Choose an option:
    1. Deposit
    2. Withdraw
    3. Display Balance
    4. Exit
    Enter your choice (1-4): 3   
    Account Number: 12345
    Account Holder: Harshal
    Current Balance: 400.0

    Choose an option:
    1. Deposit
    2. Withdraw
    3. Display Balance
    4. Exit
    Enter your choice (1-4): 4
    Thank you for using the BankAccount system!
    macbook@Macbooks-MacBook-Pro Assignment_14 %   
"""