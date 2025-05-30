""" 
    Write a python program using multiprocessing.Process to square a list of numbers using multiple processes.
"""
import multiprocessing

def squareNum(numbers, result, index):
    squared = [n ** 2 for n in numbers]
    result[index] = squared

def main():
    nums = input("Enter numbers: ").strip().split()
    numbers = list(map(int, nums))

    no_processes = 2
    size = (len(numbers) + no_processes - 1) // no_processes
    str = [numbers[i*size:(i+1)*size] for i in range(no_processes)]

    manager = multiprocessing.Manager()
    result = manager.list([[]] * no_processes)

    processes = []
    for i in range(no_processes):
        p = multiprocessing.Process(target=squareNum, args=(str[i], result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    squared_numbers = []
    for part in result:
        squared_numbers.extend(part)

    print("Squared numbers:", squared_numbers)
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_9 % python3 Assignment9_2.py
    Enter numbers: 1 2 3 4 5 6 7 8 9 10
    Squared numbers: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    macbook@Macbooks-MacBook-Pro Assignment_9 % 
"""