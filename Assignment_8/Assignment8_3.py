""" 
    Design python application which creates two thread named as evenlist and oddlist.
    Both the thread accept list of integers as parameter. Evenlist thread add all even
    elements from input list and display the addition. Oddlist thread add all off
    elements from input list and display the addition
"""
import threading

def evenlist(num):
    even_sum = 0
    for num in num:
        if num % 2 == 0:
            even_sum += num
            print(num)
    print(f"Sum of even numbers: {even_sum}")

def oddlist(num):
    odd_sum = 0
    for num in num:
        if num % 2 != 0:
            odd_sum += num
            print(num)
    print(f"Sum of odd numbers: {odd_sum}")

def main():
    
    no = list(map(int, input("Enter numbers: ").split()))

    even_thread = threading.Thread(target=evenlist, args=(no,), name="evenlist")
    odd_thread = threading.Thread(target=oddlist, args=(no,), name="oddlist")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads have completed execution.")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_8 % python3 Assignment8_3.py
    Enter numbers: 1 2 3 4 5 6 7 8 9 10
    2
    4
    6
    8
    10
    Sum of even numbers: 30
    1
    3
    5
    7
    9
    Sum of odd numbers: 25
    Both threads have completed execution.
    macbook@Macbooks-MacBook-Pro Assignment_8 %  
"""