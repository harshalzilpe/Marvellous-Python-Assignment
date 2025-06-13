""" 
    Create a task that runs once every day at 9:00 AM and prints "Namskar..."
"""
import schedule, time

def main():
    print("Namskar...")

    schedule.every().day.at("09:00").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
            
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_17 % python3 Assignment17_4.py
    Namskar...
    Namskar...
    Namskar...
    ^Z
    zsh: suspended  python3 Assignment17_4.py
    macbook@192 Assignment_17 % 
"""