""" 
    Vowels or Consonant Check
    Accept single character from the user and check if it is vowels (a, e, i, o, u). If not,
    print it's a consonant.
    Input:
    Enter a character: e
    Output:
    'e' is a vowel.
"""
def ChkVowels(ch1):
    if ch1 in "aeiou":
        print(f"{ch1} is a vowel.")
    else:
        print(f"{ch1} is a consonant.")

def main():
    char = input("Enter the character: ")
    
    ChkVowels(char)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_2.py
    Enter the character: a
    a is a vowel.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_2.py 
    Enter the character: e
    e is a vowel.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_2.py
    Enter the character: i
    i is a vowel.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_2.py
    Enter the character: o
    o is a vowel.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_2.py
    Enter the character: u
    u is a vowel.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_2.py
    Enter the character: v
    v is a consonant.
    macbook@Macbooks-MacBook-Pro Assignment_5 % 
"""