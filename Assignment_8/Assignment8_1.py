""" 
    Design python application which creates two thread named as even and odd.
    Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
"""
import threading

def print_even():
    print("Even Thread Started")
    for i in range(2, 21, 2):  
        print(f"Even: {i}")

def print_odd():
    print("Odd Thread Started")
    for i in range(1, 20, 2):  
        print(f"Odd: {i}")

def main():
    even_thread = threading.Thread(target=print_even, name="Even")
    odd_thread = threading.Thread(target=print_odd, name="Odd")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Main Thread Finished")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_8 % python3 Assignment8_1.py
    Even Thread Started
    Even: 2
    Even: 4
    Even: 6
    Even: 8
    Even: 10
    Even: 12
    Even: 14
    Even: 16
    Even: 18
    Even: 20
    Odd Thread Started
    Odd: 1
    Odd: 3
    Odd: 5
    Odd: 7
    Odd: 9
    Odd: 11
    Odd: 13
    Odd: 15
    Odd: 17
    Odd: 19
    Main Thread Finished
    macbook@Macbooks-MacBook-Pro Assignment_8 %  
"""