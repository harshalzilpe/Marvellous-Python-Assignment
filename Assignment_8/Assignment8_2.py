""" 
    Design python application which creates two thread named as evenfactor and oddfactor.
    Both the thread accept one parameter as integer. Evenfactor thread will display addition
    of even factors of given numbers and oddfactor will display addition of odd
    factors of given numbers. After execution of both the thread gets completed main thread should display message as "exit from main"
"""
import threading

class EvenFactor(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        sum_even = 0
        for i in range(1, self.number + 1):
            if self.number % i == 0 and i % 2 == 0:
                sum_even += i
                print(i)
        print(f"Sum of even factors of {self.number}: {sum_even}")

class OddFactor(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        sum_odd = 0
        for i in range(1, self.number + 1):
            if self.number % i == 0 and i % 2 != 0:
                sum_odd += i
                print(i)
        print(f"Sum of odd factors of {self.number}: {sum_odd}")

def main():
    number = int(input("Enter a number: "))

    even_thread = EvenFactor(number)
    odd_thread = OddFactor(number)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("exit from main")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_8 % python3 Assignment8_2.py
    Enter a number: 20
    2
    4
    10
    20
    Sum of even factors of 20: 36
    1
    5
    Sum of odd factors of 20: 6
    exit from main
    macbook@Macbooks-MacBook-Pro Assignment_8 % 
"""