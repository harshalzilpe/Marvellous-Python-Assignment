""" 
    Write a python program using multiprocessing.Pool to compute factorial of numbers in a list.
"""
import multiprocessing

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    
def main():
    Num = input("Enter numbers: ")
    numbers = list(map(int, Num.strip().split()))

    pool = multiprocessing.Pool()
    results = pool.map(factorial, numbers)
    
    pool.close()
    pool.join()

    for num, fact in zip(numbers, results):
        print(f"Factorial of {num} is {fact}")


if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_9 % python3 Assignment9_3.py
    Enter numbers separated by space: 1 2 3 4 5 6 7
    Factorial of 1 is 1
    Factorial of 2 is 2
    Factorial of 3 is 6
    Factorial of 4 is 24
    Factorial of 5 is 120
    Factorial of 6 is 720
    Factorial of 7 is 5040
    macbook@Macbooks-MacBook-Pro Assignment_9 %  
"""