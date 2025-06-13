""" 
    Schedule a task that displays the current date and time every minute using the datetime module.
"""
import datetime, time

def main():
    while True:
        now = datetime.datetime.now()
        print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(60)
            
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_17 % python3 Assignment17_2.py
    Current Date and Time: 2025-06-14 01:09:38
    Current Date and Time: 2025-06-14 01:10:38
    Current Date and Time: 2025-06-14 01:11:38
    ^Z
    zsh: suspended  python3 Assignment17_2.py
    macbook@192 Assignment_17 % 
"""