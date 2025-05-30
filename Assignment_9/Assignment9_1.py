""" 
    Create a python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use threading.Thread.
"""
import threading
import time

def printNum(thread_name):
    for i in range(1, 6):
        print(f"{thread_name}: {i}")
        time.sleep(1)

def main():
    thread1 = threading.Thread(target=printNum, args=("Thread-1",))
    thread2 = threading.Thread(target=printNum, args=("Thread-2",))
    thread3 = threading.Thread(target=printNum, args=("Thread-3",))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("All threads have finished.")

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_9 % python3 Assignment9_1.py
    Thread-1: 1
    Thread-2: 1
    Thread-3: 1
    Thread-1: 2
    Thread-2: 2
    Thread-3: 2
    Thread-1: 3
    Thread-2: 3
    Thread-3: 3
    Thread-1: 4
    Thread-2: 4
    Thread-3: 4
    Thread-1: 5
    Thread-2: 5
    Thread-3: 5
    All threads have finished.
    macbook@Macbooks-MacBook-Pro Assignment_9 % 
"""