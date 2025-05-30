""" 
    Create a python program thst compare execution time of summing numbers from 1 to 10 million using normal function, threading, and multiprocessing.
"""

import time
import threading
import multiprocessing

def normal_sum(N):
    return sum(range(1, N + 1))

def partial_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))

def threading_sum(N):
    threads = []
    results = [0] * 4  # 4 threads
    step = N // 4
    for i in range(4):
        start = i * step + 1
        end = (i + 1) * step if i < 3 else N
        t = threading.Thread(target=partial_sum, args=(start, end, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return sum(results)

def multiprocessing_sum_worker(start, end, queue):
    queue.put(sum(range(start, end + 1)))

def multiprocessing_sum(N):
    processes = []
    queue = multiprocessing.Queue()
    step = N // 4
    for i in range(4):
        start = i * step + 1
        end = (i + 1) * step if i < 3 else N
        p = multiprocessing.Process(target=multiprocessing_sum_worker, args=(start, end, queue))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    result = 0
    while not queue.empty():
        result += queue.get()
    return result

def measure_time(func, N):
    start_time = time.time()
    result = func(N)
    end_time = time.time()
    return result, end_time - start_time

def main():
    N = int(input("Enter the upper limit number to sum up to: "))

    print(f"\nCalculating sum from 1 to {N}\n")

    result_normal, time_normal = measure_time(normal_sum, N)
    print(f"Normal sum: {result_normal}, Time taken: {time_normal:.4f} seconds")

    result_thread, time_thread = measure_time(threading_sum, N)
    print(f"Threading sum: {result_thread}, Time taken: {time_thread:.4f} seconds")

    result_multi, time_multi = measure_time(multiprocessing_sum, N)
    print(f"Multiprocessing sum: {result_multi}, Time taken: {time_multi:.4f} seconds")

    
if __name__ == "__main__":
    main()

""" 
    macbook@Macbooks-MacBook-Pro Assignment_9 % python3 Assignment9_4.py
    Enter the upper limit number to sum up to: 10000000

    Calculating sum from 1 to 10000000

    Normal sum: 50000005000000, Time taken: 0.2021 seconds
    Threading sum: 50000005000000, Time taken: 0.2030 seconds
    Multiprocessing sum: 50000005000000, Time taken: 0.1957 seconds
    macbook@Macbooks-MacBook-Pro Assignment_9 % python3 Assignment9_4.py
    Enter the upper limit number to sum up to: 100000000

    Calculating sum from 1 to 100000000

    Normal sum: 5000000050000000, Time taken: 1.9269 seconds
    Threading sum: 5000000050000000, Time taken: 1.9623 seconds
    Multiprocessing sum: 5000000050000000, Time taken: 0.7314 seconds
    macbook@Macbooks-MacBook-Pro Assignment_9 % python3 Assignment9_4.py
    Enter the upper limit number to sum up to: 1000000000

    Calculating sum from 1 to 1000000000

    Normal sum: 500000000500000000, Time taken: 19.0462 seconds
    Threading sum: 500000000500000000, Time taken: 20.0505 seconds
    Multiprocessing sum: 500000000500000000, Time taken: 5.6771 seconds
    macbook@Macbooks-MacBook-Pro Assignment_9 % 
"""