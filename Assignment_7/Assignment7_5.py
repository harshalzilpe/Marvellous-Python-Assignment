""" 
    Write a function that accepts a string and check whether it is a palindrone.
    Expected Input:
    Enter the string: radar
    Expected Output:
    radar is a palindrome.
"""
def ChkPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    string = input("Enter the string : ")
    
    convert = string.replace(" ", "").lower()
    
    if ChkPalindrome(convert):
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")
        
if __name__ == "__main__":
    main()
""" 
    macbook@192 Assignment_7 % python3 Assignment7_5.py
    Enter the string : radar
    radar is a palindrome.
    macbook@192 Assignment_7 % python3 Assignment7_5.py
    Enter the string : name
    name is not a palindrome.
    macbook@192 Assignment_7 % python3 Assignment7_5.py
    Enter the string : RaceCar        
    RaceCar is a palindrome.
    macbook@192 Assignment_7 % 
"""