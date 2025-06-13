""" 
    Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt.
"""
import schedule, time
from datetime import datetime

def CurrentTime():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file = open('Marvellous.txt', 'a')
    file.write(current_time + '\n')
    file.close()
    print(f"Time written to file: {current_time}")
    
def main():
    schedule.every(5).minutes.do(CurrentTime)

    while True:
        schedule.run_pending()
        time.sleep(1)
                
if __name__ == "__main__":
    main()

"""  
    macbook@192 Assignment_17 % python3 Assignment17_5.py
    Time written to file: 2025-06-14 01:28:11
    Time written to file: 2025-06-14 01:33:12
    Time written to file: 2025-06-14 01:38:13
    ^Z
    zsh: suspended  python3 Assignment17_5.py
    macbook@192 Assignment_17 % 
"""