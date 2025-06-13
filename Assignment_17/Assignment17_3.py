""" 
    Write a program that schedules a function to print "Do Coding...!" every 30minutes.
"""
import schedule, time

def main():
    print("Do Coding...!")

    schedule.every(30).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
            
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_17 % python3 Assignment17_3.py
    Do Coding...!
    Do Coding...!
    ^Z
    zsh: suspended  python3 Assignment17_3.py
    macbook@192 Assignment_17 % 
"""