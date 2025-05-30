""" 
    Design python application which contains two threads named as thread1 and thread2.
    Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse oredr on
    screen. After execution of thread1 gets completed then schedule thread2.
"""
import threading

def thread1(no):
    for i in range(1, no + 1):
        print(f"Thread1: {i}")
    print("---End of Thread1---")
    print()

def thread2(no):
    for i in range(no, 0, -1):
        print(f"Thread2: {i}")
    print("---End of Thread2---")

def main():
    
    n = int(input("Enter a number: "))

    t1 = threading.Thread(target=thread1, args=(n,))
    t2 = threading.Thread(target=thread2, args=(n,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_8 % python3 Assignment8_5.py
    Enter a number: 10
    Thread1: 1
    Thread1: 2
    Thread1: 3
    Thread1: 4
    Thread1: 5
    Thread1: 6
    Thread1: 7
    Thread1: 8
    Thread1: 9
    Thread1: 10
    ---End of Thread1---

    Thread2: 10
    Thread2: 9
    Thread2: 8
    Thread2: 7
    Thread2: 6
    Thread2: 5
    Thread2: 4
    Thread2: 3
    Thread2: 2
    Thread2: 1
    ---End of Thread2---
    macbook@Macbooks-MacBook-Pro Assignment_8 % 
"""