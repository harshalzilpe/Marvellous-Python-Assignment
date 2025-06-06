""" 
    Create a class Vehicle with method start(). 
    Derive class Car and override the method start() with additional behavior. Show method overriding.
"""
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a keyless push button...")
        
def main():
    choice = input("Enter vehicle type (vehicle/car): ").strip().lower()

    if choice == "vehicle":
        v = Vehicle()
        v.start()
    elif choice == "car":
        c = Car()
        c.start()
    else:
        print("Invalid input. Please enter 'vehicle' or 'car'.")
    
if __name__ == "__main__":
    main()

"""  
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_8.py
    Enter vehicle type (vehicle/car): Car
    Car is starting with a keyless push button...
    macbook@Macbooks-MacBook-Pro Assignment_14 % python3 Assignment14_8.py
    Enter vehicle type (vehicle/car): Vehicle
    Vehicle is starting...
    macbook@Macbooks-MacBook-Pro Assignment_14 % 
"""