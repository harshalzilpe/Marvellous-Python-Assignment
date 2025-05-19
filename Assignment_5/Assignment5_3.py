""" 
    Voting Eligibility Checker
    Accept age from the user and check whether the person is eligible to vote.
    (Age should be 18 or above).
    Input:
    Enter your age: 19
    Output:
    Eligible to vote.
"""
def ChkEligibility(no):
    if no >= 18:
        print("Your are eligible to vote.")
    else:
        print("Your are not eligible to vote.")

def main():
    age = int(input("Enter your age: "))
    
    ChkEligibility(age)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_3.py
    Enter your age: 18
    Your are eligible to vote.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_3.py
    Enter your age: 19
    Your are eligible to vote.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_3.py
    Enter your age: 17
    Your are not eligible to vote.
    macbook@Macbooks-MacBook-Pro Assignment_5 % 
"""