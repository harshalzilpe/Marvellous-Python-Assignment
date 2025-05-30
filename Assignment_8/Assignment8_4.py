""" 
    Design python application which creates three threads as small, capital, digits. All the 
    threads accepts string as parameter. Small thread display number of small character, capital
    thread display number of capital characters and digits thread display number of digits. Display
    id and name of each thread.
"""
import threading

class Small(threading.Thread):
    def __init__(self, text):
        super().__init__(name="SmallThread")
        self.text = text

    def run(self):
        count = 0
        for c in self.text:
            if 'a' <= c <= 'z':
                count += 1
        print(f"Thread Name: {self.name}, ID: {threading.get_ident()}, Small letters: {count}")

class Capital(threading.Thread):
    def __init__(self, text):
        super().__init__(name="CapitalThread")
        self.text = text

    def run(self):
        count = 0
        for c in self.text:
            if 'A' <= c <= 'Z':  
                count += 1
        print(f"Thread Name: {self.name}, ID: {threading.get_ident()}, Capital letters: {count}")

class Digit(threading.Thread):
    def __init__(self, text):
        super().__init__(name="DigitThread")
        self.text = text

    def run(self):
        count = 0
        for c in self.text:
            if '0' <= c <= '9':  
                count += 1
        print(f"Thread Name: {self.name}, ID: {threading.get_ident()}, Digits: {count}")

def main():
    
    str = input("Enter a string: ")

    t1 = Small(str)
    t2 = Capital(str)
    t3 = Digit(str)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_8 % python3 Assignment8_4.py
    Enter a string: Jay Ganesh 101121
    Thread Name: SmallThread, ID: 123145414426624, Small letters: 7
    Thread Name: CapitalThread, ID: 123145431216128, Capital letters: 2
    Thread Name: DigitThread, ID: 123145448005632, Digits: 6
    macbook@Macbooks-MacBook-Pro Assignment_8 %   
"""